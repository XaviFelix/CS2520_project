from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

class QuestionWindow(QWidget):
    def __init__(self):
        super().__init__()

        #For now I will use a local list for testing, change to the referenced list
        #self.my_list = []
        
        # Set the fixed sizing of the MainWindow
        self.setFixedSize(QSize(700, 400))

        # Create QLineEdit, I need two
        self.question_box = QLineEdit(parent=self)
        self.answer_box = QLineEdit(parent=self)

        # Set fixed height for QLineEdit instances
        self.question_box.setFixedHeight(90)
        self.question_box.setFixedWidth(620)

        self.answer_box.setFixedHeight(90)
        self.answer_box.setFixedWidth(620)


        # Might want to add some font and font sizing here:
        font = QFont()
        font.setPointSize(12)
        self.question_box.setFont(font)
        self.answer_box.setFont(font)

        # Create my Buttons
        self.open_existing_btn = QPushButton("Open existing deck")
        self.next_question_btn  = QPushButton("Next Question")
        self.finish_btn = QPushButton("Finish")

        # Add buttons to HBox
        h_box = QHBoxLayout()
        h_box.addWidget(self.open_existing_btn)
        h_box.addWidget(self.next_question_btn)
        h_box.addWidget(self.finish_btn)
        h_box.setSpacing(200)

        # Create QFormLayout for my QEditLine instances
        q_layout = QFormLayout()
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
        

# For debugging puposes
# NOTE: Need to make sure QApplication is imported first
app = QApplication([])
main_window = QuestionWindow()
main_window.show()
app.exec()
