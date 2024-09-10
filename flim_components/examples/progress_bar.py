import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from components.misc.progress_bar import ProgressBar
from styles.progress_bar_styles import ProgressBarStyles
from components.buttons.base_button import BaseButton



class ProgressBarExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ProgressBar Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout(self)

        # Create an instance of ProgressBar
        self.progress_bar = ProgressBar(
            label_text="Progress:", color="#1E90FF", layout_type="vertical", spacing=10
        )

        layout.addWidget(self.progress_bar)

        # Create a button to start progress
        self.start_button = BaseButton(
            text="Start Progress",
            width=150,
            height=50,
            bg_color_base="#1E90FF",
            bg_color_hover="#4682B4",
            bg_color_pressed="#4169E1",
        )
        self.start_button.clicked.connect(self.start_progress)
        layout.addSpacing(20)
        layout.addWidget(self.start_button)

        # Connect the custom signal to a slot
        self.progress_bar.complete.connect(self.on_progress_complete)

        # Indeterminate progress-bar
        self.indeterminate_progress_bar = ProgressBar(
            label_text="Indeterminate:",
            color="red",
            layout_type="vertical",
            spacing=10,
            indeterminate=True,
        )

        layout.addSpacing(40)
        layout.addWidget(self.indeterminate_progress_bar)

        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def start_progress(self):
        self.progress_bar.set_style(
            ProgressBarStyles.progress_bar_style(color="#1E90FF")
        )
        import time
        for i in range(1, 101):
            # Simulate some work
            time.sleep(0.05)  # Simulate delay
            self.progress_bar.update_progress(i, 100, f"Progress: {i}%")

    def on_progress_complete(self):
        self.progress_bar.set_style(
            ProgressBarStyles.progress_bar_style(color="lightgrey")
        )
        print("Progress Complete!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBarExampleWindow()
    window.show()
    sys.exit(app.exec())
