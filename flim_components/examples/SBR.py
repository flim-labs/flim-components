import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer
from flim_components.components.misc.SBR import SBRWidget

class SBRWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SBR Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setFixedSize(400, 200) 

        # Create and configure the layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)
        
        # Create the SBR widget
        self.SBR_widget = SBRWidget()

        # Add the SBR widget to the layout
        layout.addWidget(self.SBR_widget)
        layout.addStretch()

        # Set up a QTimer to update the SBR widget periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sbr)
        self.timer.start(300)  # Update every 300 milliseconds

        # Initialize example data
        self.y_data = np.random.random(100) * 10  # Example random data

    def update_sbr(self):
        # Update SBR value with example data and 3 decimal places
        self.y_data = np.random.random(100) * 10  # Update with new random data
        self.SBR_widget.update_SBR(self.y_data, decimals=3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SBRWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
