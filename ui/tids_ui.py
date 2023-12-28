# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tids.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(870, 630))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icn-replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ogretici = QtWidgets.QWidget()
        self.tab_ogretici.setObjectName("tab_ogretici")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_ogretici)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_ogretici_kelime_ara = QtWidgets.QLineEdit(self.tab_ogretici)
        self.le_ogretici_kelime_ara.setObjectName("le_ogretici_kelime_ara")
        self.verticalLayout.addWidget(self.le_ogretici_kelime_ara)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.lw_ogretici_kelime_listesi = QtWidgets.QListWidget(self.tab_ogretici)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lw_ogretici_kelime_listesi.setFont(font)
        self.lw_ogretici_kelime_listesi.setObjectName("lw_ogretici_kelime_listesi")
        self.verticalLayout.addWidget(self.lw_ogretici_kelime_listesi)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lbl_ogretici_secili_kelime_img = QtWidgets.QLabel(self.tab_ogretici)
        self.lbl_ogretici_secili_kelime_img.setObjectName("lbl_ogretici_secili_kelime_img")
        self.horizontalLayout.addWidget(self.lbl_ogretici_secili_kelime_img)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.txt_ogretici_secili_kelime_anlam = QtWidgets.QPlainTextEdit(self.tab_ogretici)
        self.txt_ogretici_secili_kelime_anlam.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txt_ogretici_secili_kelime_anlam.setFont(font)
        self.txt_ogretici_secili_kelime_anlam.setReadOnly(True)
        self.txt_ogretici_secili_kelime_anlam.setObjectName("txt_ogretici_secili_kelime_anlam")
        self.verticalLayout_2.addWidget(self.txt_ogretici_secili_kelime_anlam)
        self.verticalLayout_2.setStretch(0, 1)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 2, 2)
        spacerItem5 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_ogretici, "")
        self.tab_cevirici = QtWidgets.QWidget()
        self.tab_cevirici.setObjectName("tab_cevirici")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_cevirici)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txt_cevirici_cumle = QtWidgets.QPlainTextEdit(self.tab_cevirici)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_cevirici_cumle.setFont(font)
        self.txt_cevirici_cumle.setObjectName("txt_cevirici_cumle")
        self.verticalLayout_3.addWidget(self.txt_cevirici_cumle)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cevirici_cevir = QtWidgets.QPushButton(self.tab_cevirici)
        self.btn_cevirici_cevir.setObjectName("btn_cevirici_cevir")
        self.horizontalLayout_2.addWidget(self.btn_cevirici_cevir)
        spacerItem10 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.btn_cevirici_konus = QtWidgets.QPushButton(self.tab_cevirici)
        self.btn_cevirici_konus.setIconSize(QtCore.QSize(30, 22))
        self.btn_cevirici_konus.setObjectName("btn_cevirici_konus")
        self.horizontalLayout_2.addWidget(self.btn_cevirici_konus)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.lbl_cevirici_cumle_img = QtWidgets.QLabel(self.tab_cevirici)
        self.lbl_cevirici_cumle_img.setObjectName("lbl_cevirici_cumle_img")
        self.horizontalLayout_3.addWidget(self.lbl_cevirici_cumle_img)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 1, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_3.addItem(spacerItem13, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_cevirici, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 35))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Türk İşaret Dili Sözlüğü"))
        self.le_ogretici_kelime_ara.setPlaceholderText(_translate("MainWindow", "Bir kelime arayın"))
        self.lbl_ogretici_secili_kelime_img.setText(_translate("MainWindow", "TextLabel"))
        self.txt_ogretici_secili_kelime_anlam.setPlaceholderText(_translate("MainWindow", "Anlamı burada gösterilir."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ogretici), _translate("MainWindow", "Öğretici"))
        self.btn_cevirici_cevir.setText(_translate("MainWindow", "YAZIYI ÇEVİR"))
        self.btn_cevirici_konus.setText(_translate("MainWindow", "DİKTE"))
        self.lbl_cevirici_cumle_img.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cevirici), _translate("MainWindow", "Çevirici"))
import ui.imgs_rc
