import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

from flim_components.layouts.layout_separator import LayoutSeparator

class LayoutSeparatorExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout Separator Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setFixedSize(400, 400) 
        
        # Create main layout
        main_layout = QVBoxLayout()

        # Add some widgets before the separator
        label1 = QLabel("Section 1")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label1)

        # Add a horizontal separator
        separator1 = LayoutSeparator(
            line_width=2,
            color="#FF0000",  # Red color
            horizontal_space=10,
            vertical_space=20,
            layout_type="horizontal",
            visible=True
        )
        main_layout.addWidget(separator1)

        # Add some widgets after the separator
        label2 = QLabel("Section 2")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label2)

        # Add another separator, this time vertical
        separator2 = LayoutSeparator(
            line_width=2,
            color="#00FF00",  # Green color
            horizontal_space=20,
            vertical_space=10,
            layout_type="vertical",
            visible=True
        )
        main_layout.addWidget(separator2)

        # Add some more widgets to the right of the vertical separator
        label3 = QLabel("Section 3")
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label3)        
        

       
        main_layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LayoutSeparatorExampleWindow()
    window.show()
    sys.exit(app.exec())
