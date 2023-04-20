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
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

import str_common as strc

'''
strc.Print_table(dir(QWidget), 6, 24)
strc.Print_table(dir(QApplication), 6, 24)
'''

def selfdoc():
    print(
        ''' 
           === QT fo python tutorial ==============================================  

           Первая работа: "Основная структура приложения QT: создание окон"

           Вторая работа: Подкласс QMainWindow для настройки главного окна приложения

           Третья работа: слот the_button_was_clicked, сигнал clicked от QPushButton:

           Самодокументируемый текст прораммы не требует подробных комментариев

           =======================================================================
        '''
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT_tutorial")

        self.button_is_checked = True

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        '''
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        '''
        # В Released нет сигнала, которым отправляется текущее сосояние
        # checked, поэтому проверяем состояние checked («Нажата») в
        # нажатом обработчике the_button_was_released()

        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        # Размеры
        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)
        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

        if(self.button_is_checked):
            self.setFixedSize(QSize(400, 300))
        else:
            self.setFixedSize(QSize(800, 600))

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


def main():

    print()

    selfdoc()

    strc.zagolovok("Первая работа: Основная структура приложения QT")

    # Приложению нужен один (и только один) экземпляр QApplication.
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
    # Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
    app = QApplication(sys.argv)

    strc.zagolovok("Вторая работа: Создание и настройка окна QT")
    '''
    # Создаём виджет Qt — окно windw. Важно: окно по умолчанию скрыто. Поэтоиу надо show()
    wind = QWidget()
    wind.show()

    # Еще виджет Qt — окно win.
    win = QPushButton("Push Me")
    win.show()
    '''

    # можно сразу уст контейнер для окон, предварительно создав свой класс
    window = MainWindow()
    window.show()





    # Запускаем цикл событий.
    app.exec()

if __name__ == "__main__":
    main()
