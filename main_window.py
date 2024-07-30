import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from place_holder import Color

class MainWindow(QWidget):
    def __init__(self, deck):
        super().__init__()

        self.deck = deck

        self.setWindowTitle("My App")

        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Set the layout For this window
        vertical_box = QVBoxLayout()
        horizontal_box_btns1 = QHBoxLayout()
        horizontal_box_btns2 = QHBoxLayout()

        # Create the buttons
        open_existing_btn = QPushButton("Open existing deck")
        create_new_btn = QPushButton("Create new deck")
        back_btn = QPushButton("Back")
        next_btn = QPushButton("Next")

        # button functions
        # back_btn.clicked.connect()
        next_btn.clicked.connect(self.change_card)


        # Add buttons to the first button layout
        horizontal_box_btns1.addWidget(open_existing_btn)
        horizontal_box_btns1.addWidget(create_new_btn)
        horizontal_box_btns1.setSpacing(200)

        # Add buttons to the second button layout
        horizontal_box_btns2.addWidget(back_btn)
        horizontal_box_btns2.addWidget(next_btn)
        horizontal_box_btns2.setSpacing(200)

        # Add the widgets to the Vbox
        vertical_box.addLayout(horizontal_box_btns1)
        vertical_box.addWidget(Color("Red")) 
        vertical_box.addLayout(horizontal_box_btns2)

        self.setLayout(vertical_box)

    def change_card(self):
        print("changing card")





    