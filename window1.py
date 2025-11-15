import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ReciPy(object):
    def setupUi(self, ReciPy):
        ReciPy.setObjectName("ReciPy")
        ReciPy.resize(1558, 824)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{os.getcwd()}//image//icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ReciPy.setWindowIcon(icon)
        ReciPy.setStyleSheet("color:black;\n"
                             "font-weight: bold;\n"
                             "font-size: 32pt;\n"
                             "font-family: \"Comic Sans MS\", cursive, sans-serif;\n"
                             "QPushButton {\n"
                             "    border-style: solid;\n"
                             "}")
        self.centralwidget = QtWidgets.QWidget(parent=ReciPy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setStyleSheet("color:rgb(0, 0, 0);\n"
                                "font-weight: bold;\n"
                                "font-size: 16pt;\n"
                                "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.name.setObjectName("name")
        self.horizontalLayout_3.addWidget(self.name)
        self.found = QtWidgets.QPushButton(parent=self.centralwidget)
        self.found.setStyleSheet("color:rgb(0, 0, 0);\n"
                                 "font-weight: bold;\n"
                                 "font-size: 16pt;\n"
                                 "font-family: \"Comic Sans MS\", cursive, sans-serif;")
        self.found.setObjectName("found")
        self.horizontalLayout_3.addWidget(self.found)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.supi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.supi.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supi.sizePolicy().hasHeightForWidth())
        self.supi.setSizePolicy(sizePolicy)
        self.supi.setAutoFillBackground(False)
        self.supi.setStyleSheet(f"background-image: url(image//sup.png);\n"
                                "background-repeat: no-repeat;\n"
                                "background-position: center;\n"
                                "background-origin: content;\n"
                                "background-clip: padding;")
        self.supi.setObjectName("supi")
        self.horizontalLayout.addWidget(self.supi)
        self.vtoroe = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vtoroe.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vtoroe.sizePolicy().hasHeightForWidth())
        self.vtoroe.setSizePolicy(sizePolicy)
        self.vtoroe.setAutoFillBackground(False)
        self.vtoroe.setStyleSheet("background-image: url(image//vtoroe.png);\n"
                                  "background-repeat: no-repeat;\n"
                                  "background-position: center;\n"
                                  "background-origin: content;\n"
                                  "background-clip: padding;")
        self.vtoroe.setObjectName("vtoroe")
        self.horizontalLayout.addWidget(self.vtoroe)
        self.deserti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deserti.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deserti.sizePolicy().hasHeightForWidth())
        self.deserti.setSizePolicy(sizePolicy)
        self.deserti.setStyleSheet("background-image: url(image//desert.png);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-position: center;\n"
                                   "background-origin: content;\n"
                                   "background-clip: padding;")
        self.deserti.setObjectName("deserti")
        self.horizontalLayout.addWidget(self.deserti)
        self.vipechka = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vipechka.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vipechka.sizePolicy().hasHeightForWidth())
        self.vipechka.setSizePolicy(sizePolicy)
        self.vipechka.setStyleSheet("background-image: url(image//vipechka.png);\n"
                                    "background-repeat: no-repeat;\n"
                                    "background-position: center;\n"
                                    "background-origin: content;\n"
                                    "background-clip: padding;")
        self.vipechka.setObjectName("vipechka")
        self.horizontalLayout.addWidget(self.vipechka)
        self.napitki = QtWidgets.QPushButton(parent=self.centralwidget)
        self.napitki.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.napitki.sizePolicy().hasHeightForWidth())
        self.napitki.setSizePolicy(sizePolicy)
        self.napitki.setStyleSheet("background-image: url(image//napitok.png);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-position: center;\n"
                                   "background-origin: content;\n"
                                   "background-clip: padding;")
        self.napitki.setObjectName("napitki")
        self.horizontalLayout.addWidget(self.napitki)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zagotovki = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zagotovki.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zagotovki.sizePolicy().hasHeightForWidth())
        self.zagotovki.setSizePolicy(sizePolicy)
        self.zagotovki.setStyleSheet("background-image: url(image//zagotovki.png);\n"
                                     "background-repeat: no-repeat;\n"
                                     "background-position: center;\n"
                                     "background-origin: content;\n"
                                     "background-clip: padding;")
        self.zagotovki.setObjectName("zagotovki")
        self.horizontalLayout_2.addWidget(self.zagotovki)
        self.salat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.salat.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.salat.sizePolicy().hasHeightForWidth())
        self.salat.setSizePolicy(sizePolicy)
        self.salat.setStyleSheet("background-image: url(image//salad.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;\n"
                                 "background-origin: content;\n"
                                 "background-clip: padding;")
        self.salat.setObjectName("salat")
        self.horizontalLayout_2.addWidget(self.salat)
        self.zakuski = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zakuski.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zakuski.sizePolicy().hasHeightForWidth())
        self.zakuski.setSizePolicy(sizePolicy)
        self.zakuski.setStyleSheet("background-image: url(image//zakuski.png);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-position: center;\n"
                                   "background-origin: content;\n"
                                   "background-clip: padding;")
        self.zakuski.setObjectName("zakuski")
        self.horizontalLayout_2.addWidget(self.zakuski)
        self.testo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.testo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testo.sizePolicy().hasHeightForWidth())
        self.testo.setSizePolicy(sizePolicy)
        self.testo.setStyleSheet("background-image: url(image//testo.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;\n"
                                 "background-origin: content;\n"
                                 "background-clip: padding;")
        self.testo.setObjectName("testo")
        self.horizontalLayout_2.addWidget(self.testo)
        self.sousi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sousi.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sousi.sizePolicy().hasHeightForWidth())
        self.sousi.setSizePolicy(sizePolicy)
        self.sousi.setStyleSheet("background-image: url(image//sousi.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;\n"
                                 "background-origin: content;\n"
                                 "background-clip: padding;")
        self.sousi.setObjectName("sousi")
        self.horizontalLayout_2.addWidget(self.sousi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        ReciPy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ReciPy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1558, 66))
        self.menubar.setObjectName("menubar")
        ReciPy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ReciPy)
        self.statusbar.setObjectName("statusbar")
        ReciPy.setStatusBar(self.statusbar)
        self.retranslateUi(ReciPy)
        QtCore.QMetaObject.connectSlotsByName(ReciPy)

    def retranslateUi(self, ReciPy):
        _translate = QtCore.QCoreApplication.translate
        ReciPy.setWindowTitle(_translate("ReciPy", "ReciPy"))
        self.found.setText(_translate("ReciPy", "Найти по названию"))
        self.supi.setText(_translate("ReciPy", "Супы"))
        self.vtoroe.setText(_translate("ReciPy", "Вторые блюда"))
        self.deserti.setText(_translate("ReciPy", "Десерты"))
        self.vipechka.setText(_translate("ReciPy", "Выпечка"))
        self.napitki.setText(_translate("ReciPy", "Напитки"))
        self.zagotovki.setText(_translate("ReciPy", "Заготовки"))
        self.salat.setText(_translate("ReciPy", "Салаты"))
        self.zakuski.setText(_translate("ReciPy", "Закуски"))
        self.testo.setText(_translate("ReciPy", "Тесто"))
        self.sousi.setText(_translate("ReciPy", "Соусы"))
