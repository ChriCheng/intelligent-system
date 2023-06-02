from PyQt6 import QtCore, QtGui, QtWidgets


class RuleManage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 294)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(
            self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.listView = QtWidgets.QListView(parent=Dialog)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        # self.verticalLayout_2.addWidget(self.pushButton)
        # self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.verticalLayout_2.addWidget(self.pushButton_2)
        # self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        # 返回
        self.pushButton_4.clicked.connect(self.reject)
        # 增加规则
        self.pushButton.clicked.connect(self.Open_1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Open_1(self):
        import AddRule

        self.form1 = QtWidgets.QDialog()
        self.ui1 = AddRule.AddRule()
        self.ui1.setupUi(self.form1)
        self.ui1.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "已有规则"))
        self.pushButton.setText(_translate("Dialog", "修改规则"))
        # self.pushButton_2.setText(_translate("Dialog", "删除规则"))
        # self.pushButton_3.setText(_translate("Dialog", "修改规则"))
        self.pushButton_4.setText(_translate("Dialog", "返回"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = RuleManage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
