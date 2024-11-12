# Form implementation generated from reading ui file 'ui/imagenes_window.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(934, 618)
        Form.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 0 10px")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setStyleSheet("border:none;\n"
"margin-top:10px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../resources/images/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.general = QtWidgets.QPushButton(parent=self.frame)
        self.general.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.general.setObjectName("general")
        self.verticalLayout.addWidget(self.general)
        self.imagenes = QtWidgets.QPushButton(parent=self.frame)
        self.imagenes.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.imagenes.setObjectName("imagenes")
        self.verticalLayout.addWidget(self.imagenes)
        self.log = QtWidgets.QPushButton(parent=self.frame)
        self.log.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.informes = QtWidgets.QPushButton(parent=self.frame)
        self.informes.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.informes.setObjectName("informes")
        self.verticalLayout.addWidget(self.informes)
        self.line_2 = QtWidgets.QFrame(parent=self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.desconectarse = QtWidgets.QPushButton(parent=self.frame)
        self.desconectarse.setStyleSheet("border:none;\n"
"padding:5px 0;\n"
"color: rgb(0, 0, 0);")
        self.desconectarse.setObjectName("desconectarse")
        self.verticalLayout.addWidget(self.desconectarse)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 5, 10, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setStyleSheet("border:none;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_6.setStyleSheet("border:none;\n"
"background:transparent;")
        self.pushButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../resources/svg/bell-solid-black.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.line_3 = QtWidgets.QFrame(parent=self.frame_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.widget = QtWidgets.QWidget(parent=self.frame_3)
        self.widget.setStyleSheet("border:none;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setStyleSheet("color: rgb(113, 113, 113);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"padding:0;\n"
"padding-left:10px")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #DBDADE;\n"
"padding: 7px 0;\n"
"border-radius:5px;\n"
"padding-left:5px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.cargue = QtWidgets.QPushButton(parent=self.frame_5)
        self.cargue.setStyleSheet("background-color: rgb(94, 90, 219);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"padding:10px;\n"
"border-radius:5px;")
        self.cargue.setObjectName("cargue")
        self.horizontalLayout_3.addWidget(self.cargue)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView = QtWidgets.QTableView(parent=self.frame_6)
        self.tableView.setStyleSheet("color:#000000")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_5.addWidget(self.tableView)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 17)
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestion de imagenes"))
        self.general.setText(_translate("Form", "General"))
        self.imagenes.setText(_translate("Form", "Gestion de imagenes"))
        self.log.setText(_translate("Form", "Logs de aplicacion"))
        self.informes.setText(_translate("Form", "Informes generados"))
        self.desconectarse.setText(_translate("Form", "Desconectarse"))
        self.label_3.setText(_translate("Form", "GESTION DE IMAGENES"))
        self.label_5.setText(_translate("Form", "Superuser"))
        self.label_4.setText(_translate("Form", "Administrador"))
        self.label_2.setText(_translate("Form", "Está página permite el cargue de imágenes de vehículos a la base de datos."))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar"))
        self.cargue.setText(_translate("Form", "Nuevo cargue"))
