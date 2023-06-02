from PyQt6 import QtCore, QtGui, QtWidgets


class AddRule(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 270)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(
            self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(
            self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(parent=Dialog)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        # 返回
        self.pushButton_2.clicked.connect(self.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "规则格式"))
        self.label_2.setText(
            _translate(
                "Dialog",
                "前提1 | … | 前提n > 结论 ( | 表示“或) \n" "前提1 & … & 前提n > 结论 ( & 表示“与”)\n" " ",
            )
        )
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AddRule()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
