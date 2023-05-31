from PRbase import ProductionRule
from PyQt6 import QtCore, QtGui, QtWidgets

from AddFactWindow import *


class MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Main")
        Form.resize(500, 400)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(
            self.label_2, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(
            self.label, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 9, 1, 1, 1)
        self.Chosen = QtWidgets.QColumnView(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(self.Chosen.sizePolicy().hasHeightForWidth())
        self.Chosen.setSizePolicy(sizePolicy)
        self.Chosen.setObjectName("Chosen")
        self.gridLayout.addWidget(self.Chosen, 2, 1, 1, 1)
        self.Fact = QtWidgets.QColumnView(parent=Form)
        self.Fact.setObjectName("Fact")
        self.gridLayout.addWidget(self.Fact, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        # 增加事实
        self.pushButton_3.clicked.connect(self.Open_1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def Open_1(self):
        self.form2 = QtWidgets.QWidget()
        self.ui2 = FactWindow()  # Ui_form为你副窗口的对象名
        self.ui2.setupUi(self.form2)
        self.ui2.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "已选事实"))
        self.label.setText(_translate("Form", "已有事实"))
        self.pushButton_2.setText(_translate("Form", "开始推理"))
        self.pushButton.setText(_translate("Form", "管理规则"))
        self.pushButton_3.setText(_translate("Form", "增加事实"))
        self.pushButton_4.setText(_translate("Form", "选择事实"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec())
