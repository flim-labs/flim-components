import os
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from typing import Dict, Literal
from components.misc.cps_counter import CPSCounter
from layouts.compact_layout import CompactLayout
from styles.cps_counter_styles import CPSCounterStyles
from utils.resource_path import resource_path


class ChannelCPS(QWidget):
    """
    A widget for displaying a channel with a CPS (Counts Per Second) counter and an arrow icon.

    This widget arranges its child widgets in either a horizontal or vertical layout. It displays
    a label for the channel, a CPS counter, and an arrow icon. The appearance of the label and the
    container can be customized using stylesheets.

    Parameters
    ----------
    channel_label : str
        The text to display as the channel label.
    cps_counter : CPSCounter
        An instance of CPSCounter that shows the counts per second.
    channel_label_stylesheet : str | None, optional
        A stylesheet string to apply to the channel label. If None, a default stylesheet is used.
    layout_type : Literal["horizontal", "vertical"], optional
        The layout orientation for arranging the widgets. Can be "horizontal" or "vertical".
        Default is "horizontal".
    background_color : str, optional
        The background color of the container widget. Default is "transparent".
    border_color : str, optional
        The border color of the container widget. Default is "#3b3b3b".
    arrow_icon_width : int, optional
        The width of the arrow icon. Default is 30.
    visible : bool, optional
        If True, the widget is visible; if False, the widget is hidden. Default is True.
    parent : QWidget, optional
        The parent widget of this widget. Default is None.
    """

    def __init__(
        self,
        channel_label: str,
        cps_counter: CPSCounter,
        channel_label_stylesheet: str | None = None,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        background_color: str = "transparent",
        border_color: str = "#3b3b3b",
        arrow_icon: str = resource_path("assets/arrow-right-grey.png"),
        arrow_icon_width: int = 30,
        visible: bool = True,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.wrapper = QWidget()
        self.compact_layout = CompactLayout(QVBoxLayout())
        self.layout_type = layout_type
        self.layout = QHBoxLayout() if layout_type == "horizontal" else QVBoxLayout()

        self.cps_counter = cps_counter
        if self.layout_type == "vertical":
            self.layout.addStretch()
            self.cps_counter.cps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.channel_label = QLabel(channel_label)
        if self.layout_type == "vertical":
            self.channel_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.set_channel_label_style(channel_label_stylesheet)
        self.layout.addWidget(self.channel_label)
        arrow = QLabel()
        arrow.setPixmap(QPixmap(arrow_icon).scaledToWidth(arrow_icon_width))
        if self.layout_type == "horizontal":
            self.layout.addWidget(arrow)
        self.layout.addWidget(self.cps_counter)
        if self.layout_type == "vertical":
            self.layout.addStretch()

        self.wrapper.setObjectName("container")
        self.set_container_style(background_color, border_color)
        self.wrapper.setLayout(self.layout)
        self.compact_layout.addWidget(self.wrapper)
        self.setLayout(self.compact_layout)
        self.set_visible(visible)

    def set_visible(self, visible: bool) -> None:
        """
        Show or hide the widget.

        Parameters
        ----------
        visible : bool
            If True, the widget is visible; if False, the widget is hidden.
        """
        self.setVisible(visible)

    def set_container_style(self, background_color: str, border_color: str) -> None:
        """
        Set the style for the container widget.

        Parameters
        ----------
        background_color : str
            The background color of the container widget.
        border_color : str
            The border color of the container widget.
        """
        self.wrapper.setStyleSheet(
            CPSCounterStyles.channel_cps_container_style(background_color, border_color)
        )

    def set_channel_label_style(self, stylesheet: str | None) -> None:
        """
        Apply a stylesheet to the channel label.

        Parameters
        ----------
        stylesheet : str | None
            A stylesheet string to apply to the channel label. If None, a default stylesheet is used.
        """
        self.channel_label.setStyleSheet(
            stylesheet
            if stylesheet is not None
            else CPSCounterStyles.channel_cps_label_style(self.layout_type)
        )
