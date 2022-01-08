from a2qt import QtWidgets, QtCore

class HoverWidget(QtWidgets.QWidget):
    clicked: QtCore.Signal = ...
    context_menu_requested: QtCore.Signal = ...
    mouse_pressed: QtCore.Signal = ...
    mouse_released: QtCore.Signal = ...
    def add_widget(self, widget: QtWidgets.QWidget) -> None: ...
    def set_hover_widget(self, widget: QtWidgets.QWidget) -> None: ...