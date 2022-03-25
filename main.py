from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(600, 300)
window.setWindowTitle("测试")

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入：")
textEdit.resize(300, 350)
textEdit.move(10, 10)

button = QPushButton("按钮", window)
button.move(350, 50)

window.show()

app.exec_()
