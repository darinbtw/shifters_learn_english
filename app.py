from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)
print(app)

window = QWidget()
print(window)

layout = QVBoxLayout()
print(layout)
layout.addWidget(QPushButton('Главная страница'))
layout.addWidget(QPushButton('Мой GitHub аккаунт'))

window.setLayout(layout)
window.show()

app.exec_()


