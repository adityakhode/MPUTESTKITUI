# Author           : Aditya Khode
# Filename         : MPUTESTKITUI
# Functions        :  __init__ , setupUi , retranslateUi , toggleSettingWidget , buttons_initilised , exit , selectFile , saveDataBase , changeTheDatabase , goToSecondFrame , saveResult , secondFrameinit , backButtonFrame3 , thirdpage , backButtonFrame2 , main
# Global Variables : None



import os
import sys
import shutil
from src import assets
import webbrowser
from src.pdfAndQr import pdfAndQr
from src.databaseclass import DatabaseClass 
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    # Function Name : __init__
    # input         : None 
    # Output        : void
    # Logic         : Initilised database
    # example       : call Automatically called when object created
    def __init__(self) -> None:
        self.db = DatabaseClass()


    # Function Name : setupUi
    # input         : MainWindow 
    # Output        : void
    # Logic         : Initilised and configer all the UI elements sets all the property 
    #                 1)decleard mainwindow ,central widget footerframe and firstFrame
    #                 2)decleard database UI
    #                 3)decleard secondFrame 
    #                 4)decleard thirdFrame
    #                 5)initilised Necessary function
    # example       : object.Ui_MainWindow(MainWindow)
    #comments refer frontendImageExample for idea
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mainframe = QtWidgets.QFrame(self.centralwidget)
        self.Mainframe.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.Mainframe.setStyleSheet("")
        self.Mainframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe.setObjectName("Mainframe")
        self.footerframe = QtWidgets.QFrame(self.Mainframe)
        self.footerframe.setGeometry(QtCore.QRect(0, 420, 800, 71))
        self.footerframe.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(0, 0, 0);")
        self.footerframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footerframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footerframe.setObjectName("footerfrane")
        self.companyname = QtWidgets.QLabel(self.footerframe)
        self.companyname.setGeometry(QtCore.QRect(240, 0, 401, 61))
        self.companyname.setObjectName("companyname")
        self.logo = QtWidgets.QLabel(self.footerframe)
        self.logo.setGeometry(QtCore.QRect(10, -10, 231, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.background = QtWidgets.QLabel(self.Mainframe)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.background.setStyleSheet("background-image: url(:/background/backgroud.png);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/background/background.svg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.firstFrame = QtWidgets.QFrame(self.Mainframe)
        self.firstFrame.setGeometry(QtCore.QRect(70, 50, 691, 361))
        self.firstFrame.setStyleSheet("background-color: rgb(15, 0, 46);\n"
"border-radius:20px;")
        self.firstFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstFrame.setObjectName("firstFrame")
        self.TCDetails = QtWidgets.QLabel(self.firstFrame)
        self.TCDetails.setGeometry(QtCore.QRect(50, 20, 161, 16))
        self.TCDetails.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.TCDetails.setObjectName("TCDetails")
        self.UserDetails = QtWidgets.QLabel(self.firstFrame)
        self.UserDetails.setGeometry(QtCore.QRect(60, 160, 91, 16))
        self.UserDetails.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.189055 rgba(0, 0, 20, 0), stop:1 rgba(102, 0, 255, 0));")
        self.UserDetails.setObjectName("UserDetails")
        self.next = QtWidgets.QPushButton(self.firstFrame)
        self.next.setGeometry(QtCore.QRect(590, 320, 81, 31))
        self.next.setStyleSheet("/* QPushButton base style */\n"
"QPushButton {\n"
"    background-color: rgb(141, 145, 139);\n"
"    color: red;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QPushButton:hover {\n"
"    background-color: rgb(208, 187, 246);\n"
"    color: red;\n"
"}\n"
"\n"
"/* Clicked effect with padding */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"")
        self.next.setObjectName("next")
        self.UserDetailframe = QtWidgets.QFrame(self.firstFrame)
        self.UserDetailframe.setGeometry(QtCore.QRect(90, 190, 541, 111))
        self.UserDetailframe.setStyleSheet("background-color: rgb(25, 10, 87);\n"
"border-radius:15px;")
        self.UserDetailframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UserDetailframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UserDetailframe.setObjectName("UserDetailframe")
        self.Name = QtWidgets.QLabel(self.UserDetailframe)
        self.Name.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.Name.setObjectName("Name")
        self.Nameinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.Nameinput.setGeometry(QtCore.QRect(150, 10, 371, 16))
        self.Nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nameinput.setObjectName("Nameinput")
        self.Partnumberlable = QtWidgets.QLabel(self.UserDetailframe)
        self.Partnumberlable.setGeometry(QtCore.QRect(280, 36, 91, 21))
        self.Partnumberlable.setObjectName("Partnumberlable")
        self.Partnamelable = QtWidgets.QLabel(self.UserDetailframe)
        self.Partnamelable.setGeometry(QtCore.QRect(10, 37, 91, 20))
        self.Partnamelable.setObjectName("Partnamelable")
        self.partnameinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.partnameinput.setGeometry(QtCore.QRect(150, 40, 113, 16))
        self.partnameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.partnameinput.setObjectName("partnameinput")
        self.Partnumberinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.Partnumberinput.setGeometry(QtCore.QRect(410, 40, 113, 16))
        self.Partnumberinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Partnumberinput.setObjectName("Partnumberinput")
        self.Batchnumberlable = QtWidgets.QLabel(self.UserDetailframe)
        self.Batchnumberlable.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.Batchnumberlable.setObjectName("Batchnumberlable")
        self.Channlanolable = QtWidgets.QLabel(self.UserDetailframe)
        self.Channlanolable.setGeometry(QtCore.QRect(10, 80, 121, 20))
        self.Channlanolable.setObjectName("Channlanolable")
        self.ChallanQuantlable = QtWidgets.QLabel(self.UserDetailframe)
        self.ChallanQuantlable.setGeometry(QtCore.QRect(280, 60, 121, 20))
        self.ChallanQuantlable.setObjectName("ChallanQuantlable")
        self.ChallanDatelable = QtWidgets.QLabel(self.UserDetailframe)
        self.ChallanDatelable.setGeometry(QtCore.QRect(280, 80, 101, 20))
        self.ChallanDatelable.setObjectName("ChallanDatelable")
        self.BatchNoinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.BatchNoinput.setGeometry(QtCore.QRect(150, 60, 113, 16))
        self.BatchNoinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BatchNoinput.setObjectName("BatchNoinput")
        self.Challannumberinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.Challannumberinput.setGeometry(QtCore.QRect(150, 80, 113, 16))
        self.Challannumberinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Challannumberinput.setObjectName("Challannumberinput")
        self.ChallanQuatinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.ChallanQuatinput.setGeometry(QtCore.QRect(410, 60, 113, 16))
        self.ChallanQuatinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ChallanQuatinput.setObjectName("ChallanQuatinput")
        self.challanDateinput = QtWidgets.QLineEdit(self.UserDetailframe)
        self.challanDateinput.setGeometry(QtCore.QRect(410, 80, 113, 16))
        self.challanDateinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.challanDateinput.setObjectName("challanDateinput")
        self.TCframe = QtWidgets.QFrame(self.firstFrame)
        self.TCframe.setGeometry(QtCore.QRect(190, 60, 301, 80))
        self.TCframe.setMouseTracking(True)
        self.TCframe.setStyleSheet("background-color: rgb(25, 10, 87);\n"
"border-radius:15px;")
        self.TCframe.setInputMethodHints(QtCore.Qt.ImhDate)
        self.TCframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TCframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TCframe.setObjectName("TCframe")
        self.TCNoLable = QtWidgets.QLabel(self.TCframe)
        self.TCNoLable.setGeometry(QtCore.QRect(30, 10, 91, 17))
        self.TCNoLable.setObjectName("TCNoLable")
        self.TCDateLable = QtWidgets.QLabel(self.TCframe)
        self.TCDateLable.setGeometry(QtCore.QRect(30, 30, 91, 17))
        self.TCDateLable.setObjectName("TCDateLable")
        self.SupplierCodeLable = QtWidgets.QLabel(self.TCframe)
        self.SupplierCodeLable.setGeometry(QtCore.QRect(30, 50, 121, 17))
        self.SupplierCodeLable.setObjectName("SupplierCodeLable")
        self.TCNOinput = QtWidgets.QLineEdit(self.TCframe)
        self.TCNOinput.setGeometry(QtCore.QRect(150, 10, 113, 16))
        self.TCNOinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TCNOinput.setObjectName("TCNOinput")
        self.TCDateinput = QtWidgets.QLineEdit(self.TCframe)
        self.TCDateinput.setGeometry(QtCore.QRect(150, 30, 113, 16))
        self.TCDateinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TCDateinput.setObjectName("TCDateinput")
        self.SuppCodeinput = QtWidgets.QLineEdit(self.TCframe)
        self.SuppCodeinput.setGeometry(QtCore.QRect(150, 50, 113, 16))
        self.SuppCodeinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SuppCodeinput.setObjectName("SuppCodeinput")
        self.settings = QtWidgets.QPushButton(self.Mainframe)
        self.settings.setGeometry(QtCore.QRect(0, 5, 41, 41))
        self.settings.setStyleSheet("border-image: url(:/setting/setting.jpeg);\n"
"border-radius:20px;")
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.widget = QtWidgets.QWidget(self.Mainframe)
        self.widget.setGeometry(QtCore.QRect(0, 5, 791, 41))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.widget.setObjectName("widget")
        self.changeDatabase = QtWidgets.QPushButton(self.widget)
        self.changeDatabase.setGeometry(QtCore.QRect(110, 10, 131, 25))
        self.changeDatabase.setStyleSheet("border-radius:4px;\n"
"color:red;")
        self.changeDatabase.setObjectName("changeDatabase")
        self.contactUs = QtWidgets.QPushButton(self.widget)
        self.contactUs.setGeometry(QtCore.QRect(610, 10, 131, 25))
        self.contactUs.setStyleSheet("border-radius:4px;\n"
"color:red;")
        self.contactUs.setObjectName("contactUs")
        self.AboutUs = QtWidgets.QPushButton(self.widget)
        self.AboutUs.setGeometry(QtCore.QRect(360, 10, 131, 25))
        self.AboutUs.setStyleSheet("border-radius:4px;\n"
"color:red;")
        self.AboutUs.setObjectName("AboutUs")
        self.background.raise_()
        self.firstFrame.raise_()
        self.footerframe.raise_()
        self.widget.raise_()
        self.settings.raise_()


#------------------------------------database-------------------------------------------------#
        

        self.databaseFrame = QtWidgets.QFrame(self.Mainframe)
        self.databaseFrame.setGeometry(QtCore.QRect(40, 50, 721, 351))
        self.databaseFrame.setStyleSheet("background-color: rgb(15, 0, 46);\n"
"border-radius:20px;")
        self.databaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.databaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.databaseFrame.setObjectName("databaseFrame")
        self.header = QtWidgets.QLabel(self.databaseFrame)
        self.header.setGeometry(QtCore.QRect(0, 10, 711, 51))
        self.header.setObjectName("header")
        self.selectbutton = QtWidgets.QPushButton(self.databaseFrame)
        self.selectbutton.setGeometry(QtCore.QRect(200, 90, 311, 71))
        self.selectbutton.setStyleSheet("font-size:25px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.20402, y1:0, x2:1, y2:0.96, stop:0.19403 rgba(219, 0, 72, 212), stop:0.59204 rgba(3, 0, 255, 255));\n"
"color: rgb(0, 255, 0);\n"
"border-radius:8px;")
        self.selectbutton.setObjectName("selectbutton")
        self.savebutton = QtWidgets.QPushButton(self.databaseFrame)
        self.savebutton.setGeometry(QtCore.QRect(240, 230, 241, 51))
        self.savebutton.setStyleSheet("font-size:25px;\n"
"background-color: qlineargradient(spread:reflect, x1:0.20402, y1:0, x2:1, y2:0.96, stop:0.19403 rgba(219, 0, 72, 212), stop:0.59204 rgba(3, 0, 255, 255));\n"
"color: rgb(0, 255, 0);")
        self.savebutton.setObjectName("savebutton")

#----------------------------------------------------------------------------secondframe----------------------------------------------------------------------------#
        self.secondFrame = QtWidgets.QFrame(self.Mainframe)
        self.secondFrame.setGeometry(QtCore.QRect(10, 50, 781, 361))
        self.secondFrame.setStyleSheet("border-radius:20px;")
        self.secondFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondFrame.setObjectName("firstFrame")
        self.summary = QtWidgets.QLabel(self.secondFrame)
        self.summary.setGeometry(QtCore.QRect(550, 20, 161, 41))
        self.summary.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.20402, y1:0, x2:1, y2:0.948636, stop:0.19403 rgba(0, 219, 183, 180), stop:1 rgba(0, 213, 255, 108));\n"
"")
        self.summary.setObjectName("summary")
        self.frame = QtWidgets.QFrame(self.secondFrame)
        self.frame.setGeometry(QtCore.QRect(81, 70, 291, 251))
        self.frame.setStyleSheet("background-color: rgb(21, 6, 45);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.VoltageFrame = QtWidgets.QFrame(self.frame)
        self.VoltageFrame.setGeometry(QtCore.QRect(10, 130, 271, 51))
        self.VoltageFrame.setStyleSheet("background-color: rgb(45, 30, 72);\n"
"border-radius:15px;")
        self.VoltageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VoltageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VoltageFrame.setObjectName("VoltageFrame")
        self.Voltagelable = QtWidgets.QLabel(self.VoltageFrame)
        self.Voltagelable.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.Voltagelable.setObjectName("Voltagelable")
        self.Voltageideal = QtWidgets.QLabel(self.VoltageFrame)
        self.Voltageideal.setGeometry(QtCore.QRect(20, 27, 111, 21))
        self.Voltageideal.setObjectName("Voltageideal")
        self.voltageoutput = QtWidgets.QLabel(self.VoltageFrame)
        self.voltageoutput.setGeometry(QtCore.QRect(140, 10, 61, 31))
        self.voltageoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltageoutput.setObjectName("voltageoutput")
        self.voltageoutput_2 = QtWidgets.QLabel(self.VoltageFrame)
        self.voltageoutput_2.setGeometry(QtCore.QRect(210, 10, 61, 31))
        self.voltageoutput_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.voltageoutput_2.setObjectName("voltageoutput_2")
        self.SingleVoltageOutput = QtWidgets.QLabel(self.VoltageFrame)
        self.SingleVoltageOutput.setGeometry(QtCore.QRect(140, 10, 131, 31))
        self.SingleVoltageOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SingleVoltageOutput.setObjectName("SingleVoltageOutput")
        self.ResistanceFrame = QtWidgets.QFrame(self.frame)
        self.ResistanceFrame.setGeometry(QtCore.QRect(10, 10, 271, 51))
        self.ResistanceFrame.setStyleSheet("background-color: rgb(45, 30, 72);\n"
"border-radius:15px;")
        self.ResistanceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ResistanceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ResistanceFrame.setObjectName("ResistanceFrame")
        self.Resistancelable = QtWidgets.QLabel(self.ResistanceFrame)
        self.Resistancelable.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.Resistancelable.setObjectName("Resistancelable")
        self.Resistanceideal = QtWidgets.QLabel(self.ResistanceFrame)
        self.Resistanceideal.setGeometry(QtCore.QRect(10, 27, 121, 21))
        self.Resistanceideal.setObjectName("Resistanceideal")
        self.Resistanceoutput = QtWidgets.QLabel(self.ResistanceFrame)
        self.Resistanceoutput.setGeometry(QtCore.QRect(140, 10, 61, 31))
        self.Resistanceoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Resistanceoutput.setObjectName("Resistanceoutput")
        self.Resistanceoutput_2 = QtWidgets.QLabel(self.ResistanceFrame)
        self.Resistanceoutput_2.setGeometry(QtCore.QRect(210, 10, 61, 31))
        self.Resistanceoutput_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Resistanceoutput_2.setObjectName("Resistanceoutput_2")
        self.SingleResistranceOutput = QtWidgets.QLabel(self.ResistanceFrame)
        self.SingleResistranceOutput.setGeometry(QtCore.QRect(140, 10, 131, 31))
        self.SingleResistranceOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SingleResistranceOutput.setObjectName("SingleResistranceOutput")
        self.InductanceFrame = QtWidgets.QFrame(self.frame)
        self.InductanceFrame.setGeometry(QtCore.QRect(10, 70, 271, 51))
        self.InductanceFrame.setStyleSheet("background-color: rgb(45, 30, 72);\n"
"border-radius:15px;")
        self.InductanceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InductanceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InductanceFrame.setObjectName("InductanceFrame")
        self.InductanceLable = QtWidgets.QLabel(self.InductanceFrame)
        self.InductanceLable.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.InductanceLable.setObjectName("InductanceLable")
        self.InductanceIdeal = QtWidgets.QLabel(self.InductanceFrame)
        self.InductanceIdeal.setGeometry(QtCore.QRect(10, 27, 111, 21))
        self.InductanceIdeal.setObjectName("InductanceIdeal")
        self.inductanceoutput = QtWidgets.QLabel(self.InductanceFrame)
        self.inductanceoutput.setGeometry(QtCore.QRect(140, 10, 61, 31))
        self.inductanceoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inductanceoutput.setObjectName("inductanceoutput")
        self.inductanceoutput_2 = QtWidgets.QLabel(self.InductanceFrame)
        self.inductanceoutput_2.setGeometry(QtCore.QRect(210, 10, 61, 31))
        self.inductanceoutput_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inductanceoutput_2.setObjectName("inductanceoutput_2")
        self.SingleInductanceOutput = QtWidgets.QLabel(self.InductanceFrame)
        self.SingleInductanceOutput.setGeometry(QtCore.QRect(140, 10, 131, 31))
        self.SingleInductanceOutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SingleInductanceOutput.setObjectName("SingleInductanceOutput")
        self.FrequencyFrame = QtWidgets.QFrame(self.frame)
        self.FrequencyFrame.setGeometry(QtCore.QRect(10, 190, 271, 51))
        self.FrequencyFrame.setStyleSheet("background-color: rgb(45, 30, 72);\n"
"border-radius:15px;")
        self.FrequencyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrequencyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrequencyFrame.setObjectName("FrequencyFrame")
        self.FrequencyLable = QtWidgets.QLabel(self.FrequencyFrame)
        self.FrequencyLable.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.FrequencyLable.setObjectName("FrequencyLable")
        self.Frequencyideal = QtWidgets.QLabel(self.FrequencyFrame)
        self.Frequencyideal.setGeometry(QtCore.QRect(20, 27, 121, 21))
        self.Frequencyideal.setObjectName("Frequencyideal")
        self.frequencyoutput = QtWidgets.QLabel(self.FrequencyFrame)
        self.frequencyoutput.setGeometry(QtCore.QRect(140, 10, 61, 31))
        self.frequencyoutput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frequencyoutput.setObjectName("frequencyoutput")
        self.frequencyoutput_2 = QtWidgets.QLabel(self.FrequencyFrame)
        self.frequencyoutput_2.setGeometry(QtCore.QRect(210, 10, 61, 31))
        self.frequencyoutput_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frequencyoutput_2.setObjectName("frequencyoutput_2")
        self.SingleFrequency = QtWidgets.QLabel(self.FrequencyFrame)
        self.SingleFrequency.setGeometry(QtCore.QRect(140, 10, 131, 31))
        self.SingleFrequency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SingleFrequency.setObjectName("SingleFrequency")
        self.pushButton = QtWidgets.QPushButton(self.secondFrame)
        self.pushButton.setGeometry(QtCore.QRect(81, 20, 291, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:reflect, x1:0.20402, y1:0, x2:1, y2:0.948636, stop:0.19403 rgba(0, 219, 183, 180), stop:1 rgba(0, 213, 255, 108));\n"
"border-radius:20px;\n"
"font:18pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(138, 226, 52);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.stop = QtWidgets.QPushButton(self.secondFrame)
        self.stop.setGeometry(QtCore.QRect(110, 330, 231, 25))
        self.stop.setStyleSheet("QPushButton{\n"
"    background-color: rgb(164, 0, 0);\n"
"border-radius:10px;}\n"
"")
        self.stop.setObjectName("stop")
        self.outputFrame = QtWidgets.QFrame(self.secondFrame)
        self.outputFrame.setGeometry(QtCore.QRect(530, 70, 201, 281))
        self.outputFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 250), stop:1 rgba(56, 0, 161, 250));\n"
"border-radius:15px;")
        self.outputFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputFrame.setObjectName("outputFrame")
        self.outputprontframe = QtWidgets.QFrame(self.outputFrame)
        self.outputprontframe.setGeometry(QtCore.QRect(10, 20, 181, 181))
        self.outputprontframe.setStyleSheet("background-color: rgb(45, 30, 72);\n"
"border-radius:20px;")
        self.outputprontframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputprontframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputprontframe.setObjectName("outputprontframe")
        self.Summarylable = QtWidgets.QLabel(self.outputprontframe)
        self.Summarylable.setGeometry(QtCore.QRect(50, 10, 81, 21))
        self.Summarylable.setObjectName("Summarylable")
        self.hline2 = QtWidgets.QFrame(self.outputprontframe)
        self.hline2.setGeometry(QtCore.QRect(10, 50, 161, 2))
        self.hline2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline2.setObjectName("hline2")
        self.vline1 = QtWidgets.QFrame(self.outputprontframe)
        self.vline1.setGeometry(QtCore.QRect(40, 30, 2, 140))
        self.vline1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("vline1")
        self.vline2 = QtWidgets.QFrame(self.outputprontframe)
        self.vline2.setGeometry(QtCore.QRect(120, 30, 2, 140))
        self.vline2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline2.setObjectName("vline2")
        self.Srno = QtWidgets.QLabel(self.outputprontframe)
        self.Srno.setGeometry(QtCore.QRect(10, 33, 31, 16))
        self.Srno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.Srno.setObjectName("Srno")
        self.one = QtWidgets.QLabel(self.outputprontframe)
        self.one.setGeometry(QtCore.QRect(10, 60, 31, 16))
        self.one.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.one.setObjectName("one")
        self.vline3 = QtWidgets.QFrame(self.outputprontframe)
        self.vline3.setGeometry(QtCore.QRect(10, 30, 2, 140))
        self.vline3.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.vline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline3.setObjectName("vline3")
        self.hline3 = QtWidgets.QFrame(self.outputprontframe)
        self.hline3.setGeometry(QtCore.QRect(10, 170, 161, 2))
        self.hline3.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.hline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline3.setObjectName("hline3")
        self.hline1 = QtWidgets.QFrame(self.outputprontframe)
        self.hline1.setGeometry(QtCore.QRect(10, 30, 161, 2))
        self.hline1.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline1.setObjectName("hline1")
        self.measurment = QtWidgets.QLabel(self.outputprontframe)
        self.measurment.setGeometry(QtCore.QRect(40, 32, 81, 20))
        self.measurment.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.measurment.setObjectName("measurment")
        self.status = QtWidgets.QLabel(self.outputprontframe)
        self.status.setGeometry(QtCore.QRect(120, 32, 51, 20))
        self.status.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.status.setObjectName("status")
        self.Two = QtWidgets.QLabel(self.outputprontframe)
        self.Two.setGeometry(QtCore.QRect(10, 90, 31, 16))
        self.Two.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.Two.setObjectName("Two")
        self.Three = QtWidgets.QLabel(self.outputprontframe)
        self.Three.setGeometry(QtCore.QRect(10, 120, 31, 16))
        self.Three.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.Three.setObjectName("Three")
        self.Four = QtWidgets.QLabel(self.outputprontframe)
        self.Four.setGeometry(QtCore.QRect(10, 150, 31, 16))
        self.Four.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.Four.setObjectName("Four")
        self.voltage = QtWidgets.QLabel(self.outputprontframe)
        self.voltage.setGeometry(QtCore.QRect(42, 120, 61, 16))
        self.voltage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.voltage.setObjectName("voltage")
        self.Resistance = QtWidgets.QLabel(self.outputprontframe)
        self.Resistance.setGeometry(QtCore.QRect(50, 60, 61, 16))
        self.Resistance.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.Resistance.setObjectName("Resistance")
        self.inductance = QtWidgets.QLabel(self.outputprontframe)
        self.inductance.setGeometry(QtCore.QRect(46, 90, 71, 16))
        self.inductance.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.inductance.setObjectName("inductance")
        self.frequency = QtWidgets.QLabel(self.outputprontframe)
        self.frequency.setGeometry(QtCore.QRect(48, 150, 61, 16))
        self.frequency.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.223881 rgba(0, 0, 23, 0), stop:1 rgba(56, 0, 141, 0));")
        self.frequency.setObjectName("frequency")
        self.vline4 = QtWidgets.QFrame(self.outputprontframe)
        self.vline4.setGeometry(QtCore.QRect(170, 30, 2, 140))
        self.vline4.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.vline4.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline4.setObjectName("vline4")
        self.RStatus = QtWidgets.QLabel(self.outputprontframe)
        self.RStatus.setGeometry(QtCore.QRect(140, 63, 10, 10))
        self.RStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.RStatus.setObjectName("RStatus")
        self.IStatus = QtWidgets.QLabel(self.outputprontframe)
        self.IStatus.setGeometry(QtCore.QRect(140, 93, 10, 10))
        self.IStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.IStatus.setObjectName("IStatus")
        self.VStatus = QtWidgets.QLabel(self.outputprontframe)
        self.VStatus.setGeometry(QtCore.QRect(140, 123, 10, 10))
        self.VStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.VStatus.setObjectName("VStatus")
        self.FStatus = QtWidgets.QLabel(self.outputprontframe)
        self.FStatus.setGeometry(QtCore.QRect(140, 153, 10, 10))
        self.FStatus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:2px;")
        self.FStatus.setObjectName("FStatus")
        self.qrbutton = QtWidgets.QPushButton(self.outputFrame)
        self.qrbutton.setGeometry(QtCore.QRect(20, 220, 171, 25))
        self.qrbutton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(60, 231, 231);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(3, 244, 171);\n"
