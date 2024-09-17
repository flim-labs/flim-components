import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer

from flim_components.components.buttons.base_button import BaseButton
from flim_components.components.misc.time_counter import TimeCounter


class TimeCounterExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Time Counter Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout()

        # Countdown Timer
        self.countdown_label = TimeCounter(
            input_unit="ms",
            output_unit="s",
            counter_type="countdown",
            end_time=10000,  # 10 seconds
            label_text="Countdown: ",
            color="#FF5733",
            font_size="20px"
        )
        
        self.countdown_timer = QTimer(self)
        self.countdown_timer.setInterval(100)  # Update every 100ms
        self.countdown_timer.timeout.connect(self.update_countdown)

        # Start Countdown Button
        self.start_countdown_button = BaseButton(
            text="Start Countdown", 
            width=150, 
            height=50, 
            bg_color_base="#FF5733", 
            bg_color_hover="#FF5733", 
            bg_color_pressed="#FF5733", 
            border_color="#FF5733"       
        )
        self.start_countdown_button.clicked.connect(self.start_countdown)

        # Countup Timer
        self.countup_label = TimeCounter(
            input_unit="ms",
            output_unit="s",
            counter_type="countup",
            start_time=0,  # Start from 0
            label_text="Countup: ",
            color="#33C1FF",
            font_size="20px"
        )

        self.countup_timer = QTimer(self)
        self.countup_timer.setInterval(100)  # Update every 100ms
        self.countup_timer.timeout.connect(self.update_countup)

        # Start Countup Button
        self.start_countup_button = BaseButton(
            text="Start Countup", 
            width=150, 
            height=50, 
            bg_color_base="#33C1FF", 
            bg_color_hover="#33C1FF", 
            bg_color_pressed="#33C1FF",
            border_color="#33C1FF"       
        )
        self.start_countup_button.clicked.connect(self.start_countup)

        # Add widgets to layout
        layout.addWidget(self.countdown_label)
        layout.addWidget(self.start_countdown_button)
        layout.addSpacing(20)
        layout.addWidget(self.countup_label)
        layout.addWidget(self.start_countup_button)
        
        layout.addStretch(1)
        self.setLayout(layout)

    def start_countdown(self):
        self.start_time = 0  # Reset starting time
        self.countdown_timer.start()

    def update_countdown(self):
        # Simulate elapsed time (count in ms)
        self.start_time += 100  # Increment by 100 ms each tick
        self.countdown_label.update_count(self.start_time)
        # Stop the timer if the countdown is complete
        if self.countdown_label.text().startswith("Countdown: 00:00:000"):
            self.countdown_timer.stop()

    def start_countup(self):
        self.elapsed_time = 0  # Reset elapsed time
        self.countup_timer.start()

    def update_countup(self):
        # Simulate elapsed time (count in ms)
        self.elapsed_time += 100  # Increment by 100 ms each tick
        self.countup_label.update_count(self.elapsed_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeCounterExampleWindow()
    window.show()
    sys.exit(app.exec())
