import sys
from random import randint

from PyQt6 import uic, QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.drawCircleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.drawCircleBtn.setObjectName("drawCircleBtn")
        self.gridLayout.addWidget(self.drawCircleBtn, 1, 0, 1, 1)
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Git и желтые окружности"))
        self.drawCircleBtn.setText(_translate("MainWindow", ""))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.do_paint = False
        self.drawCircleBtn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp: QPainter):
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setPen(color)
        qp.setBrush(color)
        x, y = self.canvas.width(), self.canvas.height()
        radius = randint(50, 200)
        qp.drawEllipse(150, 150, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())