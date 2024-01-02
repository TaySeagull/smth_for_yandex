import copy
from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication



class Random_Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Гит_и_скитлстрянка.ui', self)  # Загружаем дизайн
        self.draw = None
        self.pushButton.clicked.connect(self.change_event)

    def change_event(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setPen(QColor(252, 227, 3))
        w, h = [randint(10, 100) for i in range(2)]
        qp.drawEllipse(200, 100, w, h)
        self.draw = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Random_Circle()
    ex.show()
    sys.exit(app.exec_())
