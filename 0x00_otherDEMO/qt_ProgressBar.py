# 正在想怎么修改一下，自己感觉代码不太对劲
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar
from random import random
from time import sleep

# 进度条的百分比进度输入
def reco():
    global percent
    while percent <= 100:
        percent = percent + 1
        sleep(random())
        return percent

# 进度条
class sbar(QWidget):
    # 子类
    def __init__(self):
        super().__init__()
        self.initUI()
    # 框框的初始值
    def initUI(self):
        self.resize(300, 200)

        self.pgb = QProgressBar(self)
        self.pgb.move(50, 50)
        self.pgb.resize(250, 20)

        # 进度条最大值最小值
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        #让框框show出来
        self.show()
        self.pgb.setValue(self.per())
        # 百分比进度
    def per(self):
        while reco() < 100:
            self.pgb.setValue(reco())
        else:
            return 100


if __name__ == "__main__":
    percent = 0
    app = QApplication(sys.argv)
    mc = sbar()
    app.exec()