"}")
        self.qrbutton.setObjectName("qrbutton")
        self.backbutton = QtWidgets.QPushButton(self.secondFrame)
        self.backbutton.setGeometry(QtCore.QRect(10, 160, 51, 71))
        self.backbutton.setStyleSheet("border-image: url(:/back/back.png);\n"
"background-color: rgb(0, 0, 0);")
        self.backbutton.setText("")
        self.backbutton.setObjectName("backbutton")


#-----------------------------------------------------------thirdframe-----------------------------------------------------------------------------------#
        self.thirdFrame = QtWidgets.QFrame(self.Mainframe)
        self.thirdFrame.setGeometry(QtCore.QRect(10, 50, 781, 361))
        self.thirdFrame.setStyleSheet("border-radius:20px;")
        self.thirdFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thirdFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thirdFrame.setObjectName("thirdFrame")
        self.backbutton2 = QtWidgets.QPushButton(self.thirdFrame)
        self.backbutton2.setGeometry(QtCore.QRect(10, 140, 51, 71))
        self.backbutton2.setStyleSheet("border-image: url(:/back/back.png);\n"
"background-color: rgb(0, 0, 0);")
        self.backbutton2.setText("")
        self.backbutton2.setObjectName("backbutton2")
        self.pdfframeicon = QtWidgets.QFrame(self.thirdFrame)
        self.pdfframeicon.setGeometry(QtCore.QRect(100, 30, 281, 291))
        self.pdfframeicon.setStyleSheet("background-color: rgb(208, 187, 246);")
        self.pdfframeicon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pdfframeicon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pdfframeicon.setObjectName("pdfframeicon")
        self.pdflable = QtWidgets.QLabel(self.pdfframeicon)
        self.pdflable.setGeometry(QtCore.QRect(40, 240, 201, 31))
        self.pdflable.setObjectName("pdflable")
        self.pdfbutton = QtWidgets.QPushButton(self.pdfframeicon)
        self.pdfbutton.setGeometry(QtCore.QRect(40, 24, 201, 201))
        self.pdfbutton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pdfbutton.setStyleSheet("border-image: url(:/pdf/pdf1.png);\n"
"background-color: rgb(0, 0, 0);")
        self.pdfbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PDF/pdf.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pdfbutton.setIcon(icon)
        self.pdfbutton.setAutoDefault(False)
        self.pdfbutton.setDefault(False)
        self.pdfbutton.setFlat(False)
        self.pdfbutton.setObjectName("pdfbutton")
        self.qrframeicon = QtWidgets.QFrame(self.thirdFrame)
        self.qrframeicon.setGeometry(QtCore.QRect(410, 30, 271, 291))
        self.qrframeicon.setStyleSheet("background-color: rgb(208, 187, 246);")
        self.qrframeicon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrframeicon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrframeicon.setObjectName("qrframeicon")
        self.qrlable = QtWidgets.QLabel(self.qrframeicon)
        self.qrlable.setGeometry(QtCore.QRect(30, 240, 201, 31))
        self.qrlable.setObjectName("qrlable")
        self.qrlabel = QtWidgets.QLabel(self.qrframeicon)
        self.qrlabel.setGeometry(QtCore.QRect(10, 10, 251, 221))
        self.qrlabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-image: url(:/qrcode/qr_code.png);\n"
