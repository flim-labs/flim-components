import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from components.misc.loading_widget import LoadingWidget
from utils.resource_path import resource_path


class LoadingWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)

        loading_widget = LoadingWidget(
            visible=True,
            label_position="left",
            gif_path=resource_path("../assets/loading.gif"),
        )
        layout.addWidget(loading_widget)

        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
