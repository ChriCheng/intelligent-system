from PyQt6 import QtCore, QtGui, QtWidgets


class Result(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(
            self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.listView = QtWidgets.QListView(parent=Dialog)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Result"))
        self.label.setText(_translate("Dialog", "推理结果"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Result()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
