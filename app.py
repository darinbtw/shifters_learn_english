from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
app.setStyle('Fabion')
print(app)

button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()
button.clicked.connect(on_button_clicked)
button.show()

window = QWidget()
print(window)

layout = QVBoxLayout()
print(layout)
layout.addWidget(QPushButton('Главная страница'))
layout.addWidget(QPushButton('Мой GitHub аккаунт'))

window.setLayout(layout)
window.show()

app.exec_()


