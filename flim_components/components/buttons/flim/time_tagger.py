from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox, QVBoxLayout
from typing import Callable, Optional
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from layouts.compact_layout import CompactLayout
from utils.resource_path import resource_path
from styles.buttons_styles import ButtonStyles


class TimeTaggerButton(QWidget):
    """
    A Flim widget representing a 'Time Tagger' button, which includes a checkbox and an icon.

    Parameters
    ----------
    event_callback : Callable[[bool], None]
        The callback function to be triggered when the checkbox state changes.
    text : str, optional
        The text to be displayed next to the checkbox (default is "TIME TAGGER").
    width : int | None, optional
        The width of the widget in pixels (default is None).
    height : int | None, optional
        The height of the widget in pixels (default is None).
    fg_color : str, optional
        The color of the checkbox text (default is "#0053a4").
    border_color : str, optional
        The color of the widget's border (default is "#0053a4").
    checkbox_color : str, optional
        The color of the checkbox (default is an empty string).
    bg_color : str, optional
        The background color of the widget (default is "#ffffff").
    enabled : bool, optional
        Whether the checkbox is enabled or disabled (default is True).
    visible : bool, optional
        Whether the widget is visible or hidden (default is True).
    checked : bool, optional
        Whether the checkbox is initially checked (default is True).
    icon_path : str | None, optional
        The file path to the icon displayed next to the checkbox (default is the path to the "time-tagger" icon).
    icon_width : int, optional
        The width of the icon in pixels (default is 25).
    parent : Optional[QWidget], optional
        The parent widget, if any (default is None).
    """

    def __init__(
        self,
        event_callback: Callable[[bool], None],
        text: str = "TIME TAGGER",
        width: int | None = None,
        height: int | None = 48,
        fg_color: str = "#0053a4",
        border_color: str = "#0053a4",
        checkbox_color: str = "#0053a4",
        bg_color: str = "#ffffff",
        enabled: bool = True,
        visible: bool = True,
        checked: bool = True,
        icon_path: str | None = resource_path("assets/time-tagger-icon.png"),
        icon_width: int = 25,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.fg_color = fg_color
        self.border_color = border_color
        self.bg_color = bg_color
        self.container = QWidget()
        self.container.setObjectName("container")
        if width is not None:
            self.container.setFixedWidth(width)
        if height is not None:
            self.container.setFixedHeight(height)
        self.container.setContentsMargins(0, 0, 0, 0)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        # time tagger icon
        pixmap = QPixmap(icon_path).scaledToWidth(icon_width)
        icon = QLabel(pixmap=pixmap)
        # time tagger checkbox
        self.time_tagger_checkbox = QCheckBox(text)
        self.time_tagger_checkbox.setChecked(checked)
        self.time_tagger_checkbox.setEnabled(enabled)
        self.time_tagger_checkbox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.time_tagger_checkbox.toggled.connect(event_callback)
        # layout
        layout.addWidget(self.time_tagger_checkbox)
        layout.addWidget(icon)
        self.container.setLayout(layout)
        main_layout = CompactLayout(QVBoxLayout())
        main_layout.addWidget(self.container)
        self.setLayout(main_layout)
        self.set_style(bg_color, fg_color, checkbox_color, border_color)
        self.setVisible(visible)

    def set_checked(self, checked: bool):
        """
        Set the checked state of the checkbox.

        Parameters
        ----------
        checked : bool
            If True, the checkbox will be checked; otherwise, it will be unchecked.
        """
        self.time_tagger_checkbox.setChecked(checked)

    def set_enabled(self, enabled: bool):
        """
        Enable or disable the checkbox.

        Parameters
        ----------
        enabled : bool
            If True, the checkbox will be enabled; otherwise, it will be disabled.
        """
        self.time_tagger_checkbox.setEnabled(enabled)

    def set_visible(self, visible: bool):
        """
        Set the visibility of the widget.

        Parameters
        ----------
        visible : bool
            If True, the widget will be visible; otherwise, it will be hidden.
        """
        self.setVisible(visible)

    def set_style(
        self, bg_color: str, fg_color: str, checkbox_color: str, border_color: str
    ) -> None:
        """
        Apply the styles to the widget, including background color, text color, checkbox color, and border color.

        Parameters
        ----------
        bg_color : str
            The background color of the widget.
        fg_color : str
            The foreground (text) color of the checkbox.
        checkbox_color : str
            The color of the checkbox.
        border_color : str
            The border color of the widget.
        """
        self.container.setStyleSheet(
            ButtonStyles.time_tagger_style(
                bg_color, fg_color, checkbox_color, border_color
            )
        )
