import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from components.buttons.flim.time_tagger import TimeTaggerButton


class TimeTaggerExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Time Tagger Example")
        self.setStyleSheet("background-color: #121212;")  
        self.setFixedSize(400, 400) 
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        time_tagger_widget = TimeTaggerButton( event_callback=self.on_time_tagger_toggled)
        layout.addStretch()
        layout.addWidget(time_tagger_widget)
        layout.addStretch()
        layout.setContentsMargins(10,10,10,10)
        self.setLayout(layout)
        
    def on_time_tagger_toggled(self, checked: bool):
        status = "active" if checked else "inactive"
        print(f"Time tagger {status}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeTaggerExampleWindow()
    window.show()
    app.exec()
