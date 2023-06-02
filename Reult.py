from PyQt6 import QtCore, QtGui, QtWidgets


class Result(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.P = []
        self._ = []
        self.DB = []

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

    def setlist(self, Plist, Rlist, ChosenList):
        self.P = Plist
        self._ = Rlist
        self.DB = ChosenList

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Result"))
        self.label.setText(_translate("Dialog", "推理结果"))

    def is_include_in_DB(self, p):
        for i in p:
            if i not in self.DB:
                return False
        return True

    def inference(self):
        self.result = "无法识别"
        mark = [0] * len(self.P)  # 标记规则是否访问过
        res = False  # 是否有结果
        flag = True  # 本次推理是否有结果

        while flag:
            flag = False
            for i, p in enumerate(self.P):
                # 遍历每条规则的前件
                if self.is_include_in_DB(p) and mark[i] == 0:
                    self.DB.append(self._[i])  # 如果事实是一条规则前件的一部分，就将该规则的后件加入事实库
                    mark[i] = 1  # 标记该规则已经使用
                    self.result = self._[i]  # 当前的结果就是该条规则的后件
                    self.procedure.append("%s -> %s" % (p, self._[i]))  # 输出推理过程
                    flag = True
                    res = True  # 推理结束，输出结果
        if res:
            pix = QtGui.QPixmap(self.result + ".jpg")
            self.label_5.setPixmap(pix)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Result()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
