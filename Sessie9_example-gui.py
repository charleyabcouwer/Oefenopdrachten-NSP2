import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        # roep de __init__() aan van de parent class
        super().__init__()

        # elk QMainWindow moet een central widget hebben
        # hierbinnen maak je een layout en hang je andere widgets
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # geef de central widget een verticale layout
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        # voeg geneste layouts en widgets toe
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)
        add_text_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_text_button)

        # Extra buttons
        add_hello_button = QtWidgets.QPushButton("Hello")
        hbox.addWidget(add_hello_button)

        # slots and signals
        clear_button.clicked.connect(self.textedit.clear)
        add_text_button.clicked.connect(self.add_text_button_clicked)
        add_hello_button.clicked.connect(self.add_hello_button_clicked)

    @Slot()
    def add_text_button_clicked(self):
        self.textedit.append("Boem")

    def add_hello_button_clicked(self):
        self.textedit.append("Hello, world!")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
