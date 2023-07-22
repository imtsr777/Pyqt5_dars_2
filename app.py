from PyQt5.QtWidgets import *
from data import userData

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)
        self.lineEdit1 = QLineEdit(self)
        self.btn1 = QPushButton("Click",self)
        self.btn1.move(100, 0)
        self.btn1.clicked.connect(self.printLineEditText)
        self.lineEdit1.textChanged.connect(self.printLineEditText)
        self.bigText = QTextEdit(self)
        self.bigText.setGeometry(0, 60, 200, 200)


    def printLineEditText(self):
        lineText = self.lineEdit1.text()
        data = ""
        for item in userData(lineText):
            data += item + "\n"

        self.bigText.setText(data)

    
app = QApplication([])
window = Window()
window.show()
app.exec()

data = "Salom"
print("" in data)