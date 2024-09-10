from PyQt6.QtWidgets import QLabel, QHBoxLayout, QWidget, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
from typing import List, Tuple, Optional

from components.typography.gradient_text import GradientText


class FlimTitle(QWidget):
    """
    A widget that combines an icon and gradient text in a horizontal layout.

    Parameters
    ----------
    parent : Optional[QWidget], optional
        The parent widget, if any (default is None).
    icon_path : str, optional
        The path to the icon file to display before the text (default is an empty string).
    icon_size : QSize, optional
        The size of the icon (default is QSize(40, 40)).
    spacing : int, optional
        The space between the icon and the text (default is 10).
    text : str, optional
        The text to display in the gradient text (default is an empty string).
    colors : Optional[List[Tuple[float, str]]], optional
        A list of tuples defining the gradient stops (default is a red-to-blue gradient).
    stylesheet : str, optional
        A string containing the stylesheet to apply to the gradient text (default is an empty string).
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        icon_path: str = "",
        icon_size: QSize = QSize(40, 40),
        spacing: int = 10,
        text: str = "",
        colors: Optional[List[Tuple[float, str]]] = None,
        stylesheet: str = "",
    ):
        super().__init__(parent)
        self.icon_path = icon_path
        self.icon_size = icon_size
        self.spacing = spacing

        # Create the gradient text instance
        self.gradient_text = GradientText(
            self, text=text, colors=colors, stylesheet=stylesheet
        )

        self._init_ui()

    def _init_ui(self):
        layout = QHBoxLayout(self)

        # Add icon if path is provided
        if self.icon_path:
            pixmap = QPixmap(self.icon_path).scaled(
                self.icon_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            icon_label = QLabel()
            icon_label.setPixmap(pixmap)
            layout.addWidget(icon_label)

        # Add spacing between icon and text
        layout.addSpacing(self.spacing)

        # Add gradient text
        layout.addWidget(self.gradient_text)
        expanding_widget = QWidget()
        expanding_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        layout.addWidget(expanding_widget)        
 
