import os

from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from flashcard_widget import FlashCard


class QuestionWindow(QWidget):
    def __init__(self, main_window, change_to_main_window, deck):
        super().__init__()

        # Referencing the shared list
        self.deck = deck

        self.main_window = main_window
        self.change_to_main_window = change_to_main_window
        
        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Create QLineEdit, I need two
        self.question_box = QLineEdit(parent=self)
        self.question_box.setPlaceholderText("Enter a question")

        self.answer_box = QLineEdit(parent=self)
        self.answer_box.setPlaceholderText("Enter an answer")
        self.answer_box.returnPressed.connect(self.insert_card)

        self.deck_name_box = QLineEdit(parent=self)
        self.deck_name_box.setPlaceholderText("Enter a deck name")

        # Set fixed height for QLineEdit instances
        self.question_box.setFixedHeight(90)
        self.question_box.setFixedWidth(600)

        self.answer_box.setFixedHeight(90)
        self.answer_box.setFixedWidth(600)

        self.deck_name_box.setFixedHeight(50)
        self.deck_name_box.setFixedWidth(200)


        # Might want to add some font and font sizing here:
        font = QFont()
        font.setPointSize(12)
        self.question_box.setFont(font)
        self.answer_box.setFont(font)
        self.deck_name_box.setFont(font)

        # Create my Buttons
        self.open_existing_btn = QPushButton("Open existing")
        self.insert_card_btn  = QPushButton("Insert card")
        self.finish_btn = QPushButton("Finish deck")

        # Button functionality
        self.open_existing_btn.clicked.connect(change_to_main_window)
        self.open_existing_btn.clicked.connect(self.open_existing_deck)
        self.finish_btn.clicked.connect(self.finish_deck_creation)
        self.insert_card_btn.clicked.connect(self.insert_card)

        # Add buttons to HBox
        h_box = QHBoxLayout()
        h_box.addWidget(self.open_existing_btn)
        h_box.addWidget(self.insert_card_btn)
        h_box.addWidget(self.finish_btn)
        h_box.setSpacing(200)

        # Form layout for QLineEdits
        q_layout = QFormLayout()
        q_layout.addRow("Name of Deck:", self.deck_name_box)
        q_layout.addRow("Question:", self.question_box)
        q_layout.addRow("Answer:", self.answer_box)

        # Center the form layout horizontally
        hq_box = QHBoxLayout()
        hq_box.addStretch()
        hq_box.addLayout(q_layout)
        hq_box.addStretch()

        # Main vertical layout
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(hq_box)
        v_box.addStretch()
        v_box.addLayout(h_box)

        v_box.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.setLayout(v_box)

    # Methods for my buttons
    def open_existing_deck(self):
            print("Opening from Question window")
            self.main_window.open_existing_deck()
    
    
    def insert_card(self):
        if not self.question_box.text() or not self.answer_box.text() or not self.deck_name_box.text():
            QMessageBox.warning(self, "Warning", "Onen or more input fields are empty!")
        else:
            print("Question Inserted")
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # NOTE: This only works for my computer. Delete so that it works in current directory
            deck_directory = "decks"
            deck_name = self.deck_name_box.text() + ".txt"

            file_path = os.path.join(current_directory, deck_directory, deck_name)

            if not os.path.exists(os.path.join(current_directory, deck_directory)):
                os.makedirs(os.path.join(current_directory, deck_directory))

            if os.path.exists(file_path):
                self.collect_data(file_path, 'a')
            else:
                self.collect_data(file_path, 'w')

        # self.question_box.clear()
        # self.answer_box.clear()

    # Extracts text and adds them to a file in a specific format: Q^A
    def collect_data(self, file_path, mode):
        question_text = self.question_box.text()
        answer_text = self.answer_box.text()

        card_format = question_text + "^" + answer_text

        with open(file_path, mode) as file:
            file.write(card_format + '\n')

    # TODO: Change to main_window, but load the created deck        
    def finish_deck_creation(self):
            
        if self.deck_name_box.text():
            print("Deck has been created!")
            self.deck.clear()

            current_directory = os.path.dirname(os.path.abspath(__file__))

            # NOTE: Tis only works in my computer. delete so that it works only in current directory
            deck_directory = "decks"
            deck_name = self.deck_name_box.text() + ".txt"

            current_deck_path = os.path.join(current_directory, deck_directory, deck_name)
            print(current_deck_path)

            with open(current_deck_path, 'r') as file:
                for line in file:
                    parts = line.strip().split('^', 1)  
                    if len(parts) == 2:
                        question, answer = parts
                        self.deck.append((question, answer))

            # deck has been updted, remove old widget and delete
            self.main_window.vertical_box.removeWidget(self.main_window.flashcard)
            self.main_window.flashcard.deleteLater()

            # Create new instance of a flashcard and set it in the Vbox
            self.main_window.flashcard = FlashCard()
            self.main_window.vertical_box.insertWidget(1, self.main_window.flashcard)

            print("Deck:", self.deck)
            #TODO: Check if this works:
            self.main_window.populate_qbox()
            self.deck_name_box.clear()
            self.question_box.clear()
            self.answer_box.clear()
            self.change_to_main_window()
        else:
            QMessageBox.warning(self, "Warning", "Deck name is missing")


        

        

# For debugging puposes
# NOTE: Need to make sure QApplication is imported first
# app = QApplication([])
# main_window = QuestionWindow()
# main_window.show()
# app.exec()
