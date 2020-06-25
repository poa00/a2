"""
Editor stuff for module source package meta data.
"""
from copy import deepcopy

from PySide2 import QtWidgets, QtCore

import a2core
import a2ctrl
import a2download
from a2widget import a2input_dialog, modsource_editor_ui

log = a2core.get_logger(__name__)


class ModuleSourceEditor(a2input_dialog.A2ConfirmDialog):
    ctrl_change = QtCore.Signal(str)

    def __init__(self, mod_source, main=None):
        """
        :param a2mod.ModSource mod_source: Module source package to work on.
        """
        super(ModuleSourceEditor, self).__init__(
            main, f'Make a "{mod_source.name}" Release', 'blaaa')
        self.a2 = a2core.A2Obj.inst()
        self.main = main
        self.mod_source = mod_source
        self.source_cfg = deepcopy(mod_source.config)

        a2ctrl.check_ui_module(modsource_editor_ui)
        self.ui.attributes_widget = QtWidgets.QWidget(self)
        self.ui.main_layout.insertWidget(1, self.ui.attributes_widget)
        self.source_ui = modsource_editor_ui.Ui_ModSourceUi()
        self.source_ui.setupUi(self.ui.attributes_widget)
        self.source_ui.description.setMinimumWidth(600 * self.main.style.get('scale'))

        a2ctrl.connect.matching_controls(self.source_cfg, self.source_ui, self.ctrl_change)
        self.ctrl_change.connect(self._on_ctrl_change)
        self.source_ui.github_commits_btn.clicked.connect(self._fetch_github_commits)
        self.source_ui.github_commits_btn.setIcon(a2ctrl.Icons.inst().github)

        SemVerUiHandler(self, self.source_ui, self.source_cfg)

    def _on_ctrl_change(self, value):
        print('value: %s' % (value))
        print(self.source_cfg)

    def _fetch_github_commits(self):
        self.source_ui.busy_icon.set_busy()
        thread = self.mod_source.get_update_checker(self.main)
        thread.data_fetched.connect(self._show_check_result)
        thread.update_error.connect(self._show_error)
        thread.finished.connect(thread.deleteLater)
        thread.start()

    def _show_check_result(self, result):
        owner, repo = a2download.get_github_owner_repo(result['update_url'])
        compare_url = a2download.GITHUB_COMPARE_TEMPLATE.format(
            owner=owner, repo=repo, from_tag=result['version'],
            to_tag=self.source_cfg.get('main_branch', a2download.DEFAULT_MAIN_BRANCH))
        thread = a2download.GetJSONThread(self, compare_url)
        thread.data_fetched.connect(self._show_check_result2)
        thread.error.connect(self._show_error)
        thread.finished.connect(thread.deleteLater)
        thread.start()

    def _show_check_result2(self, result):
        messages = []
        for commit in result.get('commits', ()):
            message = commit.get('commit', {}).get('message', '').strip()
            if not message:
                continue
            this_lines = message.replace('\n\n', '\n').split('\n')
            messages.append('\n  '.join(['* ' + this_lines[0]] + this_lines[1:]))

        self.source_ui.news.setText('\n'.join(messages))
        self.source_ui.busy_icon.set_idle()

    def _show_error(self, error):
        self.source_ui.busy_icon.set_idle()
        print('_show_error: %s' % error)


class SemVerUiHandler(QtCore.QObject):
    def __init__(self, parent, ui, cfg):
        super(SemVerUiHandler, self).__init__(parent)
        self.ui = ui
        self.cfg = cfg
        self.vuis = (self.ui.version_major, self.ui.version_minor, self.ui.version_patch)
        self.show_version()
        self.ui.version_str.textEdited.connect(self._check_version_str)
        for widget in self.vuis:
            widget.valueChanged.connect(self._set_version_str)
        self.ui.version_str_check.clicked[bool].connect(self.version_toggle)

    def version_toggle(self, state):
        if state:
            self.ui.version_str.setText(self.cfg_version)
        else:
            semver, _ = get_semver(self.cfg_version)
            self._set_semver(semver)
        self.ui.version_str.setVisible(state)
        self.ui.version_semantic.setVisible(not state)

    def _set_semver(self, semver_list):
        for i, number in enumerate(semver_list):
            self.vuis[i].setValue(number)

    def show_version(self):
        semver, success = get_semver(self.cfg_version)
        if success:
            self.ui.version_str.hide()
            self._set_semver(semver)
        else:
            self.ui.version_str.setText(self.cfg_version)
            self.ui.version_semantic.hide()

    def _check_version_str(self, str_version):
        _, success = get_semver(str_version)
        if success:
            self.ui.version_str_check.setEnabled(True)
        else:
            self.ui.version_str_check.setEnabled(False)
        self.cfg_version = str_version

    def _set_version_str(self):
        self.cfg_version = '.'.join(str(w.value()) for w in self.vuis)

    @property
    def cfg_version(self):
        return self.cfg.get('version', '')

    @cfg_version.setter
    def cfg_version(self, version_str):
        self.cfg['version'] = version_str


def get_semver(version_str):
    """
    Get semantic versioning (major, minor, patch) from a string.

    :param str version_str: Input string to separate if possible.
    :return: Tuple of list len 3 with version ints and success boolean.
    :rtype: tuple[list[int, int, int], bool]
    """
    result = [0, 0, 0]
    for i, part in enumerate(version_str.split('.', 3)):
        try:
            result[i] = int(part)
        except ValueError:
            return (result, False)
    return (result, True)