from PyQt6 import QtCore, QtGui, QtWidgets


class Rule(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Rule")
        Dialog.resize(400, 406)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(
            self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(
            self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.listView = QtWidgets.QListView(parent=Dialog)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "规则格式"))
        self.label_4.setText(
            _translate(
                "Dialog",
                "前提1 | … | 前提n > 结论( | 表示“或) \n" "前提1 & … & 前提n > 结论( & 表示“与”)\n" " ",
            )
        )
        self.pushButton.setText(_translate("Dialog", "修改规则"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Rule()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
