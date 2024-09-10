import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from components.buttons.tab_buttons import Tabs

class TabsExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabs Example")
        self.setStyleSheet("background-color: #121212;")  
        self.setFixedSize(400, 400) 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        tabs_config = [
            {"text": "Tab 1", "key": "tab1", "active": True},
            {"text": "Tab 2", "key": "tab2", "active": False},
            {"text": "Tab 3", "key": "tab3", "active": False},
        ]

        tabs = Tabs(
            tabs_config=tabs_config,
            enabled=True,
            visible=True,
            fg_color_active="#ffffff",
            fg_color_inactive="#ffffff",
            bg_color_active="#D01B1B",
            bg_color_inactive="transparent",
            border_color_active="transparent",
            border_color_inactive="#D01B1B",
            bg_color_hover="#E23B3B",
            bg_color_pressed="#B01010",
            bg_color_disabled="#cecece",
            border_color_disabled="#cecece",
            fg_color_disabled="#8c8b8b",
        )

        layout.addWidget(tabs)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

        tabs.active.connect(self.on_tab_active)

    def on_tab_active(self, key: str):
        print(f"Active tab: {key}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabsExampleWindow()
    window.show()
    app.exec()
