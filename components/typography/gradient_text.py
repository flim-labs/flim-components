from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QLinearGradient, QColor, QPen, QTextOption
from PyQt6.QtWidgets import QLabel, QWidget
from typing import List, Tuple, Optional


class GradientText(QLabel):
    """
    A QLabel subclass that renders text with a customizable gradient effect.
    
    Parameters
    ----------
    parent : Optional[QWidget], optional
        The parent widget, if any (default is None).
    text : str, optional
        The text to display in the label (default is an empty string).
    colors : Optional[List[Tuple[float, str]]], optional
        A list of tuples defining the gradient stops. Each tuple contains a position (0.0 to 1.0)
        and a color in hexadecimal format or a valid color name (default is a red-to-blue gradient).
    stylesheet : str, optional
        A string containing the stylesheet to apply to the label (default is an empty string).
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        text: str = "",
        colors: Optional[List[Tuple[float, str]]] = None,
        stylesheet: str = ""
    ):
        super().__init__(parent)
        self.setText(text)
        self.setStyleSheet(stylesheet)
        self.colors = colors if colors else [(0.0, "red"), (1.0, "blue")]
        self._draw_shadow = False
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        """
        Override the mouse press event to trigger a shadow effect.
        
        Parameters
        ----------
        event : QMouseEvent
            The mouse event triggered by pressing the mouse button.
        """
        self._draw_shadow = True
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Override the mouse release event to remove the shadow effect.
        
        Parameters
        ----------
        event : QMouseEvent
            The mouse event triggered by releasing the mouse button.
        """
        self._draw_shadow = False
        self.update()

    def paintEvent(self, event):
        """
        Override the paint event to draw the text with a gradient and optional shadow effect.
        
        Parameters
        ----------
        event : QPaintEvent
            The paint event triggered when the widget needs to be repainted.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setWindow(0, 0, self.width() + 6, self.height() + 3)

        if self._draw_shadow:
            self._draw_text_with_shadow(painter)

        self._draw_gradient_text(painter)

    def _draw_text_with_shadow(self, painter: QPainter):
        """
        Draw the text with a shadow effect.
        
        Parameters
        ----------
        painter : QPainter
            The painter object used to draw the shadowed text.
        """
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(QColor("white"), 0))
        painter.drawText(QRectF(3, -2, self.width(), self.height()), self.text(),
                         QTextOption(Qt.AlignmentFlag.AlignLeft))

    def _draw_gradient_text(self, painter: QPainter):
        """
        Draw the text with a gradient effect.
        
        Parameters
        ----------
        painter : QPainter
            The painter object used to draw the gradient text.
        """
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        for position, color in self.colors:
            gradient.setColorAt(position, QColor(color))
        painter.setPen(QPen(gradient, 0))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawText(QRectF(0, 0, self.width(), self.height()), self.text(),
                         QTextOption(Qt.AlignmentFlag.AlignLeft))
