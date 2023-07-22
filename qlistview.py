from PyQt5.QtWidgets import *
from data import userData

class Window(QMainWindow):

    _users = [ "Aziz", "Abror", "Sardor", "Kamron", "Asad" ]

    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)
        self.qListWidget = QListWidget(self)
        self.qListWidget.setGeometry(10, 50, 250, 300)
        
        self.qListWidget.addItems(self._users)

        self.qListWidget.itemClicked.connect(self.printItem)


    def printItem(self):
        currentItem = self.qListWidget.currentItem()
        print(currentItem.text())





app = QApplication([])
window = Window()
window.show()
app.exec()
