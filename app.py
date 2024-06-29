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
        self.label_start = QLabel('Выберите режим:')
        layout.addWidget(self.label_start)

        #Создаётся кнопка после которой нас перебрасывает на новое окно
        self.check_button = QPushButton('С Английского на Русский')
        self.check_button.clicked.connect(self.start_game)
        layout.addWidget(self.check_button)

        self.russian_game = QPushButton('С Русского на Английский')
        self.russian_game.clicked.connect(self.russian_game_start)
        layout.addWidget(self.russian_game)

        #Отображает все вставки
        central_widget.setLayout(layout)

    def russian_game_start(self):
        self.new_widged = QWidget()
        self.setCentralWidget(self.new_widged)
        self.setWindowTitle('С Русского на Английский')

        self.layout_rus = QVBoxLayout()

        self.load_new_word_rus()

        self.input_text_user = QLineEdit()
        self.input_text_user.setPlaceholderText('Впишите сюда перевод слова')
        self.layout_rus.addWidget(self.input_text_user)

        self.button_click_user = QPushButton('Отправить')
        self.button_click_user.clicked.connect(self.check_translate_rus)
        self.layout_rus.addWidget(self.button_click_user)
        
        self.back_to_main_menu1 = QPushButton('Вернутся в меню')
        self.back_to_main_menu1.clicked.connect(self.main_menu)
        self.layout_rus.addWidget(self.back_to_main_menu1)
        
        self.russian_help = QPushButton('Показать овтет?')
        self.russian_help.clicked.connect(self.help_russian)
        self.layout_rus.addWidget(self.russian_help)
        
        self.new_widged.setLayout(self.layout_rus)
        
    def help_russian(self):
        if hasattr(self, 'help_russian1'):
            self.help_russian1.setText(f'Показать ответ {self.correct_translition_rus}')
            self.show()
        else:
            self.help_russian1 = QLabel(f'Показать ответ {self.correct_translition_rus}')
            self.layout_rus.addWidget(self.help_russian1)
            
    def check_translate_rus(self):
        user_input_text = self.input_text_user.text()

        if user_input_text.lower() == self.correct_translition_rus.lower():
            QMessageBox.information(self, 'Результат', 'Вы правильно перевели')
            self.load_new_word_rus()
        else:
            QMessageBox.warning(self, 'Результат', 'Вы не правильно перевели!')

    def start_game(self):
        #Создаём новое окно
        self.new_Widged = QWidget()
        self.setCentralWidget(self.new_Widged)
        self.setWindowTitle('С Английского на Русский')
        
        #Будет добавлять вставки, текст и т.д
        self.layout_start = QVBoxLayout()

        #Выводим слово которое нужно перевести
        self.load_new_words()
        
        #Создаётся строчка для ввода пользователя
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText('Введите перевод слова')
        self.layout_start.addWidget(self.input_text)

        #Кнопка после которой идёт проверка на правильность перевода
        self.button_check = QPushButton('Проверить перевод')
        self.button_check.clicked.connect(self.check_translate)
        self.layout_start.addWidget(self.button_check)

        #Кнопка которая возвращает нас в главное меню
        self.back_main_menu = QPushButton('Вернуться обратно в меню')
        self.back_main_menu.clicked.connect(self.main_menu)
        self.layout_start.addWidget(self.back_main_menu)

        self.helping = QPushButton('Показать ответ?')
        self.helping.clicked.connect(self.helps)
        self.layout_start.addWidget(self.helping)
        
        #Отображает все вставки
        self.new_Widged.setLayout(self.layout_start)

    #Функция которая проверяет ввёдное слово пользователем на правильность перевода
    def check_translate(self):
        user_input = self.input_text.text()
        if user_input.lower() == self.correct_translition.lower():
             QMessageBox.information(self, 'Результат', 'Вы правильно перевели')
             self.load_new_words()
        else:
             QMessageBox.warning(self, 'Результат', 'Вы неправильно перевели, попробуйте ещё раз!')

    def load_new_words(self):
        self.english_word, self.correct_translition = self.generated_english_words()
        if hasattr(self, 'starts_words'):
            self.starts_words.setText(f'Переведите слово: {self.english_word}')
        else:
            self.starts_words = QLabel(f'Переведите слово: {self.english_word}')
            self.layout_start.addWidget(self.starts_words)

    #Генерирует слово из words.txt
    def generated_english_words(self):
         with open('words.txt', 'r', encoding='UTF-8') as file:
              lines = file.readlines()
              random_line = choice(lines).strip()
              english_word, russian_word = random_line.split(' - ')
              return english_word, russian_word
    
    def load_new_word_rus(self):
        self.russian_word, self.correct_translition_rus = self.generated_russian_words()
        if hasattr(self, 'starts_words_rus'):
            self.starts_words_rus.setText(f'Переведите слово: {self.russian_word}')
        else:
            self.starts_words_rus = QLabel(f'Переведите слово: {self.russian_word}')
            self.layout_rus.addWidget(self.starts_words_rus)
            
    def generated_russian_words(self):
        with open('russian_words.txt', 'r', encoding='UTF-8') as file1:
            line1 = file1.readlines()
            random_line1 = choice(line1).strip()
            russian_words1, english_words1 = random_line1.split(' - ')
            return russian_words1,english_words1
    
    def helps(self):
        if hasattr(self, 'help'):
            self.help.setText(f'Правильный перевод: {self.correct_translition}')
            self.help.show()
        else:
            self.help = QLabel(f'Правильный перевод: {self.correct_translition}')
            self.layout_start.addWidget(self.help)

#Запуск всего проекта
def starts():
        app = QApplication(sys.argv)
        app.setStyle('Fussion') #WindowsXP, Windows, Fussion, WindowsVista
        window = MainWindow()   
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    starts()