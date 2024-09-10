import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from components.buttons.select_buttons import SelectButtonGroup

class SelectButtonGroupExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Button Group Example")
        self.setStyleSheet("background-color: #121212;")  
        self.setFixedSize(1000, 400) 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        button_configs = [
            ("Selectable Button 1", "btn1", None),
            ("Selectable Button 2", "btn2", None),
            ("Selectable Button 3", "btn3", None),
            ("Selectable Button 4", "btn4", None),
            ("Selectable Button 5", "btn5", None),
            ("Selectable Button 6", "btn6", None),
            ("Selectable Button 7", "btn7", None),
            ("Selectable Button 8", "btn8", None),
        ]

        select_button_group = SelectButtonGroup(
            button_configs=button_configs,
            layout_type="horizontal",
            layout_options={"spacing": 10},
            default_selected="btn1",
        )

        layout.addWidget(select_button_group)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectButtonGroupExampleWindow()
    window.show()
    app.exec()
