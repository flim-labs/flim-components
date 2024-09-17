import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.misc.loading_widget import LoadingWidget
from flim_components.utils import resource_path



class LoadingWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        layout = QVBoxLayout(self)
        
        gif_path = resource_path.get_asset_path("assets/loading.gif")

        loading_widget = LoadingWidget(
            visible=True,
            label_position="left",
            gif_path=gif_path,
        )
        layout.addWidget(loading_widget)

        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
