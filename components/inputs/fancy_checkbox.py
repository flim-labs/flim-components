from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush,
    QMouseEvent,
)


class FancyCheckbox(QWidget):
    toggled = pyqtSignal(bool)  # Signal to emit when the checkbox state changes

    def __init__(
        self,
        label: str,
        checked: bool = False,
        enabled: bool = True,
        checked_color: str = "#FF4242",
        disabled_color: str = "#3c3c3c",
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        # Initialize the PaintedCheckbox with the given parameters
        self.checkbox = PaintedCheckbox(checked_color, disabled_color, checked, enabled, parent=self)
        self.label = QLabel(label, self)

        # Set cursor shape for both checkbox and label
        self.checkbox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label.setCursor(Qt.CursorShape.PointingHandCursor)

        # Add the checkbox and label to the layout
        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.label)

        # Connect the toggled signal from PaintedCheckbox to emit_toggled_signal
        self.checkbox.toggled.connect(self.emit_toggled_signal)

    def emit_toggled_signal(self, checked):
        self.toggled.emit(checked)  # Re-emit the toggled signal from FancyCheckbox
        
    def is_checked(self):
        return self.checkbox.is_checked()

    def is_enabled(self):
        return self.checkbox.is_enabled()

    def set_checked(self, checked):
        self.checkbox.set_checked(checked)

    def set_text(self, text):
        self.label.setText(text)

    def set_enabled(self, enabled):
        self.checkbox.set_enabled(enabled)
        self.label.setEnabled(enabled)


class PaintedCheckbox(QWidget):
    toggled = pyqtSignal(bool)  # Signal to emit when the checkbox state changes

    def __init__(
        self,
        checked_color: str = "#FF4242",
        disabled_color: str = "#3c3c3c",
        checked: bool = False,
        enabled: bool = True,
        parent=None,
    ):
        super().__init__(parent)
        self.setFixedSize(20, 20)  # Set the size of the checkbox
        self.checked_color = checked_color
        self.disabled_color = disabled_color
        self.checked = checked
        self.enabled = enabled

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Use one line to determine the outer and inner color based on the checkbox state and enabled state
        outer_color = QColor(self.checked_color if self.enabled else self.disabled_color)
        painter.setPen(QPen(outer_color, 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(1, 1, 18, 18)

        if self.checked:
            painter.setBrush(QBrush(outer_color))
            painter.drawEllipse(4, 4, 12, 12)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.enabled:
            # Toggle the checked state and update the checkbox
            self.checked = not self.checked
            self.update()  # Trigger a repaint
            self.toggled.emit(self.checked)  # Emit the toggled signal

    def is_checked(self):
        return self.checked

    def is_enabled(self):
        return self.enabled

    def set_checked(self, checked):
        if self.checked != checked:
            self.checked = checked
            self.update()

    def set_enabled(self, enabled):
        if self.enabled != enabled:
            self.enabled = enabled
            self.update()
