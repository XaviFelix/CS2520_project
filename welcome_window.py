# TODO: I need to add styling and choose a different font
# TODO: Add Buttons
# TODO: Add behavior to the buttons
#       1) Open Existing Button
#            - Open file exlporer to find file
#            - Make sure to add exception handling for this
#       2) Populate to dictionary or list of Tuples
#       3) Then switch to the second window (create this class)

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from layout_colorwidget import Color 


class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

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
        horizontal_box.addWidget(Color("Green"))
        horizontal_box.addWidget(Color("Red"))

        # Add HBox (that contains buttons) to VBox
        vertical_box.addLayout(horizontal_box)

        # Manages the Stacked Layout
        widget = QWidget()
        widget.setLayout(vertical_box)
        self.setCentralWidget(widget)



# Create the app for debugging purposes
app = QApplication(sys.argv)

# Create the MainWindow instance and show
window = WelcomeWindow()
window.show()


app.exec()