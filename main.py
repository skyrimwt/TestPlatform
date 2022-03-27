from PySide2.QtWidgets import QApplication, QMainWindow
from common.QtCode import QtCode
from common.QtDesign import QtDesign
from UI.test import Ui_MainWindow

app = QApplication([])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    test = QtCode()
    # test = QtDesign()
    # test = MainWindow()
    # test.show()
    test.window.show()
    app.exec_()
