"""
a2qt Qt for Python wrapper.
"""
import a2qt

if a2qt.QT_VERSION == 6:
    from PySide6.QtWidgets import *

else:
    from PySide2.QtWidgets import (
        QAbstractButton, QAbstractGraphicsShapeItem, QAbstractItemDelegate,
        QAbstractItemView, QAbstractScrollArea, QAbstractSlider,
        QAbstractSpinBox, QAccessibleWidget, QApplication, QBoxLayout,
        QButtonGroup, QCalendarWidget, QCheckBox, QColorDialog, QColormap,
        QColumnView, QComboBox, QCommandLinkButton, QCommonStyle, QCompleter,
        QDataWidgetMapper, QDateEdit, QDateTimeEdit, QDial, QDialog,
        QDialogButtonBox, QDockWidget, QDoubleSpinBox, QErrorMessage,
        QFileDialog, QFileIconProvider, QFileSystemModel, QFocusFrame,
        QFontComboBox, QFontDialog, QFormLayout, QFrame, QGesture, QGestureEvent,
        QGestureRecognizer, QGraphicsAnchor, QGraphicsAnchorLayout,
        QGraphicsBlurEffect, QGraphicsColorizeEffect, QGraphicsDropShadowEffect,
        QGraphicsEffect, QGraphicsEllipseItem, QGraphicsGridLayout,
        QGraphicsItem, QGraphicsItemAnimation, QGraphicsItemGroup,
        QGraphicsLayout, QGraphicsLayoutItem, QGraphicsLineItem,
        QGraphicsLinearLayout, QGraphicsObject, QGraphicsOpacityEffect,
        QGraphicsPathItem, QGraphicsPixmapItem, QGraphicsPolygonItem,
        QGraphicsProxyWidget, QGraphicsRectItem, QGraphicsRotation,
        QGraphicsScale, QGraphicsScene, QGraphicsSceneContextMenuEvent,
        QGraphicsSceneDragDropEvent, QGraphicsSceneEvent,
        QGraphicsSceneHelpEvent, QGraphicsSceneHoverEvent,
        QGraphicsSceneMouseEvent, QGraphicsSceneMoveEvent,
        QGraphicsSceneResizeEvent, QGraphicsSceneWheelEvent,
        QGraphicsSimpleTextItem, QGraphicsTextItem, QGraphicsTransform,
        QGraphicsView, QGraphicsWidget, QGridLayout, QGroupBox, QHBoxLayout,
        QHeaderView, QInputDialog, QItemDelegate, QItemEditorCreatorBase,
        QItemEditorFactory, QKeySequenceEdit, QLCDNumber, QLabel, QLayout,
        QLayoutItem, QLineEdit, QListView, QListWidget, QListWidgetItem,
        QMainWindow, QMdiArea, QMdiSubWindow, QMenu, QMenuBar, QMessageBox,
        QPanGesture, QPinchGesture, QPlainTextDocumentLayout, QPlainTextEdit,
        QProgressBar, QProgressDialog, QProxyStyle, QPushButton, QRadioButton,
        QRubberBand, QScrollArea, QScrollBar, QScroller, QScrollerProperties,
        QSizeGrip, QSizePolicy, QSlider, QSpacerItem, QSpinBox, QSplashScreen,
        QSplitter, QSplitterHandle, QStackedLayout, QStackedWidget, QStatusBar,
        QStyle, QStyleFactory, QStyleHintReturn, QStyleHintReturnMask,
        QStyleHintReturnVariant, QStyleOption, QStyleOptionButton,
        QStyleOptionComboBox, QStyleOptionComplex, QStyleOptionDockWidget,
        QStyleOptionFocusRect, QStyleOptionFrame, QStyleOptionGraphicsItem,
        QStyleOptionGroupBox, QStyleOptionHeader, QStyleOptionMenuItem,
        QStyleOptionProgressBar, QStyleOptionRubberBand, QStyleOptionSizeGrip,
        QStyleOptionSlider, QStyleOptionSpinBox, QStyleOptionTab,
        QStyleOptionTabBarBase, QStyleOptionTabWidgetFrame, QStyleOptionTitleBar,
        QStyleOptionToolBar, QStyleOptionToolBox, QStyleOptionToolButton,
        QStyleOptionViewItem, QStylePainter, QStyledItemDelegate, QSwipeGesture,
        QSystemTrayIcon, QTabBar, QTabWidget, QTableView, QTableWidget,
        QTableWidgetItem, QTableWidgetSelectionRange, QTapAndHoldGesture,
        QTapGesture, QTextBrowser, QTextEdit, QTileRules, QTimeEdit, QToolBar,
        QToolBox, QToolButton, QToolTip, QTreeView, QTreeWidget, QTreeWidgetItem,
        QTreeWidgetItemIterator, QUndoView, QVBoxLayout, QWhatsThis, QWidget,
        QWidgetAction, QWidgetItem, QWizard, QWizardPage)
    QApplication.exec = QApplication.exec_
