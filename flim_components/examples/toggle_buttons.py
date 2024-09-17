
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from flim_components.components.buttons.toggle_button import ToggleButton


class ToggleButtonsExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toggle Button Example")
        self.setStyleSheet("background-color: #121212;")  
        self.setFixedSize(400, 400) 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 
  
        toggleables = [
            {"text": "Button 1", "key": "btn1", "active": True},
            {"text": "Button 2", "key": "btn2", "active": False},
        ]

        toggle_button = ToggleButton(
            toggleables=toggleables,
        )

        layout.addWidget(toggle_button)
        layout.setContentsMargins(10,10,10,10)
        self.setLayout(layout)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToggleButtonsExampleWindow()
    window.show()
    app.exec()
