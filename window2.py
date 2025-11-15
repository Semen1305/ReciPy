from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(1059, 725)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("картинки//icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow1.setWindowIcon(icon)
        MainWindow1.setStyleSheet("color: black;\n"
                                  "font-weight: bold;\n"
                                  "font-size: 16pt;\n"
                                  "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("color: black;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 16pt;\n"
                                 "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setStyleSheet("background-color: rgb(230, 230, 255);\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("color: black;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 16pt;\n"
                                   "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.ingr = QtWidgets.QListWidget(parent=self.centralwidget)
        self.ingr.setStyleSheet("background-color: rgb(255, 226, 246);\n"
                                "")
        self.ingr.setObjectName("ingr")
        self.verticalLayout_2.addWidget(self.ingr)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setStyleSheet("color: black;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 16pt;\n"
                                   "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_3.setStyleSheet("background-color: rgb(255, 227, 224);\n"
                                        "")
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_3.addWidget(self.listWidget_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 36))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Рецепты"))
        self.label.setText(_translate("MainWindow1", "Название рецептов"))
        self.label_2.setText(_translate("MainWindow1", "Ингредиенты"))
        self.label_3.setText(_translate("MainWindow1", "Шаги приготовления"))
