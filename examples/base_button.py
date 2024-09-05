import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt, QSize

from utils import resource_path
from components.buttons.base_button import BaseButton



class ButtonExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Example")
        self.setStyleSheet("background-color: #121212;")  
        self.setFixedSize(400, 400) 

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        button = BaseButton(
            text="Base Button", 
            width=150, 
            height=50, 
            bg_color_base="#1E90FF", 
            bg_color_hover="#4682B4", 
            bg_color_pressed="#4169E1"
        )
        
        icon= resource_path.resource_path("../assets/chart-icon.png")
        button_with_icon = BaseButton(
            text="Icon Button", 
            width=150, 
            height=50, 
            icon=icon, 
            icon_size=QSize(24, 24),
            bg_color_base="#DA1212", 
            bg_color_hover="#E23B3B", 
            bg_color_pressed="#B01010",
            border_color="#DA1212"
        )
        
        layout.addWidget(button)
        layout.addSpacing(10)
        layout.addWidget(button_with_icon)
        layout.setContentsMargins(10,10,10,10)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonExampleWindow()
    window.show()
    app.exec()