"border-radius:15px;")
        self.qrlabel.setText("")
        self.qrlabel.setPixmap(QtGui.QPixmap(":/qrcode/qr_code.png"))
        self.qrlabel.setScaledContents(True)
        self.qrlabel.setObjectName("qrlabel")
        self.quitbutton = QtWidgets.QPushButton(self.thirdFrame)
        self.quitbutton.setGeometry(QtCore.QRect(718, 294, 51, 51))
        self.quitbutton.setStyleSheet("border-radius:20px;\n"
"border-image: url(:/quit/quit.png);\n"
"background-color: rgb(0, 0, 0);")
        self.quitbutton.setText("")
        self.quitbutton.setObjectName("quitbutton")

#--------------------------------------initilised function-----------------------------------------------------------#
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # Function Name : retranslateUi
    # input         : MainWindow 
    # Output        : void
    # Logic         : translate all html code of  UI  elements 
    #                 1)decleard mainwindow , firstFrame
    #                 2)decleard database UI
    #                 3)decleard secondFrame 
    #                 4)decleard thirdFrame
    #                 5)hide all the frame leaving footer and firstFrame and MainFrame and initilised all buttons
    # example       : self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MPU Testing Kit"))
        self.companyname.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#fcaf3e;\">Twintech Control Systems Pvt. Ltd.</span></p></body></html>"))
        self.TCDetails.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Test Certificate Details</span></p></body></html>"))
        self.UserDetails.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">User Details</span></p></body></html>"))
        self.next.setText(_translate("MainWindow", "NEXT"))
        self.Name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name of the party :</span></p></body></html>"))
        self.Partnumberlable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Part number :</span></p></body></html>"))
        self.Partnamelable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Part name :</span></p></body></html>"))
        self.Batchnumberlable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Batch number :</span></p></body></html>"))
        self.Channlanolable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Challan number :</span></p></body></html>"))
        self.ChallanQuantlable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Challan Quantity :</span></p></body></html>"))
        self.ChallanDatelable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Challan Date :</span></p></body></html>"))
        self.TCNoLable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TC Number :</span></p></body></html>"))
        self.TCDateLable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">TC Date :</span></p></body></html>"))
        self.SupplierCodeLable.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Suppplier Code :</span></p></body></html>"))
        self.changeDatabase.setText(_translate("MainWindow", "Change Database"))
        self.contactUs.setText(_translate("MainWindow", "Contact Us"))
        self.AboutUs.setText(_translate("MainWindow", "About Us"))

