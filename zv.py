from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QPushButton
from random import randint

app = QApplication([])
win = QWidget()

win.setWindowTitle('Визначник переможця')
win.resize(400, 200)
win.move(100, 100)

text = QLabel(win)
text.setText('Натисніть, щоб дізнатися переможця')
text.move(70, 10)

text2 = QLabel(win)
text2.setText("?")
text2.move(190, 70)

button = QPushButton(win)
button.setText('Згенерувати')
button.move(140, 130)
text.setStyleSheet('color:red; font-size:30px')
win.setStyleSheet('background:white')
def show_win():
    num = randint(1, 100)
    text2.setText(str(num))
    text.setText('Переможець:')
button.clicked.connect(show_win)


win.show()
app.exec_()