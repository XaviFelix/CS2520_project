from tkinter import filedialog

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton
from PyQt6.QtGui import QFont

class WelcomeWindow(QWidget):
    def __init__(self, main_window, switch_to_main, switch_to_question_window, deck):
        super().__init__()

        self.deck = deck

        self.main_window = main_window

        # Welcome message, set the alignment of it as well
        self.welcome_message = QLabel("Welcome to the Nebula FlashCard app")
        self.welcome_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Might want to add some font and font sizing here:
        font = QFont()
        font.setPointSize(12)
        self.welcome_message.setFont(font)


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

        # If open existing is clicked then it finds file and changes window: might need a bool
        open_existing_btn.clicked.connect(switch_to_main)
        open_existing_btn.clicked.connect(self.open_existing_deck)

        # If create new is clicked then it changes window and creates a new deck:
        create_new_btn.clicked.connect(switch_to_question_window)
        create_new_btn.clicked.connect(self.create_new_deck)

        self.setLayout(vertical_box)


    # TODO: continue testing, add exception handling later
    def open_existing_deck(self):
        print("Opening existing deck")
        self.deck.clear()
        # Accepted file types
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )

        # Open and read a selected txt file
        if file_path:
            with open(file_path, 'r') as file:

                # Line gets split to create a key,value pair for dictionary (deck)
                for line in file:
                    parts = line.strip().split('^', 1)  
                    if len(parts) == 2:
                        question, answer = parts
                        self.deck.append((question, answer))
        
        # Print deck to console for debugging purposes
        print("Deck:", self.deck)
        #TODO:
        self.main_window.populate_qbox()

    # TODO: Finish this method
    def create_new_deck(self):
        print("Creating new deck")


