"""
setEnabled
checkBox
isChecked

"""





from PyQt5.QtWidgets import *
from data import userData

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)
        self.btn = QPushButton("Click",self)
        self.btn.setEnabled(False)
        self.btn.clicked.connect(self.buttonClicked)
        self.btn.setStyleSheet("font-size: 30px; background-color: grey; border-radius:10px")
        self.checkBox = QCheckBox("Rozimisiz",self)
        self.checkBox.move(20, 50)
        self.checkBox.clicked.connect(self.buttonClicked)


    def buttonClicked(self):
        self.btn.setEnabled( self.checkBox.isChecked() )
        



app = QApplication([])
window = Window()
window.show()
app.exec()
