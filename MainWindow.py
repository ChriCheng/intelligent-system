from PRbase import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QStringListModel
from EditFactWindow import *
from RuleManage import *
from AddRule import *
from Reult import *
from Info import *
from Rule import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Main")
        Form.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.Chosen = QtWidgets.QListView(parent=Form)
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
        self.Fact = QtWidgets.QListView(parent=Form)
        self.Fact.setObjectName("Fact")
        self.gridLayout.addWidget(self.Fact, 2, 0, 1, 1)
        self.AnotherListView = QtWidgets.QListView(parent=Form)
        self.AnotherListView.setObjectName("AnotherListView")
        self.gridLayout.addWidget(self.AnotherListView, 2, 2, 1, 1)
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
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(
            self.label_3, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main"))
        self.label_2.setText(_translate("Form", "已选事实"))
        self.label.setText(_translate("Form", "已有事实"))
        self.pushButton_2.setText(_translate("Form", "开始推理"))
        self.pushButton.setText(_translate("Form", "管理规则"))
        self.pushButton_3.setText(_translate("Form", "编辑事实"))
        self.pushButton_4.setText(_translate("Form", "选择事实"))
        self.label_3.setText(_translate("Form", "已有规则"))


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.Open_1)
        self.ui.pushButton.clicked.connect(self.Open_2)
        self.ui.pushButton_2.clicked.connect(self.Open_3)
        self.FactList = []

    def Open_3(self):
        self.form3 = QtWidgets.QDialog()
        self.ui3 = Result()
        self.ui3.setupUi(self.form3)
        self.ui3.exec()

    def Open_2(self):
        self.form2 = QtWidgets.QDialog()
        self.ui2 = Rule()
        self.ui2.setupUi(self.form2)
        self.ui2.exec()

    def Open_1(self):
        self.form1 = QtWidgets.QDialog()
        self.ui1 = FactWindow()
        self.ui1.setupUi(self.form1)
        self.ui1.set_fact_list(self.FactList)
        self.ui1.factSubmitted.connect(self.factSubmittedHandler)
        self.form1.exec()

    def factSubmittedHandler(self, facts):
        self.FactList = facts
        slm = QtCore.QStringListModel()
        slm.setStringList(facts)
        self.ui.Fact.setModel(slm)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
