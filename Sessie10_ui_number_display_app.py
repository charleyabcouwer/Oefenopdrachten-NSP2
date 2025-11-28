# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sessie10_number_display_app.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 319)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textedit = QTextEdit(self.centralwidget)
        self.textedit.setObjectName(u"textedit")

        self.verticalLayout.addWidget(self.textedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.value = QSpinBox(self.centralwidget)
        self.value.setObjectName(u"value")
        self.value.setMinimum(1)
        self.value.setMaximum(28)

        self.horizontalLayout.addWidget(self.value)

        self.add_value_button = QPushButton(self.centralwidget)
        self.add_value_button.setObjectName(u"add_value_button")

        self.horizontalLayout.addWidget(self.add_value_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.quit_button = QPushButton(self.centralwidget)
        self.quit_button.setObjectName(u"quit_button")

        self.verticalLayout_5.addWidget(self.quit_button)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_value_button.setText(QCoreApplication.translate("MainWindow", u"Add value", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

