from PyQt5.QtWidgets import *
from data import userData

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)
        self.radioB1 = QRadioButton( "Ayol" ,self)
        self.radioB2 = QRadioButton( "Erkak",self)
        self.btn = QPushButton("Click",self)
        self.btn.clicked.connect(self.sendButton)

        self.radioB1.move(20, 40)
        self.radioB2.move(100, 40)

    def sendButton(self):
        if( self.radioB1.isChecked() ):
            word = self.radioB1.text()
            self.messageBox(word)

        elif( self.radioB2.isChecked() ):
            word = self.radioB2.text()
            self.messageBox(word)


    def messageBox(self, userText):
        miniWindow = QMessageBox(self)
        miniWindow.setText(userText)
        miniWindow.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        

        miniWindow.show()
        button = miniWindow.exec()

        if( button == QMessageBox.Yes ):
            print("Yes bosildi")
        elif( button == QMessageBox.No):
            print("No bosildi")



    def printHello(self):
        print("Hello")




app = QApplication([])
window = Window()
window.show()
app.exec()
