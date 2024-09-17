import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.inputs.input_select import InputSelect
from flim_components.styles.inputs_styles import InputStyles

class InputSelectExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Select Widgets Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        self.select_input = InputSelect(
            label="Select Option:",
            selected_value=1,
            options=["Option 1", "Option 2", "Option 3"],
            event_callback=self.on_select_value_changed,
            width=200,
            stylesheet=InputStyles.input_select_style(),
        )

        layout.addWidget(self.select_input)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def on_select_value_changed(self, index):
        print(f"Selected index changed to: {index}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputSelectExampleWindow()
    window.show()
    sys.exit(app.exec())
