import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QSize

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.typography.flim.flim_title import FlimTitle
from utils import resource_path

class FlimTitleExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Flim Title Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout()
        icon= resource_path.resource_path("../assets/flimlabs-logo.png")

        flim_title = FlimTitle(
            icon_path=icon,  
            icon_size=QSize(60, 60),
            spacing=10,
            text="FLIM APP TITLE",
            colors=[(0.7, "#1E90FF"), (1.0, "red")],
            stylesheet="font-size: 40px; font-weight: bold;"
        )

        layout.addWidget(flim_title)
        layout.addStretch(1)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlimTitleExampleWindow()
    window.show()
    sys.exit(app.exec())
