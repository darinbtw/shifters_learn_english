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
        self.label = QLabel('Вам нужно писать перевод к слову, которую вам предоставят!')
        layout.addWidget(self.label)

        self.label_start = QLabel('Начинаем?')
        layout.addWidget(self.label_start)

        self.check_button = QPushButton('Начать игру!')
        self.check_button.clicked.connect(self.start_game)
        layout.addWidget(self.check_button)

        central_widget.setLayout(layout)

    def start_game(self):
        New_Widged = QWidget()
        self.setCentralWidget(New_Widged)
        self.setWindowTitle('Старт игры!')
        
        layout_start = QVBoxLayout()

        self.Starts_words = QLabel('Тут должен быть текст заготовленный под какое-то слове')
        layout_start.addWidget(self.Starts_words)
        
        self.input_text = QLineEdit()
        
        self.input_text.setPlaceholderText('Введите перевод текста:')
        layout_start.addWidget(self.input_text)

        self.

        New_Widged.setLayout(layout_start)


    def generated_english_words(self):
         with open('words.txt', 'r', encoding='UTF-8') as file:
              words = file.read()
              print(words)

def starts():
        app = QApplication(sys.argv)
        app.setStyle('WindowsXP') #WindowsXP, Windows, Fussion, WindowsVista
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    starts()