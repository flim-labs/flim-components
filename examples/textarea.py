import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from styles.inputs_styles import InputStyles
from components.inputs.textarea import TextArea  

class TextAreaExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TextArea Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        self.text_area = TextArea(
            label="Enter your message:",
            event_callback=self.on_text_changed,
            max_chars=200,
            placeholder="Type your message ...",
            text="",
            width=400,
            stylesheet=InputStyles.input_text_style(),
        )

        layout.addWidget(self.text_area)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def on_text_changed(self):
        text = self.text_area.get_text()
        print(f"Text changed: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextAreaExampleWindow()
    window.show()
    sys.exit(app.exec())
