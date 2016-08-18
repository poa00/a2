"""
a2ui - setup interface for an Autohotkey environment.
"""
import os
import logging
import threading
import subprocess

import ahk
import a2core
import a2ctrl
import a2design_ui

from copy import deepcopy
from functools import partial
from PySide import QtGui, QtCore


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
reload_modules = [a2ctrl]


class A2Window(QtGui.QMainWindow):
    # to be triggered whenever a module or module source is dis/enabled
    module_enabled = QtCore.Signal()

    def __init__(self, app=None, *args):
        super(A2Window, self).__init__(parent=None)
        self.a2 = a2core.A2Obj.inst()
        self.app = app
        self._restart_thread = None

        self.dev_mode = self.a2.db.get('dev_mode') or False
        self.devset = DevSettings(self.a2)
        self._setup_ui()

        self.ui.module_list.draw_modules()
        self.ui.module_list.selection_changed.connect(self.module_selected)

        # TODO: make this optional
        self.scriptEditor = 'C:/Users/eRiC/io/tools/np++/notepad++.exe'
        self.edit_clipboard = []
        self.tempConfig = None
        self.selected = []
        self.mod = None
        self.scopes = {}

        init_selection = []
        if self.a2.db.get('remember_last') or False:
            init_selection = self.a2.db.get('last_selected') or []
        self.ui.module_list.select(init_selection)

        log.info('initialised!')

    def module_selected(self, module_list):
        self.selected = module_list
        self.num_selected = len(module_list)
        if self.num_selected == 1:
            self.mod = module_list[0]
        else:
            self.mod = None
        self.ui.module_view.draw_mod()

    def _setup_ui(self):
        if self.dev_mode:
            a2ctrl.check_ui_module(a2design_ui)
            a2ctrl.check_all_ui()
        a2ctrl.adjustSizes(self.app)

        self.ui = a2design_ui.Ui_a2MainWindow()
        self.ui.setupUi(self)

        self.ui.module_view.setup_ui(self)

        self._setup_actions()
        self._setup_shortcuts()

        self.toggle_dev_menu()
        self.setWindowIcon(a2ctrl.Icons.inst().a2)

    def _setup_actions(self):
        self.ui.actionEdit_module.triggered.connect(self.edit_mod)
        self.ui.actionEdit_module.setShortcut('Ctrl+E')
        self.ui.actionDisable_all_modules.triggered.connect(self.mod_disable_all)
        self.ui.actionExplore_to.triggered.connect(self.explore_mod)
        self.ui.actionAbout_a2.triggered.connect(partial(a2core.surfTo, self.a2.urls.help))
        self.ui.actionAbout_a2.setShortcut('F1')
        self.ui.actionAbout_Autohotkey.triggered.connect(partial(a2core.surfTo, self.a2.urls.ahk))
        self.ui.actionAbout_a2.setIcon(a2ctrl.Icons.inst().a2help)
        self.ui.actionAbout_Autohotkey.setIcon(a2ctrl.Icons.inst().autohotkey)

        self.ui.actionExplore_to_a2_dir.triggered.connect(self.explore_a2)
        #self.ui.actionNew_module.triggered.connect(self.newModule)
        self.ui.actionA2_settings.triggered.connect(partial(self.ui.module_list.select, None))
        self.ui.actionA2_settings.setIcon(a2ctrl.Icons.inst().a2)
        self.ui.actionDev_settings.triggered.connect(partial(self.ui.module_list.select, None))
        self.ui.actionExit_a2.setIcon(a2ctrl.Icons.inst().a2close)
        self.ui.actionExit_a2.triggered.connect(self.close)
        self.ui.actionRefresh_UI.triggered.connect(partial(self.settings_changed, refresh_ui=True))
        self.ui.actionRefresh_UI.setIcon(a2ctrl.Icons.inst().a2reload)
        self.ui.actionRefresh_UI.setShortcut('F5')

        self.ui.actionTest_restorewin.triggered.connect(self._testOutOfScreen)
        self.restoreA2ui()

    def _setup_shortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape),
                        self, self.escape)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Enter),
                        self, self.edit_submit)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Return),
                        self, self.edit_submit)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_S),
                        self, self.edit_submit)
