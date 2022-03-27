# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 583)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.method = QComboBox(self.centralwidget)
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.setObjectName(u"method")
        self.method.setGeometry(QRect(20, 20, 91, 31))
        self.method.setStyleSheet(u"font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.URL = QLineEdit(self.centralwidget)
        self.URL.setObjectName(u"URL")
        self.URL.setGeometry(QRect(120, 20, 391, 31))
        self.URL.setStyleSheet(u"font: 9pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.sender = QPushButton(self.centralwidget)
        self.sender.setObjectName(u"sender")
        self.sender.setGeometry(QRect(520, 20, 81, 31))
        self.sender.setStyleSheet(u"font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(170, 60, 41, 31))
        self.add.setStyleSheet(u"font: 25 14pt \"Adobe \u5b8b\u4f53 Std L\";")
        self.dele = QPushButton(self.centralwidget)
        self.dele.setObjectName(u"dele")
        self.dele.setGeometry(QRect(220, 60, 41, 31))
        self.dele.setStyleSheet(u"font: 25 14pt \"Adobe \u5b8b\u4f53 Std L\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 70, 51, 21))
        self.label.setStyleSheet(u"font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 100, 271, 192))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(330, 100, 261, 191))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 70, 51, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"Adobe \u9ed1\u4f53 Std R\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 639, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u754c\u9762", None))
        self.method.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.method.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))
        self.method.setItemText(2, QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.method.setItemText(3, QCoreApplication.translate("MainWindow", u"PUT", None))

        self.URL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165URL", None))
        self.sender.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.dele.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6c42\u5934", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u503c", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6c42\u4f53", None))
    # retranslateUi

