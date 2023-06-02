from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget


class FactWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    factSubmitted = QtCore.pyqtSignal(list)  # 返回增加型号

    def setupUi(self, Dialog):
        Dialog.setObjectName("Add")  # 设置对话框对象名
        Dialog.resize(371, 324)
        self.list = []
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(
            self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)  # 使用 QTextEdit 作为输入框
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit.setPlainText("\n".join(self.list))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 确定按钮点击事件
        self.pushButton.clicked.connect(self.accept)
        # self.pushButton.clicked.connect(self.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def accept(self):
        # 获取用户输入的文本内容
        text = self.textEdit.toPlainText()
        print(f"{text}")
        # 将文本按回车分割为数组
        facts = [fact for fact in text.split("\n") if fact.strip()]
        # 在此处对获取到的事实数据进行处理或保存操作
        print(facts)  # 示例：打印事实数组
        self.factSubmitted.emit(facts)
        # super().accept()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Add", "Add"))  # 设置对话框标题
        self.label.setText(_translate("Add", "请对内容进行编辑"))

        self.pushButton.setText(_translate("Add", "确定"))

    def set_fact_list(self, fact_list):
        self.list = fact_list
        self.textEdit.setPlainText("\n".join(self.list))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = FactWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
