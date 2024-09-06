from typing import Callable, Literal, Optional
from PyQt6.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QPainter, QColor, QMouseEvent
from PyQt6.QtWidgets import QWidget, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout

from utils.layout_utils import LayoutUtils


def take_closest(num, collection):
    return min(collection, key=lambda x: abs(x - num))


class SwitchCircle(QWidget):
    """
    A circular component of a switch that can move within a specified range.

    Parameters
    ----------
    parent : QWidget
        The parent widget of this circle.
    move_range : tuple[int, int]
        A tuple specifying the horizontal range within which the circle can move.
    color : str
        The color of the circle.
    animation_curve : QEasingCurve.Type
        The easing curve for the animation of the circle.
    animation_duration : int
        The duration of the animation in milliseconds.
    """

    def __init__(
        self,
        parent: QWidget,
        move_range: tuple[int, int],
        color: str,
        animation_curve: QEasingCurve.Type,
        animation_duration: int,
    ):
        super().__init__(parent=parent)
        self.color = color
        self.move_range = move_range
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)
        self.oldX = 0
        self.new_x = 0

    def paintEvent(self, event):
        """
        Paints the circle on the widget.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(self.color))
        painter.drawEllipse(1, 1, 20, 20)

    def set_color(self, value: str):
        """
        Sets the color of the circle and updates the widget.

        Parameters
        ----------
        value : str
            The new color for the circle.
        """
        self.color = value
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handles the mouse press event to start moving the circle.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        self.animation.stop()
        self.oldX = event.globalPosition().x()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Handles the mouse move event to move the circle.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        delta = event.globalPosition().x() - self.oldX
        self.new_x = delta + self.x()
        if self.new_x < self.move_range[0]:
            self.new_x = self.move_range[0]
        if self.new_x > self.move_range[1]:
            self.new_x = self.move_range[1]
        self.move(int(self.new_x), self.y())
        self.oldX = event.globalPosition().x()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Handles the mouse release event to animate the circle to the closest end.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        try:
            go_to = take_closest(self.new_x, self.move_range)
            self.animation.setStartValue(self.pos())
            self.animation.setEndValue(QPoint(go_to, self.y()))
            self.animation.start()
            self.parent().setChecked(go_to == self.move_range[1])
        except AttributeError:
            pass
        super().mouseReleaseEvent(event)


class SwitchControl(QCheckBox):
    """
    A switch control that toggles between on and off states with animation.

    Parameters
    ----------
    event_callback : Callable[[bool], None]
        A function that is called whenever the switch is toggled.       
    parent : QWidget, optional
        The parent widget of this switch (default is None).
    bg_color : str, optional
        The background color of the switch when inactive (default is "#777777").
    circle_color : str, optional
        The color of the circle in the switch (default is "#222222").
    active_color : str, optional
        The background color of the switch when active (default is "#aa00ff").
    animation_curve : QEasingCurve.Type, optional
        The easing curve for the switch animation (default is QEasingCurve.Type.OutBounce).
    animation_duration : int, optional
        The duration of the animation in milliseconds (default is 300).
    checked : bool, optional
        Whether the switch is initially checked (default is False).
    change_cursor : bool, optional
        Whether to change the cursor to a pointing hand (default is True).
    width : int, optional
        The width of the switch (default is 80).
    height : int, optional
        The height of the switch (default is 28).
    """

    def __init__(
        self,
        event_callback: Callable[[bool], None],
        parent: Optional[QWidget] = None,
        bg_color: str = "#777777",
        circle_color: str = "#222222",
        active_color: str = "#aa00ff",
        animation_curve: QEasingCurve.Type = QEasingCurve.Type.OutBounce,
        animation_duration: int = 300,
        checked: bool = False,
        change_cursor: bool = True,
        width: int = 80,
        height: int = 28,
    ):
        super().__init__(parent)
        self.setFixedSize(width, height)
        if change_cursor:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.active_color = active_color
        self.animation_curve = animation_curve
        self.animation_duration = animation_duration
        self.__circle = SwitchCircle(
            self,
            (3, self.width() - 26),
            self.circle_color,
            self.animation_curve,
            self.animation_duration,
        )
        self.__circle_position = 3
        self.auto = False
        self.pos_on_press = None
        self.animation = QPropertyAnimation(self.__circle, b"pos")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(animation_duration)
        self.toggled.connect(event_callback)

        if checked:
            self.__circle.move(self.width() - 26, 3)
            self.setChecked(True)
        else:
            self.__circle.move(3, 3)
            self.setChecked(False)

    def paintEvent(self, event):
        """
        Paints the switch on the widget, including the background and active state.

        Parameters
        ----------
        event : QPaintEvent
            The paint event.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        enabled = self.isEnabled()
        if not self.isChecked():
            painter.setBrush(QColor(self.bg_color) if enabled else QColor("black"))
            painter.drawRoundedRect(
                0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2
            )
        else:
            painter.setBrush(
                QColor(self.active_color) if enabled else QColor("darkgrey")
            )
            painter.drawRoundedRect(
                0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2
            )

    def hitButton(self, pos):
        """
        Determines whether the click position is within the button area.

        Parameters
        ----------
        pos : QPoint
            The position of the mouse click.

        Returns
        -------
        bool
            True if the position is within the button area; otherwise, False.
        """
        return self.contentsRect().contains(pos)

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handles the mouse press event to start animation.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        self.auto = True
        self.pos_on_press = event.globalPosition()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Handles the mouse move event to detect drag behavior.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        if event.globalPosition() != self.pos_on_press:
            self.auto = False
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """
        Handles the mouse release event to toggle the switch.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event.
        """
        if self.auto:
            self.auto = False
            self.start_animation(not self.isChecked())

    def start_animation(self, checked: bool):
        """
        Starts the animation to move the circle to the checked position.

        Parameters
        ----------
        checked : bool
            Whether the switch should be animated to the checked position.
        """
        self.animation.stop()
        self.animation.setStartValue(self.__circle.pos())
        if checked:
            self.animation.setEndValue(QPoint(self.width() - 26, self.__circle.y()))
        else:
            self.animation.setEndValue(QPoint(3, self.__circle.y()))
        self.setChecked(checked)
        self.animation.start()


