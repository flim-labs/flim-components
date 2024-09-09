from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt


class OverlayWidget(QWidget):
    """
    A widget that displays a translucent image overlay on top of other widgets, positioned at the bottom right of the window.

    Parameters
    ----------
    - image_path : str
        Path to the image file to be displayed.
    - image_width : int, optional
        Width to which the image should be scaled (default is 100).
    - opacity : float, optional
        Opacity level for the image (default is 0.3).
    - padding_right : int, optional
        Padding from the right edge of the widget (default is 10).
    - padding_bottom : int, optional
        Padding from the bottom edge of the widget (default is 20).
    - parent : QWidget, optional
        Parent widget for this overlay (default is None).
    """    
    def __init__(
        self,
        image_path: str,
        image_width: int = 100,
        opacity: float = 0.3,
        padding_right: int = 10,
        padding_bottom: int = 20,
        parent=None,
    ):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.image_path = image_path
        self.image_width = image_width
        self.opacity = opacity
        self.padding_right = padding_right
        self.padding_bottom = padding_bottom
        self.pixmap = QPixmap(self.image_path).scaledToWidth(self.image_width)
        self.adjustSize()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setOpacity(self.opacity)
        x = self.width() - self.pixmap.width() - self.padding_right
        y = self.height() - self.pixmap.height() - self.padding_bottom
        painter.drawPixmap(x, y, self.pixmap)
