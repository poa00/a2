"""
Wrapper package to work with both PySide2 and PySide6.

Whatever is installed. Prefering stable PySide2 for now. Soon to be latest!
"""
try:
    import PySide6

    QT_VERSION = 6
    QT_PATH = PySide6.__path__[0]
except ImportError:
    try:
        import PySide2

        QT_VERSION = 5
        QT_PATH = PySide2.__path__[0]
    except ImportError:
        raise ImportError('No PySide found! We need either 2 or 6!')
