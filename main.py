import sys
from random import randrange

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Form(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        radius = randrange(1, 200)
        x = randrange(radius, 501 - radius)
        y = randrange(radius, 501 - radius)

        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor('yellow'))
        qp.drawEllipse(x, y, radius, radius)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())