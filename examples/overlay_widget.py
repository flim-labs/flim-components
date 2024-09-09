import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QEvent
from layouts.overlay_widget import OverlayWidget
from utils.resource_path import resource_path

class OverlayWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Overlay Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)

        icon = resource_path("../assets/flimlabs-logo.png")
        self.overlay = OverlayWidget(
            image_path=icon,
            image_width=100,
            opacity=0.3,
            padding_right=10,
            padding_bottom=20,
            parent=self,
        )
        self.overlay.setGeometry(self.rect())
        self.overlay.show()

        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)
        self.installEventFilter(self)

    def eventFilter(self, source, event):
        try:
            if event.type() in (
                QEvent.Type.Resize,
                QEvent.Type.MouseButtonPress,
                QEvent.Type.MouseButtonRelease,
            ):
                self.overlay.raise_()
                self.overlay.resize(self.size())
            return super().eventFilter(source, event)
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
