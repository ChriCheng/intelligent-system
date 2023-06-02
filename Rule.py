from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QStringListModel


class Rule(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    RuleToMain = QtCore.pyqtSignal(list, list)  # 传到主窗口

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
        self.RuleList = []
        self.listView.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers
        )
        # 编辑规则
        self.pushButton.clicked.connect(self.Open_1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Open_1(self):
        import EditRule

        self.form1 = QtWidgets.QDialog()
        self.ui1 = EditRule.EditRule()
        self.ui1.setupUi(self.form1)
        self.RuleList = [
            f"{self.Plist[i]} > {self.Rlist[i]}" for i in range(len(self.Plist))
        ]
        self.ui1.set_rule_list(self.RuleList)
        self.ui1.ruleSubmitted.connect(self.ruleSubmittedHandler)  # 连接信号和槽函数
        self.form1.exec()

    def ruleSubmittedHandler(self, Plist, Rlist):
        self.Plist = Plist
        self.Rlist = Rlist

        # 创建包含Plist和Rlist的字符串列表
        rule_list = [f"{Plist[i]} > {Rlist[i]}" for i in range(len(Plist))]
        self.RuleToMain.emit(self.Plist, self.Rlist)
        # 更新界面显示
        slm = QStringListModel()
        slm.setStringList(rule_list)  # 将rule_list设置为字符串列表模型的数据源
        self.listView.setModel(slm)  # 在listView中显示rule_list的内容

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Rule"))
        self.label_3.setText(_translate("Dialog", "已有规则"))

        self.pushButton.setText(_translate("Dialog", "修改规则"))

    def setlist(self, Plist, Rlist):
        self.Plist = Plist
        self.Rlist = Rlist
        rule_list = [f"{Plist[i]} > {Rlist[i]}" for i in range(len(Plist))]
        self.RuleToMain.emit(self.Plist, self.Rlist)
        # 更新界面显示
        slm = QStringListModel()
        slm.setStringList(rule_list)  # 将rule_list设置为字符串列表模型的数据源
        self.listView.setModel(slm)  # 在listView中显示rule_list的内容


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Rule()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

# A | B > C
# K & O > P
