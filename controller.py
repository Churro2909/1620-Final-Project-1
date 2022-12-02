from PyQt5.QtWidgets import *
from view import *
from methods import *

# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_exponent.clicked.connect(lambda: self.calculate_exponents())
        self.pushButton_cat_ears.clicked.connect(lambda: self.calculate_cat_ears())
        self.pushButton_alien_ears.clicked.connect(lambda: self.calculate_alien_ears())

    def calculate_exponents(self):
        try:
            x = float(self.lineEdit_exponent_base.text())
            y = float(self.lineEdit_exponent.text())
            answer = powers(x, y)
            self.label_output.setText(f"The answer is {answer}")
        except ValueError:
            self.label_output.setText("Both inputs must be numbers")

    def calculate_cat_ears(self):
        try:
            x = float(self.lineEdit_cat_ears.text())
            answer = cat_ears(x)
            if answer == -1:
                self.label_output.setText(f"Input must be whole numbers! You can't have half of a cat.")
            else:
                self.label_output.setText(f"For {x} cats, there are {answer} cat ears!")
        except ValueError:
            self.label_output.setText("The input must be numbers")

    def calculate_alien_ears(self):
        try:
            x = float(self.lineEdit_alien_ears.text())
            answer = alien_ears(x)
            if answer == -1:
                self.label_output.setText(f"Input must be whole numbers! You can't have half of a alien...right?")
            else:
                self.label_output.setText(f"For {x} aliens, there are {answer} alien ears!")
        except ValueError:
            self.label_output.setText("The input must be numbers")


