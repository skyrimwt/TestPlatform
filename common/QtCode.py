from PySide2.QtWidgets import QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QComboBox, QLineEdit, QLabel, \
    QTableWidget, QTextBrowser
from PySide2.QtCore import QSize, QCoreApplication
from PySide2.QtGui import QIcon, QFont


# Qt Code UI界面
class QtCode:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(750, 600)
        self.window.move(600, 300)
        self.window.setWindowTitle("HTTP测试工具")

        # 组合选择框
        self.ComboBox = QComboBox(parent=self.window)
        self.ComboBox.resize(80, 40)
        self.ComboBox.move(30, 10)
        self.ComboBox.setStyleSheet("font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.ComboBox.addItems(["GET", "POST", "DELETE", "PUT"])

        # 单行文本框
        self.LineEdit = QLineEdit(parent=self.window)
        self.LineEdit.setPlaceholderText("请输入URL：")
        self.LineEdit.resize(500, 40)
        self.LineEdit.move(130, 10)

        # 按钮
        self.button = QPushButton(text="按钮", parent=self.window)
        self.button.setText("发送")
        self.button.resize(80, 40)
        self.button.move(650, 10)
        # self.button.setEnabled(True)
        # self.button.setIcon(QIcon('1.png'))
        # self.button.setIconSize(QSize(30, 30))
        self.button.clicked.connect(self.request)

        self.add = QPushButton(text="+", parent=self.window)
        self.add.resize(30, 30)
        self.add.move(140, 70)
        self.add.clicked.connect(self.add_head)

        self.delete = QPushButton(text="-", parent=self.window)
        self.delete.resize(30, 30)
        self.delete.move(180, 70)
        self.delete.clicked.connect(self.delete_head)

        # 标签
        self.label = QLabel("请求头", parent=self.window)
        self.label.move(50, 70)
        self.label.setStyleSheet("font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")

        # 表格
        self.table = QTableWidget(self.window)
        self.table.resize(300, 200)
        self.table.move(30, 110)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["参数", "取值", "类型"])
        # self.table.setColumnWidth(0, 100)
        # self.table.setColumnWidth(1, 100)

        # 多行文本
        self.text_edit = QPlainTextEdit(self.window)
        self.text_edit.setPlaceholderText("请输入请求体参数：")
        self.text_edit.resize(300, 200)
        self.text_edit.move(400, 110)

        # 文本浏览框
        self.text_browser = QTextBrowser(self.window)
        self.text_browser.resize(650, 200)
        self.text_browser.move(30, 350)

    def request(self):
        method = self.ComboBox.currentText()
        url = self.LineEdit.text()
        rowcount = self.table.rowCount()
        header = {
            self.table.item(i, 0).text(): self.table.item(i, 1).text() for i in range(rowcount)
        }
        self.text_browser.setPlainText("{},{},{}".format(method, url, header))
        # info = self.text_edit.toPlainText(self.window)
        # QMessageBox.about(self.window, "测试结果", info)

    def add_head(self):
        rowcount = self.table.rowCount()
        self.table.insertRow(rowcount)

    def delete_head(self):
        current_row = self.table.currentRow()
        self.table.removeRow(current_row)
