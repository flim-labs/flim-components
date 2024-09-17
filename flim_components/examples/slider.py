import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from flim_components.components.inputs.slider import Slider, SliderWithInputFactory

class SliderExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        # Horizontal slider
        self.horizontal_slider = Slider(
            orientation=Qt.Orientation.Horizontal,
            min_value=0,
            max_value=100,
            initial_value=50,
            event_callback=self.on_h_slider_value_changed,
        )

        # Vertical slider
        self.vertical_slider = Slider(
            orientation=Qt.Orientation.Vertical,
            min_value=0,
            max_value=50,
            initial_value=50,
            event_callback=self.on_v_slider_value_changed,
        )

        # Horizontal slider with input
        self.slider_with_input = SliderWithInputFactory.create_slider_with_input(
            input_params={
                "label": "Binded Slider:",
                "event_callback": self.on_slider_with_input_value_changed,
            },
            slider_params={"event_callback": self.on_slider_with_input_value_changed},
            layout_type="horizontal",
            input_position="left",
            spacing=20,
        )

        layout.addWidget(self.horizontal_slider)
        layout.addSpacing(20)
        layout.addWidget(self.vertical_slider)
        layout.addSpacing(20)
        layout.addWidget(self.slider_with_input)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def on_h_slider_value_changed(self, value):
        print(f"Horizontal Slider value changed to: {value}")

    def on_v_slider_value_changed(self, value):
        print(f"Vertical Slider value changed to: {value}")

    def on_slider_with_input_value_changed(self, value):
        print(f"Binded Slider value changed to: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderExampleWindow()
    window.show()
    sys.exit(app.exec())
