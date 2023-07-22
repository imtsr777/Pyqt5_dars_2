from PyQt5.QtWidgets import *
from data import userData

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowSettings()
    

    def windowSettings(self):
        self.setFixedSize(300, 400)
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10,10, 250, 100)

        self.checkBox = QCheckBox(self)
        self.checkBox.move(10, 130)

        self.btn = QPushButton("click",self)
        self.btn.move(10, 180)
        self.btn.setEnabled(False)

        self.checkBox.clicked.connect(self.turnButton)
        self.btn.clicked.connect(self.showMessage)

    def turnButton(self):
        self.btn.setEnabled( self.checkBox.isChecked() )

    def showMessage(self):
        word = self.textEdit.toPlainText()
        self.messageBox(word)


    def messageBox(self, message):
        msg = QMessageBox(self)
        msg.setText(message)
        msg.show()





app = QApplication([])
window = Window()
window.show()
app.exec()
