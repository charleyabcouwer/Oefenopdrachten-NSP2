import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from Sessie9_number_display_gui import Ui_MainWindow


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_value_button.clicked.connect(self.add_value_button_clicked)

    @Slot()
    def add_value_button_clicked(self):
        self.ui.textedit.append("You've clicked the 'Add value' button")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
