import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.typography.gradient_text import GradientText


class GradientTextExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gradient Text Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout()

        gradient_label = GradientText(
            text="Gradient Text Example",
            colors=[(0.0, "purple"), (1.0, "orange")],
            stylesheet="font-size: 24px; font-weight: bold;"
        )

        layout.addWidget(gradient_label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradientTextExampleWindow()
    window.show()
    sys.exit(app.exec())