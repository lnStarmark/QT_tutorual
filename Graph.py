#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("img\\dali.png")

        lbl = QLabel("<b>Dali</b>", self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(700, 700)
        self.setWindowTitle("Dali")
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())