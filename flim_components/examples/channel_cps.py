import random
import sys
import os
import time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget,QHBoxLayout
from PyQt6.QtCore import QTimer
from components.misc.cps_counter import CPSCounter
from components.misc.channel_cps import ChannelCPS



class ChannelCPSExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Channel/CPS Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setMinimumSize(800, 200)

        # Create and configure the layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

        # Initialize the CPSCounter 1
        self.cps_counter_1 = CPSCounter(
            label_text="No CPS", cps_threshold_animation=True, visible=True
        )

        # Initialize the CPSCounter 2
        self.cps_counter_2 = CPSCounter(
            label_text="No CPS", cps_threshold_animation=True, visible=True
        )

        # Initialize the Channel CPS 1 Widget
        self.channel_cps_1 = ChannelCPS(
            channel_label="Channel 1",
            cps_counter=self.cps_counter_1,
            layout_type="vertical",
        )

        # Add widget to layout
        layout.addWidget(self.channel_cps_1)

        # Initialize the Channel CPS 2 Widget
        self.channel_cps_2 = ChannelCPS(
            channel_label="Channel 2",
            cps_counter=self.cps_counter_2,
            layout_type="horizontal",
        )

        # Add widget to layout
        layout.addWidget(self.channel_cps_2)

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
        self.cps_counter_1.update_cps_count(
            current_time_ns,
            self.last_time_ns,
            self.interval_ns,
            self.cps_curr_count,
            self.cps_last_count,
            self.cps_threshold,
        )
        self.cps_counter_2.update_cps_count(
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
    window = ChannelCPSExampleWindow()
    window.show()
    sys.exit(app.exec())
