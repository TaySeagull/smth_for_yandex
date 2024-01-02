import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from Гит_и_скитлстрянка import Ui_Form


class Random_Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.draw = None
        self.ui.pushButton.clicked.connect(self.change_event)

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
        qp.setPen(QColor(*[randint(0, 255) for _ in range(3)]))
        w, h = [randint(10, 100) for _ in range(2)]
        qp.drawEllipse(200, 100, w, h)
        self.draw = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Random_Circle()
    ex.show()
    sys.exit(app.exec_())

