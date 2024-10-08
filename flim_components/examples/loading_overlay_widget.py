import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from flim_components.components.misc.loading_widget import LoadingOverlayWidget
from flim_components.utils import resource_path


class LoadingOverlayWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Widget Example")
        self.setStyleSheet("background-color: #222222; color: white;")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        gif_path = resource_path.get_asset_path("assets/loading.gif")

        self.loading_widget = LoadingOverlayWidget(
            label_position="left",
            gif_path=gif_path,
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
