# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(718, 784)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deckSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckSelect.sizePolicy().hasHeightForWidth())
        self.deckSelect.setSizePolicy(sizePolicy)
        self.deckSelect.setObjectName("deckSelect")
        self.gridLayout_2.addWidget(self.deckSelect, 0, 0, 1, 1)
        self.adcSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adcSelect.sizePolicy().hasHeightForWidth())
        self.adcSelect.setSizePolicy(sizePolicy)
        self.adcSelect.setObjectName("adcSelect")
        self.gridLayout_2.addWidget(self.adcSelect, 0, 1, 1, 2)
        self.softwareSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.softwareSelect.sizePolicy().hasHeightForWidth())
        self.softwareSelect.setSizePolicy(sizePolicy)
        self.softwareSelect.setObjectName("softwareSelect")
        self.gridLayout_2.addWidget(self.softwareSelect, 0, 3, 1, 2)
        self.mediaSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mediaSelect.sizePolicy().hasHeightForWidth())
        self.mediaSelect.setSizePolicy(sizePolicy)
        self.mediaSelect.setObjectName("mediaSelect")
        self.gridLayout_2.addWidget(self.mediaSelect, 0, 5, 1, 1)
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.speedSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedSelect.sizePolicy().hasHeightForWidth())
        self.speedSelect.setSizePolicy(sizePolicy)
        self.speedSelect.setObjectName("speedSelect")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.speedSelect)
        self.gridLayout_2.addLayout(self.formLayout_10, 1, 0, 1, 2)
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.eqSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eqSelect.sizePolicy().hasHeightForWidth())
        self.eqSelect.setSizePolicy(sizePolicy)
        self.eqSelect.setObjectName("eqSelect")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.eqSelect)
        self.gridLayout_2.addLayout(self.formLayout_11, 1, 2, 1, 2)
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.typeSelect = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeSelect.sizePolicy().hasHeightForWidth())
        self.typeSelect.setSizePolicy(sizePolicy)
        self.typeSelect.setObjectName("typeSelect")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.typeSelect)
        self.gridLayout_2.addLayout(self.formLayout_12, 1, 4, 1, 2)
        self.md5Check = QtWidgets.QCheckBox(Dialog)
        self.md5Check.setChecked(True)
        self.md5Check.setObjectName("md5Check")
        self.gridLayout_2.addWidget(self.md5Check, 2, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.descriptionLine = QtWidgets.QLineEdit(Dialog)
        self.descriptionLine.setObjectName("descriptionLine")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.descriptionLine)
        self.horizontalLayout.addLayout(self.formLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.originatorLine = QtWidgets.QLineEdit(Dialog)
        self.originatorLine.setObjectName("originatorLine")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.originatorLine)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.originatorRefLine = QtWidgets.QLineEdit(Dialog)
        self.originatorRefLine.setObjectName("originatorRefLine")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.originatorRefLine)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.originationDateLine = QtWidgets.QLineEdit(Dialog)
        self.originationDateLine.setObjectName("originationDateLine")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.originationDateLine)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_5.addLayout(self.formLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.originationTimeLine = QtWidgets.QLineEdit(Dialog)
        self.originationTimeLine.setObjectName("originationTimeLine")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.originationTimeLine)
        self.horizontalLayout_6.addLayout(self.formLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.titleLine = QtWidgets.QLineEdit(Dialog)
        self.titleLine.setObjectName("titleLine")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLine)
        self.horizontalLayout_7.addLayout(self.formLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.technicianBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.technicianBox.sizePolicy().hasHeightForWidth())
        self.technicianBox.setSizePolicy(sizePolicy)
        self.technicianBox.setEditable(True)
        self.technicianBox.setObjectName("technicianBox")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.technicianBox)
        self.horizontalLayout_8.addLayout(self.formLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.copyrightText = QtWidgets.QPlainTextEdit(Dialog)
        self.copyrightText.setObjectName("copyrightText")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.copyrightText)
        self.horizontalLayout_9.addLayout(self.formLayout_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.copyrightSelect = QtWidgets.QComboBox(Dialog)
        self.copyrightSelect.setObjectName("copyrightSelect")
        self.verticalLayout.addWidget(self.copyrightSelect)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 0, 1, 3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.codingHistoryText = QtWidgets.QPlainTextEdit(Dialog)
        self.codingHistoryText.setObjectName("codingHistoryText")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.codingHistoryText)
        self.horizontalLayout_10.addLayout(self.formLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout_10, 5, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Speed:"))
        self.label_12.setText(_translate("Dialog", "EQ:"))
        self.label_13.setText(_translate("Dialog", "Tape type:"))
        self.md5Check.setText(_translate("Dialog", "Embed MD5 of data chunk"))
        self.label.setText(_translate("Dialog", "Description"))
        self.label_2.setText(_translate("Dialog", "Originator"))
        self.label_3.setText(_translate("Dialog", "OriginatorRef"))
        self.label_4.setText(_translate("Dialog", "OriginationDate"))
        self.label_5.setText(_translate("Dialog", "OriginationTime"))
        self.label_6.setText(_translate("Dialog", "Title"))
        self.label_8.setText(_translate("Dialog", "Technician"))
        self.label_9.setText(_translate("Dialog", "Copyright"))
        self.label_10.setText(_translate("Dialog", "Replace with boilerplate:"))
        self.label_11.setText(_translate("Dialog", "CodingHistory"))

