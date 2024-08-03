from tkinter import filedialog

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QComboBox
from place_holder import Color
from flashcard_widget import FlashCard

class MainWindow(QWidget):
    def __init__(self, switch_to_question_window,  deck):
        super().__init__()

        # Create list and flashcard instance
        self.deck = deck
        self.current_index = 0
        self.flashcard = FlashCard()
        self.setWindowTitle("Nebula")

        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Set the layouts
        self.vertical_box = QVBoxLayout()
        horizontal_box_btns1 = QHBoxLayout()
        horizontal_box_btns2 = QHBoxLayout()

        # Create the buttons
        open_existing_btn = QPushButton("Open existing deck")
        create_new_btn = QPushButton("Create new deck")
        back_btn = QPushButton("Previous")
        next_btn = QPushButton("Next")

        # TODO: Create QBox
        self.qbox = QComboBox()
        self.qbox.setFixedWidth(200)
        self.populate_qbox()
        self.qbox.currentIndexChanged.connect(self.update_flashcard)


        # The button functions
        next_btn.clicked.connect(self.next_card)
        back_btn.clicked.connect(self.previous_card)
        open_existing_btn.clicked.connect(self.open_existing_deck)
        create_new_btn.clicked.connect(switch_to_question_window)


        # Add buttons to the first button layout
        horizontal_box_btns1.addWidget(open_existing_btn)
        horizontal_box_btns1.addWidget(self.qbox) # Test to see if this works
        horizontal_box_btns1.addWidget(create_new_btn)
        horizontal_box_btns1.setSpacing(100)

        # Add buttons to the second button layout
        horizontal_box_btns2.addWidget(back_btn)
        horizontal_box_btns2.addWidget(next_btn)
        horizontal_box_btns2.setSpacing(200)

        # Add the widgets to the Vbox
        self.vertical_box.addLayout(horizontal_box_btns1)
        self.vertical_box.addWidget(self.flashcard)
        self.vertical_box.addLayout(horizontal_box_btns2)

        self.setLayout(self.vertical_box)

    # increments the index in the list and changes the flashcard
    def next_card(self):
        print("next card")

        # Wraps index to the beginning
        self.current_index = (self.current_index + 1) % len(self.deck)
        self.flashcard.change_flashcard(self.deck[self.current_index][0], self.deck[self.current_index][1])

    # decrements the index in the list and changes the flashcard
    def previous_card(self):
        print("previous card")

        # Wraps index to the end
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.deck) - 1
                
        self.flashcard.change_flashcard(self.deck[self.current_index][0], self.deck[self.current_index][1])

    # NOTE: This pertains to the QComboBox
    def update_flashcard(self):
        self.current_index = self.qbox.currentIndex()
        self.flashcard.change_flashcard(self.deck[self.current_index][0], self.deck[self.current_index][1])



    # Open another deck of flashcards
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
        
        # deck has been updted, remove old widget and delete
        self.vertical_box.removeWidget(self.flashcard)
        self.flashcard.deleteLater()

        # Create new instance of a flashcard and set it in the Vbox
        self.flashcard = FlashCard()
        self.vertical_box.insertWidget(1, self.flashcard)
        
        # Print deck to console for debugging purposes
        print("Deck:", self.deck)
        self.populate_qbox() #TODO: Check to see if this works

    # TODO:
    # Grabs an instance of qbox and adds the elemetns from list to the box
    def populate_qbox(self):
        self.qbox.clear()
        for question in self.deck:
            self.qbox.addItem(question[0])






    