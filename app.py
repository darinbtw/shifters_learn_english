from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox, QMainWindow, QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle('Учёба английскому!')

        layout = QVBoxLayout()

        self.label = QLabel('Вам нужно писать перевод к этому слову')
        layout.addWidget(self.label)

        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        self.check_button = QPushButton('Проверить перевод')
        self.check_button.clicked.connect(self.check_translation)
        layout.addWidget(self.check_button)

        central_widget.setLayout(layout)

    def check_translation(self):
        print('Вы написали перевод!')

def starts():
        app = QApplication(sys.argv)
        app.setStyle('WindowsXP') #WindowsXP, Windows, Fussion, WindowsVista
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    starts()