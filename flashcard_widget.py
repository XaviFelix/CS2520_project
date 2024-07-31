from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class FlashCard(QWidget):
    def __init__(self, question="Deck has been loaded!", answer="Pess the next button"):
        super().__init__()

        self.question, self.answer = question, answer
        self.is_question = True 

        # Initialize the label
        self.label = QLabel(self.question)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set up layout for the FlashCard widget
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Event for mouse click
        self.label.mousePressEvent = self.flip_card

    # Shows either a question or an answer when clicked
    def flip_card(self, event):
        if self.is_question:
            self.label.setText(self.answer)
        else:
            self.label.setText(self.question)
        self.is_question = not self.is_question

    # Works as a setter to change the contents of the flashcard
    def change_flashcard(self, question, answer):
        self.question, self.answer = question, answer
        self.is_question = True
        self.label.setText(self.question)

