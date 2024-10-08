# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1315, 779)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QPushButton {\n"
"border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"min-width: 80px;\n"
"}\n"
"\n"
"QComboBox {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 29, 795, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_widgets = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_widgets.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_widgets.setObjectName("verticalLayout_widgets")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_pushButton.sizePolicy().hasHeightForWidth())
        self.browse_pushButton.setSizePolicy(sizePolicy)
        self.browse_pushButton.setMinimumSize(QtCore.QSize(84, 32))
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.horizontalLayout_11.addWidget(self.browse_pushButton, 0, QtCore.Qt.AlignLeft)
        self.path_output_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.path_output_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.path_output_label.setFont(font)
        self.path_output_label.setText("")
        self.path_output_label.setObjectName("path_output_label")
        self.horizontalLayout_11.addWidget(self.path_output_label)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setLineWidth(12)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_11.addWidget(self.line_3)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_11)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_widgets.addWidget(self.line)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(3)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_widgets.addWidget(self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.theta_tilt_offset_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.theta_tilt_offset_label.setFont(font)
        self.theta_tilt_offset_label.setLineWidth(3)
        self.theta_tilt_offset_label.setTextFormat(QtCore.Qt.RichText)
        self.theta_tilt_offset_label.setObjectName("theta_tilt_offset_label")
        self.horizontalLayout_7.addWidget(self.theta_tilt_offset_label)
        self.concavity_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.concavity_lineEdit.setObjectName("concavity_lineEdit")
        self.horizontalLayout_7.addWidget(self.concavity_lineEdit)
        self.theta_tilt_offset_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.theta_tilt_offset_label_2.setFont(font)
        self.theta_tilt_offset_label_2.setLineWidth(3)
        self.theta_tilt_offset_label_2.setTextFormat(QtCore.Qt.RichText)
        self.theta_tilt_offset_label_2.setObjectName("theta_tilt_offset_label_2")
        self.horizontalLayout_7.addWidget(self.theta_tilt_offset_label_2)
        self.curve_center_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.curve_center_lineEdit.setObjectName("curve_center_lineEdit")
        self.horizontalLayout_7.addWidget(self.curve_center_lineEdit)
        self.theta_tilt_offset_label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.theta_tilt_offset_label_5.setFont(font)
        self.theta_tilt_offset_label_5.setLineWidth(3)
        self.theta_tilt_offset_label_5.setTextFormat(QtCore.Qt.RichText)
        self.theta_tilt_offset_label_5.setObjectName("theta_tilt_offset_label_5")
        self.horizontalLayout_7.addWidget(self.theta_tilt_offset_label_5)
        self.curve_E0_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.curve_E0_lineEdit.setObjectName("curve_E0_lineEdit")
        self.horizontalLayout_7.addWidget(self.curve_E0_lineEdit)
        self.theta_tilt_offset_label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.theta_tilt_offset_label_4.setFont(font)
        self.theta_tilt_offset_label_4.setLineWidth(3)
        self.theta_tilt_offset_label_4.setTextFormat(QtCore.Qt.RichText)
        self.theta_tilt_offset_label_4.setObjectName("theta_tilt_offset_label_4")
        self.horizontalLayout_7.addWidget(self.theta_tilt_offset_label_4)
        self.E_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.E_lineEdit.sizePolicy().hasHeightForWidth())
        self.E_lineEdit.setSizePolicy(sizePolicy)
        self.E_lineEdit.setObjectName("E_lineEdit")
        self.horizontalLayout_7.addWidget(self.E_lineEdit)
        self.theta_tilt_offset_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.theta_tilt_offset_label_3.setFont(font)
        self.theta_tilt_offset_label_3.setLineWidth(3)
        self.theta_tilt_offset_label_3.setTextFormat(QtCore.Qt.RichText)
        self.theta_tilt_offset_label_3.setObjectName("theta_tilt_offset_label_3")
        self.horizontalLayout_7.addWidget(self.theta_tilt_offset_label_3)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_7.addWidget(self.line_6)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.E_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.E_label_2.setFont(font)
        self.E_label_2.setLineWidth(3)
        self.E_label_2.setTextFormat(QtCore.Qt.PlainText)
        self.E_label_2.setObjectName("E_label_2")
        self.horizontalLayout_3.addWidget(self.E_label_2)
        self.curve_length_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curve_length_lineEdit.sizePolicy().hasHeightForWidth())
        self.curve_length_lineEdit.setSizePolicy(sizePolicy)
        self.curve_length_lineEdit.setObjectName("curve_length_lineEdit")
        self.horizontalLayout_3.addWidget(self.curve_length_lineEdit)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setLineWidth(3)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.ls_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ls_comboBox.setObjectName("ls_comboBox")
        self.ls_comboBox.addItem("")
        self.ls_comboBox.addItem("")
        self.ls_comboBox.addItem("")
        self.ls_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.ls_comboBox)
        self.color_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.color_comboBox.setObjectName("color_comboBox")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.color_comboBox)
        self.lw_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.lw_comboBox.setObjectName("lw_comboBox")
        self.lw_comboBox.addItem("")
        self.lw_comboBox.addItem("")
        self.lw_comboBox.addItem("")
        self.lw_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.lw_comboBox)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_5.addWidget(self.line_4)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_widgets.addWidget(self.line_2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(3)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_widgets.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(44, 30, 44, -1)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.E_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.E_label.setFont(font)
        self.E_label.setLineWidth(3)
        self.E_label.setTextFormat(QtCore.Qt.PlainText)
        self.E_label.setObjectName("E_label")
        self.horizontalLayout.addWidget(self.E_label)
        self.kmin_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kmin_lineEdit.sizePolicy().hasHeightForWidth())
        self.kmin_lineEdit.setSizePolicy(sizePolicy)
        self.kmin_lineEdit.setObjectName("kmin_lineEdit")
        self.horizontalLayout.addWidget(self.kmin_lineEdit)
        self.kmax_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.kmax_lineEdit.setSizePolicy(sizePolicy)
        self.kmax_lineEdit.setObjectName("kmax_lineEdit")
        self.horizontalLayout.addWidget(self.kmax_lineEdit)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.E_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.E_label_3.setFont(font)
        self.E_label_3.setLineWidth(3)
        self.E_label_3.setTextFormat(QtCore.Qt.PlainText)
        self.E_label_3.setObjectName("E_label_3")
        self.horizontalLayout_4.addWidget(self.E_label_3)
        self.Emin_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Emin_lineEdit.sizePolicy().hasHeightForWidth())
        self.Emin_lineEdit.setSizePolicy(sizePolicy)
        self.Emin_lineEdit.setObjectName("Emin_lineEdit")
        self.horizontalLayout_4.addWidget(self.Emin_lineEdit)
        self.Emax_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Emax_lineEdit.sizePolicy().hasHeightForWidth())
        self.Emax_lineEdit.setSizePolicy(sizePolicy)
        self.Emax_lineEdit.setObjectName("Emax_lineEdit")
        self.horizontalLayout_4.addWidget(self.Emax_lineEdit)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_buton_plotBZ = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buton_plotBZ.setObjectName("horizontalLayout_buton_plotBZ")
        self.clickHere_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clickHere_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clickHere_pushButton.sizePolicy().hasHeightForWidth())
        self.clickHere_pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.clickHere_pushButton.setFont(font)
        self.clickHere_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clickHere_pushButton.setMouseTracking(False)
        self.clickHere_pushButton.setTabletTracking(False)
        self.clickHere_pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.clickHere_pushButton.setObjectName("clickHere_pushButton")
        self.horizontalLayout_buton_plotBZ.addWidget(self.clickHere_pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_widgets.addLayout(self.horizontalLayout_buton_plotBZ)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(830, 20, 461, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.plottingSpace_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.plottingSpace_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plottingSpace_verticalLayout.setObjectName("plottingSpace_verticalLayout")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(829, 570, 471, 81))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(3)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.mass_output_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.mass_output_label.setEnabled(True)
        self.mass_output_label.setText("")
        self.mass_output_label.setObjectName("mass_output_label")
        self.horizontalLayout_13.addWidget(self.mass_output_label)
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(803, 20, 41, 731))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setMidLineWidth(0)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Effective mass calculator (by aymen mahmoudi) V 2.0"))
        self.browse_pushButton.setText(_translate("Form", "Browse"))
        self.label_7.setText(_translate("Form", "Parabolic fitting"))
        self.theta_tilt_offset_label.setText(_translate("Form", "<html><head/><body><p>E = </p></body></html>"))
        self.concavity_lineEdit.setText(_translate("Form", "-5"))
        self.concavity_lineEdit.setPlaceholderText(_translate("Form", "tilt offset"))
        self.theta_tilt_offset_label_2.setText(_translate("Form", "<html><head/><body><p>10<span style=\" vertical-align:super;\">-35</span> x (k -</p></body></html>"))
        self.curve_center_lineEdit.setText(_translate("Form", "0"))
        self.curve_center_lineEdit.setPlaceholderText(_translate("Form", "integration"))
        self.theta_tilt_offset_label_5.setText(_translate("Form", "<html><head/><body><p>)<span style=\" vertical-align:super;\">2 </span>+ </p></body></html>"))
        self.curve_E0_lineEdit.setText(_translate("Form", "-1"))
        self.curve_E0_lineEdit.setPlaceholderText(_translate("Form", "integration"))
        self.theta_tilt_offset_label_4.setText(_translate("Form", "<html><head/><body><p> + </p></body></html>"))
        self.E_lineEdit.setText(_translate("Form", "0"))
        self.E_lineEdit.setPlaceholderText(_translate("Form", "Energy"))
        self.theta_tilt_offset_label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">x k </span></p></body></html>"))
        self.E_label_2.setText(_translate("Form", "parabol length (+/- around the center)"))
        self.curve_length_lineEdit.setText(_translate("Form", "0.5"))
        self.curve_length_lineEdit.setPlaceholderText(_translate("Form", "Energy"))
        self.label_10.setText(_translate("Form", "Line style/color/width"))
        self.ls_comboBox.setItemText(0, _translate("Form", "dashed"))
        self.ls_comboBox.setItemText(1, _translate("Form", "dotted"))
        self.ls_comboBox.setItemText(2, _translate("Form", "solid"))
        self.ls_comboBox.setItemText(3, _translate("Form", "dashdot"))
        self.color_comboBox.setItemText(0, _translate("Form", "red"))
        self.color_comboBox.setItemText(1, _translate("Form", "green"))
        self.color_comboBox.setItemText(2, _translate("Form", "blue"))
        self.color_comboBox.setItemText(3, _translate("Form", "yellow"))
        self.lw_comboBox.setItemText(0, _translate("Form", "1"))
        self.lw_comboBox.setItemText(1, _translate("Form", "2"))
        self.lw_comboBox.setItemText(2, _translate("Form", "3"))
        self.lw_comboBox.setItemText(3, _translate("Form", "4"))
        self.label_9.setText(_translate("Form", "Picture settings"))
        self.E_label.setText(_translate("Form", "k (A°)  (min & max)  "))
        self.kmin_lineEdit.setText(_translate("Form", "-1"))
        self.kmin_lineEdit.setPlaceholderText(_translate("Form", "Phi"))
        self.kmax_lineEdit.setText(_translate("Form", "1"))
        self.kmax_lineEdit.setPlaceholderText(_translate("Form", "Phi"))
        self.E_label_3.setText(_translate("Form", "Energy (eV)  (min & max)    "))
        self.Emin_lineEdit.setText(_translate("Form", "-4"))
        self.Emin_lineEdit.setPlaceholderText(_translate("Form", "Energy"))
        self.Emax_lineEdit.setText(_translate("Form", "1"))
        self.Emax_lineEdit.setPlaceholderText(_translate("Form", "Energy"))
        self.clickHere_pushButton.setToolTip(_translate("Form", "this is toolTIP"))
        self.clickHere_pushButton.setText(_translate("Form", "Re-calculate"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Relative eff mass </span><span style=\" font-size:14pt; vertical-align:super;\">m*</span><span style=\" font-size:14pt;\">⁄</span><span style=\" font-size:14pt; vertical-align:sub;\">m0</span></p></body></html>"))
