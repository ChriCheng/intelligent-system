from PyQt6 import QtCore, QtGui, QtWidgets


class EditRule(QtWidgets.QDialog):
    ruleSubmitted = QtCore.pyqtSignal(list, list)  # 返回列表

    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def match(self, rule):
        # 检查规则的前提条件和结论是否符合指定的格式
        # 返回布尔值，表示规则格式是否正确

        # 检查规则是否为空
        if not rule:
            self.Open_1("规则不能为空")
            return False

        # 检查规则是否包含前提条件和结论分隔符
        if ">" not in rule:
            self.Open_1("规则格式错误：缺少结论分隔符 '>'")
            return False

        # 拆分规则为前提条件和结论
        premises, conclusion = rule.split(">")

        # 检查前提条件是否为空
        premises = premises.strip()
        if not premises:
            self.Open_1("规则格式错误：缺少前提条件")
            return False

        # 检查结论是否为空
        conclusion = conclusion.strip()
        if not conclusion:
            self.Open_1("规则格式错误：缺少结论")
            return False

        return True

    def Open_1(self, exec):
        import Info

        self.form1 = QtWidgets.QDialog()
        self.ui1 = Info.Info()
        self.ui1.setupUi(self.form1)
        self.ui1.setInfo(exec)
        self.form1.exec()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 270)
        self.list = []
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
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)  # 使用 QTextEdit 作为输入框
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.textEdit.setPlainText("\n".join(self.list))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        # 确定
        self.pushButton.clicked.connect(self.accept)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def accept(self):
        # 获取用户输入的文本内容
        text = self.textEdit.toPlainText()
        # 将文本按回车分割为数组
        rules = [rule for rule in text.split("\n") if rule.strip()]
        Plist = []  # 存储前提条件的列表
        Rlist = []  # 存储结论的列表

        for rule in rules:
            if not self.match(rule):
                return
            premises, conclusion = rule.split(">")
            premises = premises.strip()
            conclusion = conclusion.strip()

            if "|" in premises:
                premises_list = premises.split("|")
                for premise in premises_list:
                    Plist.append(premise.strip())
                    Rlist.append(conclusion)
            else:
                Plist.append(premises)
                Rlist.append(conclusion)

        # 在此处对获取到的规则数据进行处理或保存操作
        self.ruleSubmitted.emit(Plist, Rlist)
        super().accept()

    def set_rule_list(self, rule_list):
        self.list = rule_list
        self.textEdit.setPlainText("\n".join(self.list))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("EditRule", "EditRule"))
        self.label.setText(_translate("Dialog", "规则格式"))
        self.label_2.setText(
            _translate(
                "Dialog",
                "前提1 | … | 前提n > 结论( | 表示“或) \n" "前提1 & … & 前提n > 结论( & 表示“与”)\n" " ",
            )
        )
        self.pushButton.setText(_translate("Dialog", "确定"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = EditRule()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
