import random
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer
from components.misc.cps_counter import CPSCounter


class CPSCounterExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CPS Counter Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setFixedSize(400, 200) 

        # Create and configure the layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

        # Initialize the CPSCounter
        self.cps_counter = CPSCounter(
            label_text="No CPS", 
            cps_threshold_animation=True, 
            visible=True
        )
      
        # Add widget to layout
        layout.addWidget(self.cps_counter)

        # Timer to simulate CPS updates periodically
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Update every second
        self.timer.timeout.connect(self.simulate_cps_update)
        self.timer.start()

        # Variables to simulate CPS count updates
        self.last_time_ns = 0
        self.cps_curr_count = 0
        self.cps_last_count = 0
        self.interval_ns = 330_000_000 
        self.cps_threshold = 5  # Example threshold for animation

    def simulate_cps_update(self):
        """
        Simulate CPS count update with random values.
        """
        current_time_ns = time.time_ns()  
        self.cps_last_count = self.cps_curr_count
        self.cps_curr_count += random.randint(0, 10)  # Simulate a random CPS count
        self.cps_counter.update_cps_count(
            current_time_ns,
            self.last_time_ns,
            self.interval_ns,
            self.cps_curr_count,
            self.cps_last_count,
            self.cps_threshold,
        )
        self.last_time_ns = current_time_ns 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CPSCounterExampleWindow()
    window.show()
    sys.exit(app.exec())

