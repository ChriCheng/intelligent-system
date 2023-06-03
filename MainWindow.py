from PRbase import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QStringListModel
from EditFactWindow import *
from EditRule import *
from Reult import *
from Info import *
from Rule import *


class MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Main")
        Form.resize(500, 400)
        self.FactList = self.loadFromFile("save/factlist.txt")
        self.Rlist = self.loadFromFile("save/Rlist.txt")
        self.Plist = self.loadFromFile("save/Plist.txt")
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
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)

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
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_5, 9, 1, 1, 1)
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

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.pushButton_5.clicked.connect(self.ClearChosenList)
        # 显示内容
        slm = QStringListModel()
        slm.setStringList(self.FactList)
        self.Fact.setModel(slm)

        self.Fact.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.Chosen.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        # 选择列表
        self.ChosenList = []

        # 编辑事实
        self.pushButton_3.clicked.connect(self.Open_1)
        # 管理规则
        self.pushButton.clicked.connect(self.Open_2)
        # 开始推理
        self.pushButton_2.clicked.connect(self.Open_3)
        # 清空事实
        self.pushButton_5.clicked.connect(self.ClearChosenList)
        # 存储
        Form.closeEvent = self.closeEvent
        # 双击选择：
        self.Fact.doubleClicked.connect(self.CurrentItem)
        # 双击选择
        self.Chosen.doubleClicked.connect(self.retruntofact)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retruntofact(self):
        indexes = self.Chosen.selectedIndexes()
        if not indexes:
            return
        item = indexes[0].data()
        self.FactList.append(item)
        slm = QStringListModel()
        slm.setStringList(self.FactList)
        self.Fact.setModel(slm)
        self.ChosenList.remove(item)
        model = QStringListModel(self.ChosenList)
        self.Chosen.setModel(model)

    def loadFromFile(self, filename):
        try:
            with open(filename, "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            return []

    def closeEvent(self, even):
        # 保存FactList中的值到txt文件
        self.ClearChosenList()
        self.saveFactListToFile("save/factlist.txt", self.FactList)
        self.saveFactListToFile("save/Plist.txt", self.Plist)
        self.saveFactListToFile("save/Rlist.txt", self.Rlist)

    def saveFactListToFile(self, filename, List):
        with open(filename, "r+") as file:
            file.truncate(0)
        with open(filename, "w") as file:
            for fact in List:
                file.write(fact + "\n")

    def ClearChosenList(self):
        self.FactList = self.FactList + self.ChosenList
        self.ChosenList.clear()
        chose = QStringListModel(self.ChosenList)
        self.Chosen.setModel(chose)

        fact = QStringListModel(self.FactList)
        self.Fact.setModel(fact)

    def CurrentItem(self):
        indexes = self.Fact.selectedIndexes()
        if not indexes:
            return
        item = indexes[0].data()
        self.ChosenList.append(item)
        slm = QStringListModel()
        slm.setStringList(self.ChosenList)
        self.Chosen.setModel(slm)
        self.FactList.remove(item)
        fact_model = QStringListModel(self.FactList)
        self.Fact.setModel(fact_model)

    def Open_3(self):
        self.form3 = QtWidgets.QDialog()
        self.ui3 = Result()
        self.ui3.setupUi(self.form3)
        self.ui3.setlist(self.Plist, self.Rlist, self.ChosenList)
        self.form3.show()

    def Open_2(self):
        self.form2 = QtWidgets.QDialog()
        self.ui2 = Rule()
        self.ui2.setupUi(self.form2)
        self.ui2.setlist(self.Plist, self.Rlist)
        self.ui2.RuleToMain.connect(self.ruleClosedHandler)
        self.form2.show()

    def ruleClosedHandler(self, Plist, Rlist):
        self.Plist = Plist
        self.Rlist = Rlist
        rule_list = [f"{Plist[i]} > {Rlist[i]}" for i in range(len(Plist))]
        print("Received Plist:", Plist)
        print("Received Rlist:", Rlist)
        print("Rule list:", rule_list)

    def Open_1(self):
        self.form1 = QtWidgets.QDialog()
        self.ui1 = FactWindow()
        self.ui1.setupUi(self.form1)
        self.ui1.set_fact_list(self.FactList)
        self.ui1.factSubmitted.connect(self.factSubmittedHandler)  # 连接信号和槽函数
        self.form1.exec()

    def factSubmittedHandler(self, facts):
        self.FactList = facts
        slm = QStringListModel()
        slm.setStringList(facts)
        self.Fact.setModel(slm)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main"))
        self.label_2.setText(_translate("Form", "已选事实"))
        self.label.setText(_translate("Form", "已有事实"))
        self.pushButton_2.setText(_translate("Form", "开始推理"))
        self.pushButton.setText(_translate("Form", "管理规则"))
        self.pushButton_3.setText(_translate("Form", "编辑事实"))
        self.pushButton_5.setText(_translate("Form", "清空已选事实"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec())
