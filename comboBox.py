from PyQt5.QtWidgets import *
from data import userData

class Colors:
    red = "Red"
    yellow = "Yellow"
    blue = "Blue"



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)

        self.comboBox = QComboBox(self)
        # self.comboBox.addItem("Salom")
        # self.comboBox.addItem("Hayr")


        comboTexts = [Colors.blue, Colors.red, Colors.yellow]

        self.comboBox.addItems(comboTexts)
        self.comboBox.activated.connect(self.some)

    def some(self):
        color = self.comboBox.currentText()
        self.setStyleSheet(f"background-color: {color}")



app = QApplication([])
window = Window()
window.show()
app.exec()
