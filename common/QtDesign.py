from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox


# QtDesign UI导入类
class QtDesign:

    def __init__(self):
        # 从文件加载UI定义
        file_stats = QFile("UI/test.ui")
        # file_stats.open(QFile.ReadOnly)
        # file_stats.close()

        self.window = QUiLoader().load(file_stats)
        self.window.button.clicked.connect(self.test_event)

    def test_event(self):
        info = self.window.text_edit.toPlainText()
        QMessageBox.about(self.window, "测试结果", info)
