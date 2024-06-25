from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox, QMainWindow, QLineEdit
import sys
from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle('Учёба английскому языку!')
        self.main_menu()

    def main_menu(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #Текст с небольшим объяснением того, что нужно делать
        layout = QVBoxLayout()
        self.label = QLabel('Вам нужно писать перевод к слову, которую вам предоставят!')
        layout.addWidget(self.label)

        #Создаётся другой текст с вопросом
        self.label_start = QLabel('Начинаем?')
        layout.addWidget(self.label_start)

        #Создаётся кнопка после которой нас перебрасывает на новое окно
        self.check_button = QPushButton('Начать игру!')
        self.check_button.clicked.connect(self.start_game)
        layout.addWidget(self.check_button)

        #Отображает все вставки
        central_widget.setLayout(layout)

    def start_game(self):
        #Создаём новое окно
        New_Widged = QWidget()
        self.setCentralWidget(New_Widged)
        self.setWindowTitle('Старт игры!')
        
        #Будет добавлять вставки, текст и т.д
        layout_start = QVBoxLayout()

        #Выводим слово которое нужно перевести
        self.english_word, self.correct_translition = self.generated_english_words()
        self.Starts_words = QLabel(f'Переведите слово: {self.english_word}')
        layout_start.addWidget(self.Starts_words)
        
        #Создаётся строчка для ввода пользователя
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText('Введите перевод слова')
        layout_start.addWidget(self.input_text)

        #Кнопка после которой идёт проверка на правильность перевода
        self.button_check = QPushButton('Проверить перевод')
        self.button_check.clicked.connect(self.check_translate)
        layout_start.addWidget(self.button_check)

        #Кнопка которая возвращает нас в главное меню
        self.back_main_menu = QPushButton('Вернуться обратно в меню')
        self.back_main_menu.clicked.connect(self.main_menu)
        layout_start.addWidget(self.back_main_menu)
        
        #Отображает все вставки
        New_Widged.setLayout(layout_start)

    #Функция которая проверяет ввёдное слово пользователем на правильность перевода
    def check_translate(self):
        user_input = self.input_text.text()
        if user_input.lower() == self.correct_translition.lower():
             QMessageBox.information(self, 'Результат', 'Вы правильно перевели')
        else:
             QMessageBox.warning(self, 'Результат', 'Вы неправильно перевели, попробуйте ещё раз!')

    #Генерирует слово из words.txt
    def generated_english_words(self):
         with open('words.txt', 'r', encoding='UTF-8') as file:
              lines = file.readlines()
              random_line = choice(lines).strip()
              english_word, russian_word = random_line.split(' - ')
              return english_word, russian_word

#Запуск всего проекта
def starts():
        app = QApplication(sys.argv)
        app.setStyle('WindowsXP') #WindowsXP, Windows, Fussion, WindowsVista
        window = MainWindow()   
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    starts()