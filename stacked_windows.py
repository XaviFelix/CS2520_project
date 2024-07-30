
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

from main_window import MainWindow
from welcome_window import WelcomeWindow

class StackedWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        # A shared dictionary
        my_deck  = []
        current_index = 0

        # Set up title and a fixed size
        self.setWindowTitle("Nebula Flash")
        self.setFixedSize(QSize(700,400))

        # Creating Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Creating StackedLayout
        self.stacked_layout = QStackedLayout()

        # My window instances
        self.welcome_window = WelcomeWindow(self.change_to_main_window, my_deck)
        self.main_window = MainWindow(my_deck)

        # Add my windows to the stack layout
        self.stacked_layout.addWidget(self.welcome_window)
        self.stacked_layout.addWidget(self.main_window)

        # Central widget layout
        central_layout = QVBoxLayout()
        central_layout.addLayout(self.stacked_layout)
        central_widget.setLayout(central_layout)

        # First window is welcome window
        self.stacked_layout.setCurrentWidget(self.welcome_window)

    # This will be changing the windows
    def change_to_main_window(self):
        self.stacked_layout.setCurrentWidget(self.main_window)

    def change_to_welcome_window(self):
        self.stacked_layout.setCurrentWidget(self.welcome_window)

        
        


app = QApplication([])
main_window = StackedWindows()
main_window.show()
app.exec()
