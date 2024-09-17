import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.inputs.switch import DualLabelSwitchBox, SwitchBox

class SwitchExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SwitchBox Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        switch_box = SwitchBox(
            label="One label switch:",
            event_callback=self.on_switch_toggled,
            bg_color="#777777",
            circle_color="#ffffff",
            active_color="#00ff00",
            checked=False,
            width=80,
            height=28,
            spacing=10,
            layout_type="horizontal",
        )

        dual_label_switch = DualLabelSwitchBox(
            event_callback=self.on_dual_label_switch_toggled,
            label_on="ON",
            label_off="OFF",
        )

        layout.addWidget(switch_box)
        layout.addSpacing(20)
        layout.addWidget(dual_label_switch)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

    def on_switch_toggled(self, state):
        print("Switch is now:", "ON" if state else "OFF")

    def on_dual_label_switch_toggled(self, state):
        print("Dual Label Switch is now:", "ON" if state else "OFF")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwitchExampleWindow()
    window.show()
    sys.exit(app.exec())
