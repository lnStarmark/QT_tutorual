# -*- coding: utf-8 -*-
"""
Program QT_tutorial

Created on Tue Apr 19 23:32:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import str_common as strc

def selfdoc():
    print()
    print(
        ''' 
           === QT fo python tutorial 2 ============================================  

           Первая работа: "Подключение виджетов друг к другу напрямую"

           Самодокументируемый текст прораммы не требует подробных комментариев

           =======================================================================
        '''
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT_tutorial")

        self.label = QLabel("Click in this window")

        # Сигнал от виджета inpt напрямую подкл к слоту виджета label
        # т.к. в label есть встренный слот setText
        # потому не надо создавать внешнюю функцию и привязывать ее к виджету
        # ZB: для Label в документации смотрим:
        # https://doc.qt.io/qt-5/qlabel.html#public-slots

        self.inpt = QLineEdit()
        self.inpt.textChanged.connect(self.label.setText)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.inpt)
        self.layout.addWidget(self.label)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.container)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        print(f"mouseMoveEvent: {e}")

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self.ClearInput() )) #--- ???????
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    def ClearInput(self):
        self.inpt.clear()
def main():

    selfdoc()

    #--- create application -----------------------------
    app = QApplication(sys.argv)

    # уст контейнер для окон, из своего класса MainWindow
    window = MainWindow()
    window.show()

    #--- loop events ------------------------------------
    app.exec()

if __name__ == "__main__":
    main()
