import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from components.misc.loading_widget import LoadingOverlayWidget
from utils.resource_path import resource_path


class LoadingOverlayWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Widget Example")
        self.setStyleSheet("background-color: #222222; color: white;")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.loading_widget = LoadingOverlayWidget(
            label_position="left",
            gif_path=resource_path("assets/loading.gif"),
            widget_alignment=Qt.AlignmentFlag.AlignBottom,
            parent=self,
        )
        self.loading_widget.toggle_visibility()
        layout.addWidget(self.loading_widget)

        self.setLayout(layout)

    def showEvent(self, event):
        super().showEvent(event)
        self.loading_widget.resize_overlay(self.rect())

    def resizeEvent(self, event):
        self.loading_widget.resize_overlay(self.rect())
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingOverlayWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
