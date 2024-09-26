import sys
from PyQt5.QtWidgets import QApplication, QMainWindow ,QLineEdit,QPushButton
from PyQt5.uic import loadUi
import time


class MyWindow(QMainWindow):
    global query
    global i
    global l
    l=[]
    i=0
    def __init__(self):
        super(MyWindow,self).__init__()
        loadUi("CBtest.ui",self)
        self.setWindowTitle("CHATBOPT")
        self.setGeometry(100, 100, 600, 400)
        self.inputbx.setPlaceholderText("Type Something...")
        self.sendbtn.clicked.connect(self.on_click)

    def on_click(self):
        query = self.inputbx.text()
        if query:  # Ensure the query is not empty
            l.append(query)  # Append the query to the chat history list
            txt = self.output.toPlainText()  # Get the existing text from the QTextBrowser
            # Append the new chat
            txt += f'User : {query}\n'
            txt += 'Bot : \n'  # You can add the bot's response here
            txt += '\n'
            self.output.setText(txt)  # Update the QTextBrowser with the new text
            self.inputbx.clear()  # Clear the input box for the next query


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

