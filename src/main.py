from PySide6.QtWidgets import QApplication
import sys
from GUI.interfaz_gui import *


if __name__ == "__main__":
    """Main process
    """
    app = QApplication(sys.argv)
    win = interfaz_gui()
    win.show()
    sys.exit(app.exec())