#-------------------------------dataabase--------------------------------------------------------#
        self.header.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:20pt; font-weight:696; color:#ff06ea;\">Upload the EXEL file</span></p></body></html>"))
        self.selectbutton.setText(_translate("MainWindow", "Select Excel File"))
        self.savebutton.setText(_translate("MainWindow", "Save"))

#------------------------------------------secondframe---------------------------------------------------------------------#
        self.summary.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Summary</span></p></body></html>"))
        self.Voltagelable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">VOLTAGE</span></p></body></html>"))
        self.Voltageideal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal Voltage : 80 Vpp</span></p></body></html>"))
        self.voltageoutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.voltageoutput_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SingleVoltageOutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Resistancelable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">RESISTANCE</span></p></body></html>"))
        self.Resistanceideal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal Resistance: 2 ohm</span></p></body></html>"))
        self.Resistanceoutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Resistanceoutput_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SingleResistranceOutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.InductanceLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">INDUCTANCE</span></p></body></html>"))
        self.InductanceIdeal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal Inductance : 4 H</span></p></body></html>"))
        self.inductanceoutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.inductanceoutput_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SingleInductanceOutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.FrequencyLable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Frequency</span></p></body></html>"))
        self.Frequencyideal.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal Frequency: 20MHz</span></p></body></html>"))
        self.frequencyoutput.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.frequencyoutput_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.SingleFrequency.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Click to Measure"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.Summarylable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">SUMMARY</span></p></body></html>"))
        self.Srno.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#8ae234;\">Sr.no</span></p></body></html>"))
        self.one.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">1</span></p></body></html>"))
        self.measurment.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#8ae234;\">Measurment</span></p></body></html>"))
        self.status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#8ae234;\">Status</span></p></body></html>"))
        self.Two.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">2</span></p></body></html>"))
        self.Three.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">3</span></p></body></html>"))
        self.Four.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">4</span></p></body></html>"))
        self.voltage.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Voltage</span></p></body></html>"))
        self.Resistance.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Resistance</span></p></body></html>"))
        self.inductance.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Inductance</span></p></body></html>"))
        self.frequency.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">Frequency</span></p></body></html>"))
        self.RStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.IStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.VStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.FStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.qrbutton.setText(_translate("MainWindow", "Click here for PDF or QR"))


