from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QStringListModel


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

        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit.setReadOnly(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Result"))
        self.label.setText(_translate("Dialog", "推理结果"))

    def setlist(self, Plist, Rlist, ChosenList):
        self.Plist = Plist
        self.Rlist = Rlist
        self.DB = "".join(ChosenList)
        self.textEdit.append("- 开始推理 -")
        self.perform_inference()  # 进行推理
        self.textEdit.append("- 推理结束 -")

    def is_include_in_DB(self, p):
        conditions = p.split(" & ")

        for condition in conditions:
            if condition not in self.DB:
                return False
        return True

    def perform_inference(self):
        self.result = "无法识别"
        mark = [0] * len(self.Plist)  # 标记规则是否访问过
        flag = True  # 本次推理是否有结果

        while flag:
            flag = False
            for i in range(len(self.Plist)):
                if self.is_include_in_DB(self.Plist[i]) and mark[i] == 0:
                    self.DB += self.Rlist[i]  # 如果前提与动态数据库匹配，将结果加入事实库
                    mark[i] = 1  # 标记该规则已经使用
                    self.result = self.Rlist[i]  # 当前的结果就是该条规则的后件
                    self.textEdit.append(
                        "%s -> %s" % (self.Plist[i], self.Rlist[i])
                    )  # 输出推理过程
                    flag = True
                    res = True  # 推理结束，输出结果
        self.textEdit.append(self.result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Result()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
