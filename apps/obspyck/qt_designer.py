# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer.ui'
#
# Created: Mon Sep  6 23:48:01 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_qMainWindow_obsPyck(object):
    def setupUi(self, qMainWindow_obsPyck):
        qMainWindow_obsPyck.setObjectName("qMainWindow_obsPyck")
        qMainWindow_obsPyck.resize(1782, 756)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(qMainWindow_obsPyck.sizePolicy().hasHeightForWidth())
        qMainWindow_obsPyck.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("obspyck.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        qMainWindow_obsPyck.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(qMainWindow_obsPyck)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(8)
        self.splitter.setObjectName("splitter")
        self.splitter1 = QtGui.QSplitter(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter1.sizePolicy().hasHeightForWidth())
        self.splitter1.setSizePolicy(sizePolicy)
        self.splitter1.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter1.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter1.setOrientation(QtCore.Qt.Horizontal)
        self.splitter1.setHandleWidth(8)
        self.splitter1.setObjectName("splitter1")
        self.layoutWidgetxx = QtGui.QWidget(self.splitter1)
        self.layoutWidgetxx.setObjectName("layoutWidgetxx")
        self.leftVerticalLayout = QtGui.QVBoxLayout(self.layoutWidgetxx)
        self.leftVerticalLayout.setSpacing(1)
        self.leftVerticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.leftVerticalLayout.setMargin(1)
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.qToolButton_clearAll = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_clearAll.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_clearAll.setFont(font)
        self.qToolButton_clearAll.setStyleSheet("None")
        self.qToolButton_clearAll.setCheckable(False)
        self.qToolButton_clearAll.setObjectName("qToolButton_clearAll")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearAll)
        self.qToolButton_clearOrigMag = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_clearOrigMag.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearOrigMag.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_clearOrigMag.setFont(font)
        self.qToolButton_clearOrigMag.setObjectName("qToolButton_clearOrigMag")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearOrigMag)
        self.qToolButton_clearFocMec = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_clearFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_clearFocMec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_clearFocMec.setFont(font)
        self.qToolButton_clearFocMec.setObjectName("qToolButton_clearFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_clearFocMec)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem)
        self.qToolButton_doHyp2000 = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_doHyp2000.sizePolicy().hasHeightForWidth())
        self.qToolButton_doHyp2000.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_doHyp2000.setFont(font)
        self.qToolButton_doHyp2000.setObjectName("qToolButton_doHyp2000")
        self.leftVerticalLayout.addWidget(self.qToolButton_doHyp2000)
        self.qToolButton_do3dloc = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_do3dloc.sizePolicy().hasHeightForWidth())
        self.qToolButton_do3dloc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_do3dloc.setFont(font)
        self.qToolButton_do3dloc.setObjectName("qToolButton_do3dloc")
        self.leftVerticalLayout.addWidget(self.qToolButton_do3dloc)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.qToolButton_doNlloc = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_doNlloc.sizePolicy().hasHeightForWidth())
        self.qToolButton_doNlloc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_doNlloc.setFont(font)
        self.qToolButton_doNlloc.setObjectName("qToolButton_doNlloc")
        self.horizontalLayout_3.addWidget(self.qToolButton_doNlloc)
        self.qComboBox_nllocModel = QtGui.QComboBox(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qComboBox_nllocModel.sizePolicy().hasHeightForWidth())
        self.qComboBox_nllocModel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.qComboBox_nllocModel.setFont(font)
        self.qComboBox_nllocModel.setStyleSheet("None")
        self.qComboBox_nllocModel.setObjectName("qComboBox_nllocModel")
        self.qComboBox_nllocModel.addItem("")
        self.qComboBox_nllocModel.addItem("")
        self.qComboBox_nllocModel.addItem("")
        self.horizontalLayout_3.addWidget(self.qComboBox_nllocModel)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_3)
        self.qToolButton_calcMag = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_calcMag.sizePolicy().hasHeightForWidth())
        self.qToolButton_calcMag.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_calcMag.setFont(font)
        self.qToolButton_calcMag.setObjectName("qToolButton_calcMag")
        self.leftVerticalLayout.addWidget(self.qToolButton_calcMag)
        self.qToolButton_doFocMec = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_doFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_doFocMec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_doFocMec.setFont(font)
        self.qToolButton_doFocMec.setObjectName("qToolButton_doFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_doFocMec)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem1)
        self.qToolButton_showMap = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_showMap.sizePolicy().hasHeightForWidth())
        self.qToolButton_showMap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_showMap.setFont(font)
        self.qToolButton_showMap.setCheckable(True)
        self.qToolButton_showMap.setObjectName("qToolButton_showMap")
        self.leftVerticalLayout.addWidget(self.qToolButton_showMap)
        self.qToolButton_showFocMec = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_showFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_showFocMec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_showFocMec.setFont(font)
        self.qToolButton_showFocMec.setCheckable(True)
        self.qToolButton_showFocMec.setObjectName("qToolButton_showFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_showFocMec)
        self.qToolButton_nextFocMec = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_nextFocMec.sizePolicy().hasHeightForWidth())
        self.qToolButton_nextFocMec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_nextFocMec.setFont(font)
        self.qToolButton_nextFocMec.setObjectName("qToolButton_nextFocMec")
        self.leftVerticalLayout.addWidget(self.qToolButton_nextFocMec)
        self.qToolButton_showWadati = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_showWadati.sizePolicy().hasHeightForWidth())
        self.qToolButton_showWadati.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_showWadati.setFont(font)
        self.qToolButton_showWadati.setCheckable(True)
        self.qToolButton_showWadati.setObjectName("qToolButton_showWadati")
        self.leftVerticalLayout.addWidget(self.qToolButton_showWadati)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem2)
        self.qToolButton_getNextEvent = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_getNextEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_getNextEvent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_getNextEvent.setFont(font)
        self.qToolButton_getNextEvent.setObjectName("qToolButton_getNextEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_getNextEvent)
        self.qToolButton_updateEventList = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_updateEventList.sizePolicy().hasHeightForWidth())
        self.qToolButton_updateEventList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_updateEventList.setFont(font)
        self.qToolButton_updateEventList.setObjectName("qToolButton_updateEventList")
        self.leftVerticalLayout.addWidget(self.qToolButton_updateEventList)
        self.qToolButton_sendEvent = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_sendEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_sendEvent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_sendEvent.setFont(font)
        self.qToolButton_sendEvent.setObjectName("qToolButton_sendEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_sendEvent)
        self.qCheckBox_publishEvent = QtGui.QCheckBox(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qCheckBox_publishEvent.sizePolicy().hasHeightForWidth())
        self.qCheckBox_publishEvent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qCheckBox_publishEvent.setFont(font)
        self.qCheckBox_publishEvent.setObjectName("qCheckBox_publishEvent")
        self.leftVerticalLayout.addWidget(self.qCheckBox_publishEvent)
        self.qToolButton_deleteEvent = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_deleteEvent.sizePolicy().hasHeightForWidth())
        self.qToolButton_deleteEvent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_deleteEvent.setFont(font)
        self.qToolButton_deleteEvent.setObjectName("qToolButton_deleteEvent")
        self.leftVerticalLayout.addWidget(self.qToolButton_deleteEvent)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.qCheckBox_sysop = QtGui.QCheckBox(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qCheckBox_sysop.sizePolicy().hasHeightForWidth())
        self.qCheckBox_sysop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qCheckBox_sysop.setFont(font)
        self.qCheckBox_sysop.setObjectName("qCheckBox_sysop")
        self.horizontalLayout_4.addWidget(self.qCheckBox_sysop)
        self.qLineEdit_sysopPassword = QtGui.QLineEdit(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qLineEdit_sysopPassword.sizePolicy().hasHeightForWidth())
        self.qLineEdit_sysopPassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qLineEdit_sysopPassword.setFont(font)
        self.qLineEdit_sysopPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.qLineEdit_sysopPassword.setObjectName("qLineEdit_sysopPassword")
        self.horizontalLayout_4.addWidget(self.qLineEdit_sysopPassword)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.qToolButton_debug = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_debug.sizePolicy().hasHeightForWidth())
        self.qToolButton_debug.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_debug.setFont(font)
        self.qToolButton_debug.setObjectName("qToolButton_debug")
        self.horizontalLayout_5.addWidget(self.qToolButton_debug)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.leftVerticalLayout.addItem(spacerItem4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.qToolButton_previousStream = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_previousStream.sizePolicy().hasHeightForWidth())
        self.qToolButton_previousStream.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_previousStream.setFont(font)
        self.qToolButton_previousStream.setObjectName("qToolButton_previousStream")
        self.horizontalLayout_6.addWidget(self.qToolButton_previousStream)
        self.VerticalLayout = QtGui.QVBoxLayout()
        self.VerticalLayout.setSpacing(6)
        self.VerticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.VerticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.qLabel_streamNumber = QtGui.QLabel(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qLabel_streamNumber.sizePolicy().hasHeightForWidth())
        self.qLabel_streamNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.qLabel_streamNumber.setFont(font)
        self.qLabel_streamNumber.setStyleSheet("None")
        self.qLabel_streamNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.qLabel_streamNumber.setObjectName("qLabel_streamNumber")
        self.VerticalLayout.addWidget(self.qLabel_streamNumber)
        self.qComboBox_streamName = QtGui.QComboBox(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qComboBox_streamName.sizePolicy().hasHeightForWidth())
        self.qComboBox_streamName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.qComboBox_streamName.setFont(font)
        self.qComboBox_streamName.setStyleSheet("None")
        self.qComboBox_streamName.setObjectName("qComboBox_streamName")
        self.VerticalLayout.addWidget(self.qComboBox_streamName)
        self.horizontalLayout_6.addLayout(self.VerticalLayout)
        self.qToolButton_nextStream = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_nextStream.sizePolicy().hasHeightForWidth())
        self.qToolButton_nextStream.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_nextStream.setFont(font)
        self.qToolButton_nextStream.setObjectName("qToolButton_nextStream")
        self.horizontalLayout_6.addWidget(self.qToolButton_nextStream)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.qToolButton_overview = QtGui.QToolButton(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qToolButton_overview.sizePolicy().hasHeightForWidth())
        self.qToolButton_overview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qToolButton_overview.setFont(font)
        self.qToolButton_overview.setCheckable(True)
        self.qToolButton_overview.setObjectName("qToolButton_overview")
        self.verticalLayout_3.addWidget(self.qToolButton_overview)
        self.qComboBox_phaseType = QtGui.QComboBox(self.layoutWidgetxx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qComboBox_phaseType.sizePolicy().hasHeightForWidth())
        self.qComboBox_phaseType.setSizePolicy(sizePolicy)
        self.qComboBox_phaseType.setObjectName("qComboBox_phaseType")
        self.verticalLayout_3.addWidget(self.qComboBox_phaseType)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.leftVerticalLayout.addLayout(self.horizontalLayout_6)
        self.layoutWidgetx = QtGui.QWidget(self.splitter1)
        self.layoutWidgetx.setObjectName("layoutWidgetx")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidgetx)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qMplCanvas = QMplCanvas(self.layoutWidgetx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.qMplCanvas.sizePolicy().hasHeightForWidth())
        self.qMplCanvas.setSizePolicy(sizePolicy)
        self.qMplCanvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.qMplCanvas.setObjectName("qMplCanvas")
        self.verticalLayout_2.addWidget(self.qMplCanvas)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.qToolButton_filter = QtGui.QToolButton(self.layoutWidgetx)
        self.qToolButton_filter.setCheckable(True)
        self.qToolButton_filter.setObjectName("qToolButton_filter")
        self.horizontalLayout_2.addWidget(self.qToolButton_filter)
        self.qComboBox_filterType = QtGui.QComboBox(self.layoutWidgetx)
        self.qComboBox_filterType.setObjectName("qComboBox_filterType")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.qComboBox_filterType.addItem("")
        self.horizontalLayout_2.addWidget(self.qComboBox_filterType)
        self.qCheckBox_zerophase = QtGui.QCheckBox(self.layoutWidgetx)
        self.qCheckBox_zerophase.setObjectName("qCheckBox_zerophase")
        self.horizontalLayout_2.addWidget(self.qCheckBox_zerophase)
        self.qLabel_highpass = QtGui.QLabel(self.layoutWidgetx)
        self.qLabel_highpass.setObjectName("qLabel_highpass")
        self.horizontalLayout_2.addWidget(self.qLabel_highpass)
        self.qDoubleSpinBox_highpass = QtGui.QDoubleSpinBox(self.layoutWidgetx)
        self.qDoubleSpinBox_highpass.setObjectName("qDoubleSpinBox_highpass")
        self.horizontalLayout_2.addWidget(self.qDoubleSpinBox_highpass)
        self.qLabel_lowpass = QtGui.QLabel(self.layoutWidgetx)
        self.qLabel_lowpass.setObjectName("qLabel_lowpass")
        self.horizontalLayout_2.addWidget(self.qLabel_lowpass)
        self.qDoubleSpinBox_lowpass = QtGui.QDoubleSpinBox(self.layoutWidgetx)
        self.qDoubleSpinBox_lowpass.setObjectName("qDoubleSpinBox_lowpass")
        self.horizontalLayout_2.addWidget(self.qDoubleSpinBox_lowpass)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.qToolButton_spectrogram = QtGui.QToolButton(self.layoutWidgetx)
        self.qToolButton_spectrogram.setCheckable(True)
        self.qToolButton_spectrogram.setObjectName("qToolButton_spectrogram")
        self.horizontalLayout_2.addWidget(self.qToolButton_spectrogram)
        self.qCheckBox_spectrogramLog = QtGui.QCheckBox(self.layoutWidgetx)
        self.qCheckBox_spectrogramLog.setObjectName("qCheckBox_spectrogramLog")
        self.horizontalLayout_2.addWidget(self.qCheckBox_spectrogramLog)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qPlainTextEdit_stdout = QtGui.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qPlainTextEdit_stdout.sizePolicy().hasHeightForWidth())
        self.qPlainTextEdit_stdout.setSizePolicy(sizePolicy)
        self.qPlainTextEdit_stdout.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        self.qPlainTextEdit_stdout.setFont(font)
        self.qPlainTextEdit_stdout.setAcceptDrops(False)
        self.qPlainTextEdit_stdout.setUndoRedoEnabled(False)
        self.qPlainTextEdit_stdout.setReadOnly(True)
        self.qPlainTextEdit_stdout.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.qPlainTextEdit_stdout.setObjectName("qPlainTextEdit_stdout")
        self.horizontalLayout.addWidget(self.qPlainTextEdit_stdout)
        self.qPlainTextEdit_stderr = QtGui.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qPlainTextEdit_stderr.sizePolicy().hasHeightForWidth())
        self.qPlainTextEdit_stderr.setSizePolicy(sizePolicy)
        self.qPlainTextEdit_stderr.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(8)
        self.qPlainTextEdit_stderr.setFont(font)
        self.qPlainTextEdit_stderr.setAcceptDrops(False)
        self.qPlainTextEdit_stderr.setUndoRedoEnabled(False)
        self.qPlainTextEdit_stderr.setReadOnly(True)
        self.qPlainTextEdit_stderr.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.qPlainTextEdit_stderr.setObjectName("qPlainTextEdit_stderr")
        self.horizontalLayout.addWidget(self.qPlainTextEdit_stderr)
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        qMainWindow_obsPyck.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(qMainWindow_obsPyck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1782, 22))
        self.menubar.setObjectName("menubar")
        qMainWindow_obsPyck.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(qMainWindow_obsPyck)
        self.statusbar.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        qMainWindow_obsPyck.setStatusBar(self.statusbar)

        self.retranslateUi(qMainWindow_obsPyck)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow_obsPyck)

    def retranslateUi(self, qMainWindow_obsPyck):
        qMainWindow_obsPyck.setWindowTitle(QtGui.QApplication.translate("qMainWindow_obsPyck", "ObsPyck", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_clearAll.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_clearOrigMag.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "clear Orig&&Mag", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_clearFocMec.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "clear FocMec", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_doHyp2000.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "do hyp2000", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_do3dloc.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "do 3dloc", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_doNlloc.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "do NLLoc", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_nllocModel.setItemText(0, QtGui.QApplication.translate("qMainWindow_obsPyck", "BY", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_nllocModel.setItemText(1, QtGui.QApplication.translate("qMainWindow_obsPyck", "RH", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_nllocModel.setItemText(2, QtGui.QApplication.translate("qMainWindow_obsPyck", "UH", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_calcMag.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "calc Mag", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_doFocMec.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "do focmec", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_showMap.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "show Map", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_showFocMec.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "show FocMec", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_nextFocMec.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "next FocMec", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_showWadati.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "show Wadati", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_getNextEvent.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "get Next Event", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_updateEventList.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "update Event List", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_sendEvent.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "send Event", None, QtGui.QApplication.UnicodeUTF8))
        self.qCheckBox_publishEvent.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "publish Event", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_deleteEvent.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "delete Event", None, QtGui.QApplication.UnicodeUTF8))
        self.qCheckBox_sysop.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "sysop", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_debug.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "debug", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_previousStream.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.qLabel_streamNumber.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<  html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, l  i { white-space: pre-wrap; }\n"
"<  /style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<  p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00/00</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_nextStream.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_overview.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_filter.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_filterType.setItemText(0, QtGui.QApplication.translate("qMainWindow_obsPyck", "Bandpass", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_filterType.setItemText(1, QtGui.QApplication.translate("qMainWindow_obsPyck", "Bandstop", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_filterType.setItemText(2, QtGui.QApplication.translate("qMainWindow_obsPyck", "Lowpass", None, QtGui.QApplication.UnicodeUTF8))
        self.qComboBox_filterType.setItemText(3, QtGui.QApplication.translate("qMainWindow_obsPyck", "Highpass", None, QtGui.QApplication.UnicodeUTF8))
        self.qCheckBox_zerophase.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Zero Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.qLabel_highpass.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Highpass", None, QtGui.QApplication.UnicodeUTF8))
        self.qLabel_lowpass.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Lowpass", None, QtGui.QApplication.UnicodeUTF8))
        self.qToolButton_spectrogram.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "Spectrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.qCheckBox_spectrogramLog.setText(QtGui.QApplication.translate("qMainWindow_obsPyck", "log", None, QtGui.QApplication.UnicodeUTF8))

from util import QMplCanvas
