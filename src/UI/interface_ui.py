# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_SimulatorGenerator(object):
    def setupUi(self, SimulatorGenerator):
        if not SimulatorGenerator.objectName():
            SimulatorGenerator.setObjectName(u"SimulatorGenerator")
        SimulatorGenerator.resize(317, 579)
        self.centralwidget = QWidget(SimulatorGenerator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 60, 281, 101))
        self.radioButton_JSON = QRadioButton(self.groupBox)
        self.radioButton_JSON.setObjectName(u"radioButton_JSON")
        self.radioButton_JSON.setGeometry(QRect(10, 30, 100, 23))
        self.radioButton_XCI = QRadioButton(self.groupBox)
        self.radioButton_XCI.setObjectName(u"radioButton_XCI")
        self.radioButton_XCI.setGeometry(QRect(10, 60, 100, 23))
        self.lineEdit_JSON = QLineEdit(self.groupBox)
        self.lineEdit_JSON.setObjectName(u"lineEdit_JSON")
        self.lineEdit_JSON.setGeometry(QRect(70, 30, 113, 25))
        self.lineEdit_JSON.setReadOnly(True)
        self.lineEdit_XCI = QLineEdit(self.groupBox)
        self.lineEdit_XCI.setObjectName(u"lineEdit_XCI")
        self.lineEdit_XCI.setGeometry(QRect(70, 60, 113, 25))
        self.lineEdit_XCI.setReadOnly(True)
        self.pushButton_Search_JSON = QPushButton(self.groupBox)
        self.pushButton_Search_JSON.setObjectName(u"pushButton_Search_JSON")
        self.pushButton_Search_JSON.setGeometry(QRect(190, 30, 80, 25))
        self.pushButton_Search_XCI = QPushButton(self.groupBox)
        self.pushButton_Search_XCI.setObjectName(u"pushButton_Search_XCI")
        self.pushButton_Search_XCI.setGeometry(QRect(190, 60, 80, 25))
        self.pushButton_output_path = QPushButton(self.centralwidget)
        self.pushButton_output_path.setObjectName(u"pushButton_output_path")
        self.pushButton_output_path.setGeometry(QRect(200, 390, 80, 25))
        self.lineEdit_output_path = QLineEdit(self.centralwidget)
        self.lineEdit_output_path.setObjectName(u"lineEdit_output_path")
        self.lineEdit_output_path.setGeometry(QRect(32, 390, 161, 25))
        self.lineEdit_output_path.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 370, 91, 17))
        self.checkBox_readme = QCheckBox(self.centralwidget)
        self.checkBox_readme.setObjectName(u"checkBox_readme")
        self.checkBox_readme.setGeometry(QRect(20, 450, 301, 23))
        self.textEdit_Files = QTextEdit(self.centralwidget)
        self.textEdit_Files.setObjectName(u"textEdit_Files")
        self.textEdit_Files.setGeometry(QRect(30, 230, 251, 111))
        self.textEdit_Files.setReadOnly(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 210, 111, 17))
        self.pushButton_generate = QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName(u"pushButton_generate")
        self.pushButton_generate.setGeometry(QRect(200, 500, 80, 25))
        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(110, 500, 80, 25))
        self.checkBox_sim_folder = QCheckBox(self.centralwidget)
        self.checkBox_sim_folder.setObjectName(u"checkBox_sim_folder")
        self.checkBox_sim_folder.setGeometry(QRect(20, 420, 301, 23))
        SimulatorGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SimulatorGenerator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 317, 21))
        SimulatorGenerator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SimulatorGenerator)
        self.statusbar.setObjectName(u"statusbar")
        SimulatorGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(SimulatorGenerator)

        QMetaObject.connectSlotsByName(SimulatorGenerator)
    # setupUi

    def retranslateUi(self, SimulatorGenerator):
        SimulatorGenerator.setWindowTitle(QCoreApplication.translate("SimulatorGenerator", u"Simulator Generator", None))
        self.groupBox.setTitle(QCoreApplication.translate("SimulatorGenerator", u"Vivado blocks", None))
        self.radioButton_JSON.setText(QCoreApplication.translate("SimulatorGenerator", u"JSON", None))
        self.radioButton_XCI.setText(QCoreApplication.translate("SimulatorGenerator", u"XCI", None))
        self.pushButton_Search_JSON.setText(QCoreApplication.translate("SimulatorGenerator", u"Search", None))
        self.pushButton_Search_XCI.setText(QCoreApplication.translate("SimulatorGenerator", u"Search", None))
        self.pushButton_output_path.setText(QCoreApplication.translate("SimulatorGenerator", u"Search", None))
        self.label.setText(QCoreApplication.translate("SimulatorGenerator", u"Output files", None))
        self.checkBox_readme.setText(QCoreApplication.translate("SimulatorGenerator", u"Add README with simulation commands", None))
        self.label_2.setText(QCoreApplication.translate("SimulatorGenerator", u"Files to generate", None))
        self.pushButton_generate.setText(QCoreApplication.translate("SimulatorGenerator", u"Generate", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("SimulatorGenerator", u"Cancel", None))
        self.checkBox_sim_folder.setText(QCoreApplication.translate("SimulatorGenerator", u"Create SIM folder", None))
    # retranslateUi

