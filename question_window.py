import os

from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy, QMessageBox
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

class QuestionWindow(QWidget):
    def __init__(self, main_window, change_to_main_window, deck):
        super().__init__()

        # Referencing the shared list
        self.deck = deck

        self.main_window = main_window
        
        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Create QLineEdit, I need two
        self.question_box = QLineEdit(parent=self)
        self.answer_box = QLineEdit(parent=self)
        self.answer_box.returnPressed.connect(self.insert_card)
        self.deck_name_box = QLineEdit(parent=self)

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

        # TODO: Finish the funcitonality of this:
        # self.finish_deck_creation.connect(change_to_main_window)
        self.finish_btn.clicked.connect(self.finish_deck_creation)

        self.insert_card_btn.clicked.connect(self.insert_card)

        # Add buttons to HBox
        h_box = QHBoxLayout()
        h_box.addWidget(self.open_existing_btn)
        h_box.addWidget(self.insert_card_btn)
        h_box.addWidget(self.finish_btn)
        h_box.setSpacing(200)

        # Create QFormLayout for my QEditLine instances
        q_layout = QFormLayout()
        q_layout.addRow("Name of Deck:", self.deck_name_box)
        q_layout.addRow("Question:", self.question_box)
        q_layout.addRow("Answer:", self.answer_box)

        # Create an outer HBoxLayout to center the QFormLayout horizontally
        h_center_layout = QHBoxLayout()
        h_center_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        h_center_layout.addLayout(q_layout)
        h_center_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Create an outer VBoxLayout to center the QFormLayout vertically
        v_center_layout = QVBoxLayout()
        v_center_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        v_center_layout.addLayout(h_center_layout)
        v_center_layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Creating a layout for this widget and add everything here:
        main_v_box = QVBoxLayout()
        main_v_box.addLayout(v_center_layout)
        main_v_box.addLayout(h_box)

        self.setLayout(main_v_box)

    # Methods for my buttons
    def open_existing_deck(self):
            print("Opening from Question window")
            self.main_window.open_existing_deck()
    
    # TODO: If boxes don't have text then don't add to the file!
    # Fix this
    def insert_card(self):

        if not self.question_box.text() or not self.answer_box.text() or not self.deck_name_box:
            QMessageBox.warning(self, "Warning", "Onen or more input fields are empty!")
        else:
            print("Question Inserted")
            current_directory = os.path.dirname(os.path.abspath(__file__))
            deck_directory = "decks"
            deck_name = self.deck_name_box.text() + ".txt"

            file_path = os.path.join(current_directory, deck_directory, deck_name)

            if not os.path.exists(os.path.join(current_directory, deck_directory)):
                os.makedirs(os.path.join(current_directory, deck_directory))

            if os.path.exists(file_path):
                self.collect_data(file_path, 'a')
            else:
                self.collect_data(file_path, 'w')

        self.question_box.clear()
        self.answer_box.clear()

    def collect_data(self, file_path, mode):
        question_text = self.question_box.text()
        answer_text = self.answer_box.text()

        card_format = question_text + "^" + answer_text

        with open(file_path, mode) as file:
            file.write(card_format + '\n')
                
    def finish_deck_creation(self):
        print("Deck has been created!")
        

# For debugging puposes
# NOTE: Need to make sure QApplication is imported first
# app = QApplication([])
# main_window = QuestionWindow()
# main_window.show()
# app.exec()
