from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sys

from PyQt5.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.mainVlayout = QVBoxLayout(self)
        self.inputField = QLineEdit(self)
        self.clearBtn = QPushButton('clear',self)
        self.clearBtn.setStyleSheet("font-size:18px")
        self.headerHlayout = QHBoxLayout(self)
        self.headerHlayout.addWidget(self.inputField)
        self.headerHlayout.addWidget(self.clearBtn)
        self.mainVlayout.addLayout(self.headerHlayout)



        self.setLayout(self.mainVlayout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
