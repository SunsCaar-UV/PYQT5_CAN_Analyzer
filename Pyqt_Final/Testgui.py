# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2084, 869)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.receivetable = QtWidgets.QTableWidget(self.centralwidget)
        self.receivetable.setGeometry(QtCore.QRect(460, 0, 1311, 521))
        self.receivetable.setAlternatingRowColors(True)
        self.receivetable.setObjectName("receivetable")
        self.receivetable.setColumnCount(0)
        self.receivetable.setRowCount(0)
        self.transmit = QtWidgets.QPushButton(self.centralwidget)
        self.transmit.setGeometry(QtCore.QRect(530, 660, 93, 28))
        self.transmit.setTabletTracking(False)
        self.transmit.setAutoFillBackground(False)
        self.transmit.setObjectName("transmit")
        self.transmittable = QtWidgets.QTableWidget(self.centralwidget)
        self.transmittable.setGeometry(QtCore.QRect(460, 530, 1311, 221))
        self.transmittable.setObjectName("transmittable")
        self.transmittable.setColumnCount(0)
        self.transmittable.setRowCount(0)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 0, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 431, 521))
        self.listWidget.setObjectName("listWidget")
        self.logfilename = QtWidgets.QTextEdit(self.centralwidget)
        self.logfilename.setGeometry(QtCore.QRect(110, 120, 181, 31))
        self.logfilename.setObjectName("logfilename")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 130, 55, 16))
        self.label.setObjectName("label")
        self.start_log = QtWidgets.QPushButton(self.centralwidget)
        self.start_log.setGeometry(QtCore.QRect(60, 190, 93, 28))
        self.start_log.setObjectName("start_log")
        self.stop_log = QtWidgets.QPushButton(self.centralwidget)
        self.stop_log.setGeometry(QtCore.QRect(220, 190, 93, 28))
        self.stop_log.setObjectName("stop_log")
        self.logstatus = QtWidgets.QLabel(self.centralwidget)
        self.logstatus.setGeometry(QtCore.QRect(160, 240, 55, 16))
        self.logstatus.setObjectName("logstatus")
        self.listWidget.raise_()
        self.transmittable.raise_()
        self.receivetable.raise_()
        self.transmit.raise_()
        self.line.raise_()
        self.logfilename.raise_()
        self.label.raise_()
        self.start_log.raise_()
        self.stop_log.raise_()
        self.logstatus.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2084, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionconnect = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("Green")
        self.actionconnect.setIcon(icon)
        self.actionconnect.setObjectName("actionconnect")
        self.actiondisconnect = QtWidgets.QAction(MainWindow)
        self.actiondisconnect.setObjectName("actiondisconnect")
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionconnect)
        self.toolBar.addAction(self.actiondisconnect)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.transmit.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Filename: "))
        self.start_log.setText(_translate("MainWindow", "Start Log"))
        self.stop_log.setText(_translate("MainWindow", "Stop Log"))
        self.logstatus.setText(_translate("MainWindow", "Log Statuss"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionconnect.setText(_translate("MainWindow", "Connect"))
        self.actionconnect.setToolTip(_translate("MainWindow", "Button"))
        self.actiondisconnect.setText(_translate("MainWindow", "Disconnect"))