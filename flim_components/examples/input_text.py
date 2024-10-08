import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.inputs.input_text import InputText
from flim_components.styles.inputs_styles import InputStyles

class InputTextExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Text Widgets Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        self.text_input = InputText(
            label="Enter Text:",
            event_callback=self.on_text_changed,
            placeholder="Type here...",
            text="Initial Text",
            width=300,
            stylesheet=InputStyles.input_text_style(),
        )

        layout.addWidget(self.text_input)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def on_text_changed(self, text):
        print(f"Text input changed to: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputTextExampleWindow()
    window.show()
    sys.exit(app.exec())