class SwitchBox(QWidget):
    """
    A customizable widget that combines a label and a switch control into a single component.

    Parameters
    ----------
    label : str
        The text to be displayed as the label for the switch.
    event_callback : Callable[[bool], None]
        A function that is called whenever the switch is toggled.     
    enabled : bool, optional
        Whether the switch is initially enabled (default is True).
    visible : bool, optional
        Whether the switch box is initially visible (default is True).                  
    bg_color : str, optional
        The background color of the switch (default is "#777777").
    circle_color : str, optional
        The color of the switch's circle (default is "#222222").
    active_color : str, optional
        The color of the switch when it is in the active (checked) state (default is "#aa00ff").
    checked : bool, optional
        The initial checked state of the switch (default is False).
    width : int, optional
        The width of the switch (default is 80).
    height : int, optional
        The height of the switch (default is 28).
    spacing : int, optional
        The spacing between the label and the switch (default is 8).
    layout_type : Literal ["horizontal", "vertical"], optional
        The layout type for the label and switch, either "vertical" or "horizontal" (default is "vertical").
    parent : QWidget, optional
        The parent widget of this switch box (default is None).
    """

    def __init__(
        self,
        label: str,
        event_callback: Callable[[bool], None],
        enabled: bool = True,
        visible: bool = True,
        bg_color: str = "#777777",
        circle_color: str = "#222222",
        active_color: str = "#aa00ff",
        checked: bool = False,
        width: int = 80,
        height: int = 28,
        spacing: int = 8,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.q_label = QLabel(label)
        self.control_layout = (
            QVBoxLayout() if layout_type == "vertical" else QHBoxLayout()
        )
        self.control_layout.addWidget(self.q_label)
        self.control_layout.addSpacing(spacing)
        self.switch = SwitchControl(
            event_callback= event_callback,
            bg_color=bg_color,
            circle_color=circle_color,
            active_color=active_color,
            checked=checked,
            height=height,
            width=width,
        )
        self.control_layout.addWidget(self.switch)
        self.setLayout(self.control_layout)
        self.set_enabled(enabled)
        self.set_visible(visible)

    def set_enabled(self, state):
        """
        Enable or disable the switch widget.

        Parameters
        ----------
        state : bool
            If True, enables the switch widget; if False, disables it.
        """
        self.switch.setEnabled(state)

    def set_visible(self, state):
        """
        Show or hide the switch box and all its child widgets.

        Parameters
        ----------
        state : bool
            If True, makes the switch box visible; if False, hides it.
        """
        if state:
            LayoutUtils.show_layout(self.control_layout)
        else:
            LayoutUtils.hide_layout(self.control_layout)

    def set_checked(self, state):
        """
        Check or uncheck the switch widget.

        Parameters
        ----------
        state : bool
            If True, makes the switch widget checked; if False, unchecks it.
        """
        self.switch.setChecked(state)

    def is_enabled(self) -> bool:
        """
        Check if the switch widget is enabled.

        Returns
        -------
        bool
            True if the switch widget is enabled, False otherwise.
        """
        return self.switch.isEnabled()

    def is_checked(self) -> bool:
        """
        Check if the switch widget is checked.

        Returns
        -------
        bool
            True if the switch widget is checked, False otherwise.
        """
        return self.switch.isChecked()

    def set_label_text(self, text: str):
        """
        Set the text for the label associated with the switch widget.

        Parameters
        ----------
        text : str
            The text to display on the label.
        """
        self.q_label.setText(text)