#--------------------------------------------------thirdframe--------------------------------------------------------------------------------#
        self.pdflable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Tap here to open a PDF</span></p></body></html>"))
        self.qrlable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Scan this QR to get details!!</span></p></body></html>"))

        
        self.secondFrame.hide()
        self.thirdFrame.hide()
        self.databaseFrame.hide()
        self.widget.hide()
        self.buttons_initilised()


    # Function Name : buttons_initilised
    # input         : None 
    # Output        : void
    # Logic         : all buttons_initilised in ui
    # example       : self.buttons_initilised()
    def buttons_initilised(self):
        self.settings.clicked.connect(self.toggleSettingWidget)
        self.changeDatabase.clicked.connect(self.changeTheDatabase)
        self.selectbutton.clicked.connect(self.selectFile)
        self.savebutton.clicked.connect(self.saveDataBase)
        self.next.clicked.connect(self.goToSecondFrame)
        self.backbutton.clicked.connect(self.backButtonFrame2)
        self.qrbutton.clicked.connect(self.thirdpage)
        self.backbutton2.clicked.connect(self.backButtonFrame3)
        self.quitbutton.clicked.connect(self.exit)
        self.pdfbutton.clicked.connect(self.openPdf)


    # Function Name : toggleSettingWidget
    # input         : None 
    # Output        : void
    # Logic         : toggleSettingWidget toggles the setting widget
    # example       : self.toggleSettingWidget()
    def toggleSettingWidget(self):
        if self.widget.isHidden():
            self.widget.show()
        else:
            self.widget.hide()


    # Function Name : selectFile
    # input         : None 
    # Output        : void
    # Logic         : opens file manager and allow to select only xlxs file 
    #                 and then delets the previous database file if exist and then creates an new file done by another database module     
    # example       : self.selectFile()
    def selectFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Excel File", "", "Excel Files (*.xlsx *.xls)", options=options)
        if fileName:
            print("Selected file:", fileName)
            if os.path.exists('mydatabase.db'):
                os.remove('mydatabase.db')
                self.db.__init__()
            result_message = self.db.insertDataFromExcel(fileName)
            self.savebutton.setText("Saved Successfully")
            print(result_message)


    # Function Name : saveDataBase
    # input         : None 
    # Output        : void
    # Logic         : on pressing save button hides all the frame and show firstFrame so can restart from start after change in database
    # example       : self.saveDataBase()          
    def saveDataBase(self):
        self.firstFrame.show()
        self.databaseFrame.hide()
        self.secondFrame.hide()
        self.thirdFrame.hide()
   

    # Function Name : changeTheDatabase
    # input         : None 
    # Output        : void
    # Logic         : on pressing change database in setting widget menu hides all the frame and show database frame 
    # example       : self.saveDataBase() 
    def changeTheDatabase(self):
        self.firstFrame.hide()
        self.databaseFrame.show()
        self.secondFrame.hide()
        self.thirdFrame.hide()


    # Function Name : secondFrameinit
    # input         : partNumber (PrimaryKey)
    # Output        : void
    # Logic         : accourding to partNumber sets UI for single or Dual output testing and also checks if partNumber exist in databse and ensure it is corrects if any things fail it highlights the part number and if pass it hides all frame and show only second frame main frame and footer frame
    # example       : self.secondFrameinit()   
    def secondFrameinit(self,partNumber):
        self.widget.hide()
        self.singleOrDual = (self.db.getSingleOrDualNumber(partNumber))
        if self.singleOrDual == 1:
            self.Partnumberinput.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.secondFrame.show()
            self.firstFrame.hide()
            self.Resistanceoutput.hide()
            self.Resistanceoutput_2.hide()
            self.inductanceoutput.hide()
            self.inductanceoutput_2.hide()
            self.voltageoutput.hide()
            self.voltageoutput_2.hide()
            self.frequencyoutput.hide()
            self.frequencyoutput_2.hide()
            self.SingleResistranceOutput.show()
            self.SingleInductanceOutput.show()
            self.SingleVoltageOutput.show()
            self.SingleFrequency.show()
        elif self.singleOrDual == 2:
            self.Partnumberinput.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.secondFrame.show()
            self.firstFrame.hide()
            self.Resistanceoutput.show()
            self.Resistanceoutput_2.show()
            self.inductanceoutput.show()
            self.inductanceoutput_2.show()
            self.voltageoutput.show()
            self.voltageoutput_2.show()
            self.frequencyoutput.show()
            self.frequencyoutput_2.show()
            self.SingleResistranceOutput.hide()
            self.SingleInductanceOutput.hide()
            self.SingleVoltageOutput.hide()
            self.SingleFrequency.hide()
        else:
            self.Partnumberinput.setStyleSheet("background-color: rgb(255, 255, 255);\n""border: 2px solid rgb(239, 0, 0);")
            self.secondFrame.hide()
            self.firstFrame.show()

        idealvalue = self.db.get_average_parameter_value(partNumber,'resistance')
        self.Resistanceideal.setText(f"<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal : {idealvalue} Ω</span></p></body></html>")
        idealvalue = self.db.get_average_parameter_value(partNumber,'inductance')
        self.InductanceIdeal.setText(f"<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal : {idealvalue} H</span></p></body></html>")
        idealvalue = self.db.get_average_parameter_value(partNumber,'voltage')
        self.Voltageideal.setText(f"<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal : {idealvalue} Vpp</span></p></body></html>")
        idealvalue = self.db.get_average_parameter_value(partNumber,'frequency')
        self.Frequencyideal.setText(f"<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Ideal : {idealvalue} Hz</span></p></body></html>")


    # Function Name : goToSecondFrame
    # input         : None
    # Output        : void
    # Logic         : when pressed next button calls secondFrameinit and hides setting widget if open
    # example       : self.secondFrameinit() 
    def goToSecondFrame(self):
        self.secondFrameinit(self.Partnumberinput.text())
        self.widget.hide()


    # Function Name : thirdpage
    # input         : None
    # Output        : void
    # Logic         : when pressed qrbutton closes setting widget , second frame and show thirdFrame and sets the qr code
    # example       : self.thirdpage() 
    def thirdpage(self):
        self.saveResult()
        new_image_path = f"testData/{self.tCNo}/{self.tCNo}.png"
        new_pixmap = QtGui.QPixmap(new_image_path)
        self.qrlabel.setPixmap(new_pixmap)
        self.widget.hide()
        self.thirdFrame.show()
        self.secondFrame.hide()


    # Function Name : saveResult
    # input         : None
    # Output        : void
    # Logic         : when pressed qrbutton saves the data to database and generate QR and PDF
    # example       : self.saveResult() 
    # comment       : not implemented fully
    def saveResult(self):
        
        tCNo         = self.TCNOinput.text()
        tCDate       = self.TCDateinput.text()
        supplierCode = self.SuppCodeinput.text()
        partyName    = self.Nameinput.text()
        partName     = self.partnameinput.text()
        partNumber   = self.Partnumberinput.text()
        batchNumber  = self.BatchNoinput.text()
        challanQTY   = self.ChallanQuatinput.text()
        challanNo    = self.Challannumberinput.text()
        challanDate  = self.challanDateinput.text()

        if self.singleOrDual == 1:
            calResistance     = 100
            resistanceStatus  = "pass"
            calInductance     = 100
            inductanceStatus  = "pass"
            calFrequency      = 100
            frequencyStatus   = "pass"
            calVoltage        = 100
            voltageStatus     = "pass"
            calResistance2    = "N.A"
            resistanceStatus2 = "N.A"
            calInductance2    = "N.A"
            inductanceStatus2 = "N.A"
            calFrequency2     = "N.A"
            frequencyStatus2  = "N.A"
            calVoltage2       = "N.A"
            voltageStatus2    = "N.A"
        else:
            calResistance     = 100
            resistanceStatus  = "pass"
            calInductance     = 100
            inductanceStatus  = "pass"
            calFrequency      = 100
            frequencyStatus   = "pass"
            calVoltage        = 100
            voltageStatus     = "pass"
            calResistance2    = 100
            resistanceStatus2 = "pass"
            calInductance2    = 100
            inductanceStatus2 = "pass"
            calFrequency2     = 100
            frequencyStatus2  = "pass"
            calVoltage2       = 100
            voltageStatus2    = "pass"
        
        self.db.saveResult(tCNo, tCDate, supplierCode, partyName, partName, partNumber, batchNumber,challanQTY, challanNo, challanDate, calResistance, resistanceStatus,calInductance, inductanceStatus, calFrequency, frequencyStatus,calVoltage, voltageStatus,calResistance2, resistanceStatus2,calInductance2, inductanceStatus2, calFrequency2, frequencyStatus2,calVoltage2, voltageStatus2)
        self.tCNo = tCNo
        pdfAndQr.makePdf(self.tCNo)
        pdfAndQr.makeQr(self.db.get_result_by_tcno(self.tCNo),self.tCNo)


    # Function Name : backButtonFrame2
    # input         : None
    # Output        : void
    # Logic         : when pressed back button on second page it shows first page and hide second frame and widget
    # example       : self.backButtonFrame2() 
    def backButtonFrame2(self):
        self.widget.hide()
        self.firstFrame.show()
        self.secondFrame.hide()


    # Function Name : backButtonFrame3
    # input         : None
    # Output        : void
    # Logic         : when pressed back button on third page it shows Second page and hide third frame and widget
    # example       : self.backButtonFrame3() 
    def backButtonFrame3(self):
        self.secondFrame.show()
        self.thirdFrame.hide()
        self.widget.hide()

    # Function Name : openPdf
    # input         : None
    # Output        : void
    # Logic         : when pressed opens the pdf using pdf viewer
    # example       : self.openPdf() 
    def openPdf(self):
        pdf_file = f"testData/{self.tCNo}/{self.tCNo}.pdf"  # Replace with your actual PDF file name
        # Check if the file exists
        if os.path.exists(pdf_file):
            # Open the PDF using the default PDF viewer
            webbrowser.open_new(pdf_file)
        else:
            print("Error: PDF file not found in the current directory.")

    # Function Name : exit
    # input         : None
    # Output        : void
    # Logic         : when pressed quit button closes the app 
    # example       : self.exit() 
    # comment       : close database not implemented
    def exit(self):
        if os.path.exists("src/__pycache__"):
                shutil.rmtree("src/__pycache__")
        exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
