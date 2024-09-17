import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from flim_components.components.inputs.checkbox import Checkbox, WrappedCheckbox
from flim_components.styles.inputs_styles import InputStyles

class CheckboxExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Checkbox Widgets Example")
        self.setStyleSheet("background-color: #121212; color: white;")  
      
       
        layout = QVBoxLayout()
        layout.setSpacing(30)
        
        h_box_1 = QHBoxLayout()
        self.label_standard = QLabel("Channel 1 Simple unchecked")
        self.checkbox_standard = Checkbox(
            key=1,
            label="Channel 1 Simple",
            event_callback=self.on_checkbox_toggled,
            checked=False,
            fancy=False,  # standard checkbox
        )
        h_box_1.addWidget(self.checkbox_standard)
        h_box_1.addWidget(self.label_standard)
        h_box_1.addStretch(1)
       
        h_box_2 = QHBoxLayout()
        self.label_fancy = QLabel("Channel 2 Fancy unchecked")
        self.checkbox_fancy = Checkbox(
            key=2,
            label="Channel 2 Fancy",
            event_callback=self.on_fancy_checkbox_toggled,
            checked=False,
            fancy=True,  # fancy checkbox
            checkbox_color="#00FF00",
            checkbox_color_unchecked="#FF0000",
            border_color="blue"
        )
        h_box_2.addWidget(self.checkbox_fancy)
        h_box_2.addWidget(self.label_fancy)
        h_box_2.addStretch(1)

        # WrappedCheckbox
        h_box_3 = QHBoxLayout()
        self.label_wrapped = QLabel("Channel 3 Wrapped unchecked")
        self.wrapped_checkbox = WrappedCheckbox(
            key=3,
            label="Channel 3 Wrapped",
            event_callback=self.on_wrapped_checkbox_toggled,
            fancy=True,
            checkbox_color="#FF6347",
            checkbox_color_unchecked="#B22222",
            checkbox_wrapper_width=160,
            checkbox_wrapper_height=40,
            checkbox_wrapper_stylesheet=InputStyles.checkbox_wrapper_style()
        )
        h_box_3.addWidget(self.wrapped_checkbox)
        h_box_3.addWidget(self.label_wrapped)
        h_box_3.addStretch(1)

        layout.addLayout(h_box_1)
        layout.addLayout(h_box_2)
        layout.addLayout(h_box_3)
        layout.addStretch(1)
        self.setLayout(layout)

    def on_checkbox_toggled(self, checked: bool):
        status = "checked" if checked else "unchecked"
        self.label_standard.setText(f"Channel 1 Simple {status}")

    def on_fancy_checkbox_toggled(self, checked: bool):
        status = "checked" if checked else "unchecked"
        self.label_fancy.setText(f"Channel 2 Fancy {status}")

    def on_wrapped_checkbox_toggled(self, checked: bool):
        status = "checked" if checked else "unchecked"
        self.label_wrapped.setText(f"Channel 2 Wrapped {status}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckboxExampleWindow()
    window.show()
    app.exec()