#        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F5), self,
#                        partial(self.settings_changed, refresh_ui=True))

        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Home), self.ui.module_view.ui.scrollArea,
                        partial(self.scroll_to, True))
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_End), self.ui.module_view.ui.scrollArea,
                        partial(self.scroll_to, False))

    def edit_mod(self):
        if self.num_selected == 1:
            self.ui.module_view.edit_mod()

    def toggle_dev_menu(self, state=None):
        if state is None:
            # state=None happens only on startup
            state = self.a2.db.get('dev_mode') or False
            # if True we dont have to re-add
            if state is True:
                return
        if state:
            self.ui.menubar.insertAction(self.ui.menuHelp.menuAction(),
                                         self.ui.menuDev.menuAction())
        else:
            self.ui.menubar.removeAction(self.ui.menuDev.menuAction())

    def edit_submit(self):
        """
        Calls the mod to write the tempConfig to disc.
        If it's enabled only trigger settingsChanged when

        """
        if not self.ui.module_view.editing:
            return

        self.mod.config = deepcopy(self.tempConfig)
        if self.mod.name in self.a2.db.get('enabled') or []:
            self.mod.change()
            self.settings_changed()
        self.drawMod()

    def mod_enable(self, checked=None):
        """
        Handles the module checkbox to enable/disable one or multiple modules
        """
        check_box = self.ui.module_view.ui.modCheck
        if check_box.isTristate() or not checked:
            for mod in self.selected:
                mod.enabled = False
            checked = False
        else:
            for mod in self.selected:
                mod.enabled = True
            checked = True

        check_box.setTristate(False)
        check_box.setChecked(checked)
        self.settings_changed()

    def mod_disable_all(self):
        self.a2.enabled = {}
        self.settings_changed(refresh_ui=True)

    def settings_changed(self, specific=None, refresh_ui=False):
        if self._restart_thread is not None:
            self._restart_thread.quit()

        # kill old a2 process
        threading.Thread(target=ahk.killA2process).start()
        self.ui.module_list.draw_modules()

        a2core.write_includes(specific)

        self._restart_thread = RestartThread(self.a2, self)
        self._restart_thread.start()

        if refresh_ui:
            self.ui.module_view.draw_mod()

    def escape(self):
        if self.ui.module_view.editing:
            self.ui.module_view.draw_mod()
        else:
            self.close()

    def explore_mod(self):
        if self.mod is not None:
            subprocess.Popen(['explorer.exe', self.mod.path])

    def explore_a2(self):
        subprocess.Popen(['explorer.exe', self.a2.paths.a2])

    def closeEvent(self, event):
        binprefs = str(self.saveGeometry().toPercentEncoding())
        self.a2.db.set('windowprefs', {'splitter': self.ui.splitter.sizes(), 'geometry': binprefs})
        self.a2.db.set('last_selected', [m.key for m in self.selected])
        if self._restart_thread is not None:
            self._restart_thread.quit()
        QtGui.QMainWindow.closeEvent(self, event)

    def restoreA2ui(self):
        """
        gets window settings from prefs and makes sure the window will be visible
        I let Qt handle that via restoreGeometry. Downside is: It does not put back windows
        that are partiall outside of the left,right and bottom desktop border
        """
        winprefs = self.a2.db.get('windowprefs') or {}
        geometry = winprefs.get('geometry')
        if geometry is not None:
            geometry = QtCore.QByteArray().fromPercentEncoding(geometry)
            self.restoreGeometry(geometry)
        splitterSize = winprefs.get('splitter')
        if splitterSize is not None:
            self.ui.splitter.setSizes(winprefs['splitter'])

    def showRaise(self):
        self.show()
        self.activateWindow()
        #self.setFocus()

    def scroll_to(self, value, smooth=False):
        # TODO: reimplement in each widget
        pass

    def _testOutOfScreen(self):
        h = self.app.desktop().height()
        log.debug('h: %s' % h)
        geo = self.geometry()
        geo.setY(geo.x() + h)
        self.setGeometry(geo)
        log.debug('geo: %s' % self.geometry())


class RestartThread(QtCore.QThread):
    def __init__(self, a2, parent):
        self.a2 = a2
        super(RestartThread, self).__init__(parent)

    def run(self, *args, **kwargs):
        self.msleep(300)
        ahkProcess = QtCore.QProcess()
        ahkProcess.startDetached(self.a2.paths.autohotkey, [self.a2.paths.a2_script], self.a2.paths.a2)
        return QtCore.QThread.run(self, *args, **kwargs)


class DevSettings(object):
    def __init__(self, a2):
        self._enabled = False
        self.author_name = ''
        self.author_url = ''
        self.code_editor = ''
        self.json_indent = 2

        self._a2 = a2
        self._defaults = {'author_name': os.getenv('USERNAME'),
                          'author_url': '',
                          'code_editor': '',
                          'json_indent': 2}
        self._get()

    def _get(self):
        settings = self._a2.db.get('dev_settings') or {}
        for key, default in self._defaults.items():
            if key in settings and settings[key] != default:
                setattr(self, key, settings[key])
            else:
                setattr(self, key, default)

    def set(self, this):
        #settings = self.a2.db.get('dev_settings') or {}
        for key, default in self._defaults.items():
            if key in this and this[key] == default:
                del this[key]
        print('this: %s' % this)
        self._a2.db.set('dev_settings', this)


if __name__ == '__main__':
    import a2app
    a2app.main()
