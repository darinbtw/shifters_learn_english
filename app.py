from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from random import choice

#Запуск своего проекта начинается здесь
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('main.png'))
        #создаём название окна
        self.setWindowTitle('Учёба английскому языку!')
        #Запускаем окно с главным меню
        self.main_menu()

    #главное меню
    def main_menu(self):
        #Создаём окно
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Создаём переменную которая отвечает за вставки в окно 
        layout = QVBoxLayout()
        
        #Отображаем заплонированный текст
        self.label = QLabel('Вам нужно писать перевод к слову, которую вам предоставят!')
        layout.addWidget(self.label)

        self.label_start = QLabel('Выберите режим:')
        layout.addWidget(self.label_start)

        #Тут мы создаём кнопку с текстом и куда это будет направлять
        self.check_button = QPushButton('С Английского на Русский')
        self.check_button.clicked.connect(self.start_game)
        layout.addWidget(self.check_button)

        self.russian_game = QPushButton('С Русского на Английский')
        self.russian_game.clicked.connect(self.russian_game_start)
        layout.addWidget(self.russian_game)

        self.english_word_add = QPushButton('Добавить свои английски слова')
        self.english_word_add.clicked.connect(self.rule_forEnglish_words)
        layout.addWidget(self.english_word_add)

        self.russian_words_add = QPushButton('Добавить свои русские слова')
        self.russian_words_add.clicked.connect(self.rule_forRussian_words)
        layout.addWidget(self.russian_words_add)

        #В окне мы создаём виджеты за которые отвечает переменная layout
        central_widget.setLayout(layout)

    #Первый режим игры с Русского на Английский
    def russian_game_start(self):
        self.new_widget = QWidget()
        self.setCentralWidget(self.new_widget)
        self.setWindowTitle('С Русского на Английский')

        self.layout_rus = QVBoxLayout()

        self.starts_words_rus = QLabel()
        self.layout_rus.addWidget(self.starts_words_rus)

        self.load_new_word_rus()

        #С помощью QlineEdit создаём поле для ввода
        self.input_text_user = QLineEdit()
        self.input_text_user.setPlaceholderText('Впишите сюда перевод слова')
        self.layout_rus.addWidget(self.input_text_user)

        self.button_click_user = QPushButton('Отправить')
        self.button_click_user.clicked.connect(self.check_translate_rus)
        self.layout_rus.addWidget(self.button_click_user)

        self.back_to_main_menu1 = QPushButton('Вернутся в меню')
        self.back_to_main_menu1.clicked.connect(self.main_menu)
        self.layout_rus.addWidget(self.back_to_main_menu1)

        self.russian_help = QPushButton('Показать ответ?')
        self.russian_help.clicked.connect(self.help_russian)
        self.layout_rus.addWidget(self.russian_help)

        self.new_widget.setLayout(self.layout_rus)

    #Загрузить новые слова
    def rule_forRussian_words(self):
        self.new_widget4 = QWidget()
        self.setCentralWidget(self.new_widget4)
        self.setWindowTitle('Добавить новое русское слово')

        self.layout_rule = QVBoxLayout()

        self.rule_rus = QLabel('''Как же добавить новое английское слово? Вам нужно создать txt файл,
в котором будет <Русское слово> <-> тире и <Перевод на английское это слово>
Пример: яблоко - apple''')
        self.layout_rule.addWidget(self.rule_rus)

        self.add_new_words_rus = QPushButton('Добавить')
        self.add_new_words_rus.clicked.connect(self.add_new_word_for_rus)
        self.layout_rule.addWidget(self.add_new_words_rus)

        self.back_to_menu_rus = QPushButton('Вернуться в главное меню')
        self.back_to_menu_rus.clicked.connect(self.main_menu)
        self.layout_rule.addWidget(self.back_to_menu_rus)

        self.new_widget4.setLayout(self.layout_rule)
    #Создаётся загрузчик файла
    def add_new_word_for_rus(self):
        sus = QFileDialog.Options()
        file_name1, _ = QFileDialog.getOpenFileName(self, 'выберите файл', '', 'Text Files (*.txt);; All Files(*)', options=sus)
        if file_name1:
            self.adding_file(file_name1)

    #Добавляем в слова из загрзженного txt файла
    def adding_file(self, file_name1):
        try:    
            with open (file_name1, 'r', encoding='UTF-8')as b:
                line = b.readline()
                with open('russian_words.txt', 'a', encoding='UTF-8') as file1:
                    file1.write(line.strip() + '\n')
            QMessageBox.information(self, 'Успешно', 'Слово добавленно!')        
        except Exception as f:
            QMessageBox.warning(self, 'Ошибка', f'Не удалось добавить слово, {f}')

    def rule_forEnglish_words(self):
        self.new_widget3 = QWidget()
        self.setCentralWidget(self.new_widget3)
        self.setWindowTitle('Добавить новое английское слово')

        self.layout2 = QVBoxLayout()

        self.guide = QLabel('''Как же добавить новое английское слово? Вам нужно создать txt файл,
в котором будет <Английское слово> <-> тире и <Перевод на русский это слово>
Пример: apple - яблоко''')
        self.layout2.addWidget(self.guide)

        self.open_file = QPushButton('Добавить файл')
        self.open_file.clicked.connect(self.open_file_dialog)
        self.layout2.addWidget(self.open_file)

        self.back_to_main_menu2 = QPushButton('Вернутся в главное меню')
        self.back_to_main_menu2.clicked.connect(self.main_menu)
        self.layout2.addWidget(self.back_to_main_menu2)

        self.new_widget3.setLayout(self.layout2)    

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name , _ = QFileDialog.getOpenFileName(self, 'Выберите файл','', 'Text Files (*.txt);;All Files(*)', options=options)
        if file_name:
            self.add_new_word(file_name)

    def add_new_word(self, file_name):
        try:
            with open(file_name, 'r', encoding='UTF-8') as file:
                lines = file.readline()
                with open('english_words.txt', 'a', encoding='UTF-8') as english_word:
                    english_word.write(lines.strip() + '\n')
            QMessageBox.information(self, 'Успех', 'Слова успешны добавлены')
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'Не удалось добавить слова: {e}')

    #Здесь отображаем ответы
    def help_russian(self):
        if hasattr(self, 'help_russian1'):
            self.help_russian1.setText(f'Ответ: {self.correct_translition_rus}')
        else:
            self.help_russian1 = QLabel(f'Ответ: {self.correct_translition_rus}')
            self.layout_rus.addWidget(self.help_russian1)

    #Проверяем правильный ли тут переводы и если правильно то загружаем новое слово
    def check_translate_rus(self):
        user_input_text = self.input_text_user.text()

        if user_input_text.lower() == self.correct_translition_rus.lower():
            QMessageBox.information(self, 'Результат', 'Вы правильно перевели')
            self.load_new_word_rus()
        else:
            QMessageBox.warning(self, 'Результат', 'Вы не правильно перевели!')

    #второй режим
    def start_game(self):
        self.new_widget = QWidget()
        self.setCentralWidget(self.new_widget)
        self.setWindowTitle('С Английского на Русский')

        self.layout_start = QVBoxLayout()

        self.starts_words = QLabel()
        self.layout_start.addWidget(self.starts_words)

        self.load_new_words()

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText('Введите перевод слова')
        self.layout_start.addWidget(self.input_text)

        self.button_check = QPushButton('Проверить перевод')
        self.button_check.clicked.connect(self.check_translate)
        self.layout_start.addWidget(self.button_check)

        self.back_main_menu = QPushButton('Вернуться обратно в меню')
        self.back_main_menu.clicked.connect(self.main_menu)
        self.layout_start.addWidget(self.back_main_menu)

        self.helping = QPushButton('Показать ответ?')
        self.helping.clicked.connect(self.helps)
        self.layout_start.addWidget(self.helping)

        self.new_widget.setLayout(self.layout_start)

    def check_translate(self):
        user_input = self.input_text.text()
        if user_input.lower() == self.correct_translition.lower():
            QMessageBox.information(self, 'Результат', 'Вы правильно перевели')
            self.load_new_words()
        else:
            QMessageBox.warning(self, 'Результат', 'Вы неправильно перевели, попробуйте ещё раз!')
    
    #Загрузка новых слов для второго режима
    def load_new_words(self):
        self.english_word, self.correct_translition = self.generated_english_words()
        self.starts_words.setText(f'Переведите слово: {self.english_word}')

    def generated_english_words(self):
        with open('english_words.txt', 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            random_line = choice(lines).strip()
            english_word, russian_word = random_line.split(' - ')
            return english_word, russian_word
    
    #Загрузка новых слов для первого режима
    def load_new_word_rus(self):
        self.russian_word, self.correct_translition_rus = self.generated_russian_words()
        self.starts_words_rus.setText(f'Переведите слово: {self.russian_word}')

    #Загрузка новых слов для первого режима, когда вызывает функция load_new_word_rus
    def generated_russian_words(self):
        with open('russian_words.txt', 'r', encoding='UTF-8') as file1:
            lines = file1.readlines()
            random_line1 = choice(lines).strip()
            russian_words1, english_words1 = random_line1.split(' - ')
            return russian_words1, english_words1

    #показывает ответ для второго режима
    def helps(self):
        if hasattr(self, 'help'):
            self.help.setText(f'Ответ: {self.correct_translition}')
        else:
            self.help = QLabel(f'Ответ: {self.correct_translition}')
            self.layout_start.addWidget(self.help)

# Запуск всего проекта
def starts():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    starts()
