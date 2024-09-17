import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
)

from flim_components.components.inputs.input_number import InputFloat, InputInteger
from flim_components.styles.inputs_styles import InputStyles


class InputNumberExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Number Widgets Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        layout = QHBoxLayout(self)
        

        # Integer Input
        self.integer_input = InputInteger(
            label="Integer Input:",
            min_value=0,
            max_value=100,
            default_value=25,
            event_callback=self.on_integer_value_changed,
            width=200,
            stylesheet=InputStyles.input_number_style(),
        )

        # Float Input
        self.float_input = InputFloat(
            label="Float Input:",
            min_value=0.0,
            max_value=100.0,
            default_value=25.5,
            event_callback=self.on_float_value_changed,
            width=200,
            stylesheet=InputStyles.input_number_style(),
        )
      
 
        layout.addWidget(self.integer_input)
        layout.addWidget(self.float_input)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def on_integer_value_changed(self, value):
        print(f"Integer input changed to: {value}")

    def on_float_value_changed(self, value):
        print(f"Float input changed to: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputNumberExampleWindow()
    window.show()
    sys.exit(app.exec())
