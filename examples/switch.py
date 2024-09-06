import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from components.inputs.switch import SwitchBox  

class SwitchExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SwitchBox Example")

        layout = QVBoxLayout(self)

        switch_box = SwitchBox(
            label="Enable feature:",
            event_callback=self.on_switch_toggled,
            bg_color="#777777",
            circle_color="#ffffff",
            active_color="#00ff00",
            checked=False,
            width=80,
            height=28,
            spacing=10,
            layout_type="horizontal"
        )

        layout.addWidget(switch_box)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

    def on_switch_toggled(self, state):
        print("Switch is now:", "ON" if state else "OFF")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwitchExampleWindow()
    window.show()
    sys.exit(app.exec())
