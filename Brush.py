#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        width =90
        height=60

        #--- Используем в drawBrushes(self, qp)
        self.brush_patterns = [[Qt.SolidPattern, 10, 15, width, height],
                               [Qt.Dense1Pattern, 130, 15, width, height],
                               [Qt.Dense2Pattern, 250, 15, width, height],

                               #[Qt.Dense3Pattern, 10, 105, width, height],

                               [Qt.DiagCrossPattern, 10, 105, width, height],
                               [Qt.Dense5Pattern, 130, 105, width, height],
                               [Qt.Dense6Pattern, 250, 105, width, height],

                               [Qt.HorPattern, 10, 195, width, height],
                               [Qt.VerPattern, 130, 195, width, height],
                               [Qt.BDiagPattern, 250, 195, width, height]
                              ]

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()



    def drawBrushes(self, qp):

        for exempl in self.brush_patterns:
            brush = QBrush(exempl[0])
            qp.setBrush(brush)
            qp.drawRect(exempl[1],exempl[2],exempl[3],exempl[4])

        #--- Перелопатить сие безобразие:
        """
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)
        """

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())