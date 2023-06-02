from PyQt6 import QtCore, QtGui, QtWidgets


class Info(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.columnView = QtWidgets.QColumnView(parent=Dialog)
        self.columnView.setObjectName("columnView")
        self.verticalLayout.addWidget(self.columnView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Info"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Info()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
