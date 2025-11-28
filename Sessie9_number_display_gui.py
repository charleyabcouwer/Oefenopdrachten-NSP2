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

        # betekenis geven aan spinbox
        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setMaximum(28)
        self.spin_box.setMinimum(0)
        self.spin_box.setSingleStep(1)
        self.spin_box.setValue(28)

        # geef de central widget een verticale layout
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        # voeg geneste layouts en widgets toe
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)

        hbox.addWidget(self.spin_box)
        push_button = QtWidgets.QPushButton("Add value")
        hbox.addWidget(push_button)

        # slots and signals
        push_button.clicked.connect(self.push_button_clicked)

    @Slot()
    def push_button_clicked(self):
        self.textedit.append(str(self.spin_box.value()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
