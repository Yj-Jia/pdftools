from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QFileDialog)
import sys
from pdftools import pdf_tools


class PDFtools(QWidget):

    def __init__(self):
        super().__init__()
        self.pdftoolsgui()

    def pdftoolsgui(self):


        self.setGeometry(700, 700, 700, 450)
        self.setFixedSize(700,450)
        self.setWindowTitle('PDFtools')

        self.label1 = QLabel('文件名：', self)
        self.label1.move(20, 20)

        self.label2 = QLabel('起始页：', self)
        self.label2.move(20, 80)

        self.label3 = QLabel('终止页：', self)
        self.label3.move(20, 140)

        self.label4 = QLabel('新文件名：', self)
        self.label4.move(20, 200)

        self.label5 = QLabel('点此开始拆分', self)
        self.label5.move(20, 260)

        self.label6 = QLabel('          ', self)
        self.label6.move(120, 20)

        self.label7 = QLabel('    ', self)
        self.label7.move(120, 80)

        self.label8 = QLabel('    ', self)
        self.label8.move(120, 140)

        self.label9 = QLabel('            ', self)
        self.label9.move(150, 200)

        self.btn1 = QPushButton('选择文件', self)
        self.btn1.move(300, 20)

        self.btn2 = QPushButton('选择起始页', self)
        self.btn2.move(300, 80)

        self.btn3 = QPushButton('选择终止页', self)
        self.btn3.move(300, 140)

        self.btn4 = QPushButton('输入新文件名', self)
        self.btn4.move(300, 200)

        self.btn5 = QPushButton('开始', self)
        self.btn5.move(300, 260)

        self.show()

        self.btn1.clicked.connect(self.openfile)
        self.btn2.clicked.connect(self.showDialog)
        self.btn3.clicked.connect(self.showDialog)
        self.btn4.clicked.connect(self.showDialog)
        self.btn5.clicked.connect(self.start)

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './')
        self.filename = fname[0]

    def start(self):
        pdf_tools(self.filename, self.first_page, self.last_page, self.new_file)


    def showDialog(self):
        sender = self.sender()
        if sender == self.btn2:
            firpage, ok = QInputDialog.getInt(self, '起始页码', '请输入起始页（包含该页）：')
            if ok:
                self.label7.setText(str(firpage))
                print(firpage)
                self.first_page = firpage
        elif sender == self.btn3:
            lastpg, ok = QInputDialog.getInt(self, '终止页码', '请选择终止页（包含该页）：')
            if ok:
                self.label8.setText(str(lastpg))
                self.last_page = lastpg
        elif sender == self.btn4:
            newfnm, ok = QInputDialog.getText(self, '新文件名', '请输入新文件名：')
            if ok:
                self.label9.setText(newfnm)
                self.new_file = newfnm



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFtools()
    sys.exit(app.exec_())