# TODO: I need to add styling and choose a different font
# TODO: Now I need add functionality to the buttons
# TODO: Add behavior to the buttons
#       1) Open Existing Button
#            - Open file exlporer to find file
#            - Make sure to add exception handling for this
#       2) Populate to dictionary or list of Tuples
#       3) Then switch to the second window (create this class)

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton
# from place_holder import Color 


class WelcomeWindow(QWidget):
    def __init__(self, switch_window):
        super().__init__()

        # Welcome message, set the alignment of it as well
        self.welcome_message = QLabel("Welcome to the Nebula FlashCard app")
        self.welcome_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Create the stacked layout
        vertical_box = QVBoxLayout()
        horizontal_box = QHBoxLayout()

        # Add welcome message to the VBox
        vertical_box.addWidget(self.welcome_message)

        # Add Color instances as place holders for now (should be buttons)
        open_existing_btn = QPushButton("Open existing deck")
        create_new_btn = QPushButton("Create new deck")

        horizontal_box.addWidget(open_existing_btn)
        horizontal_box.addWidget(create_new_btn)
        horizontal_box.setSpacing(200)

        # Add HBox (that contains buttons) to VBox
        vertical_box.addLayout(horizontal_box)

        # If open existing is clicked then it finds file and changes window:
        open_existing_btn.clicked.connect(switch_window)
        open_existing_btn.clicked.connect(self.open_existing_deck)

        # If create new is clicked then it changes window and creates a new deck:
        create_new_btn.clicked.connect(self.create_new_deck)

        self.setLayout(vertical_box)

    def open_existing_deck(self):
        print("Opening existing deck")

        

    def create_new_deck(self):
        print("Creating new deck")
