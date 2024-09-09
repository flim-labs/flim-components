from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QLayout,
)
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QSize, Qt
from typing import Literal

from utils.resource_path import resource_path

class LoadingWidget(QWidget):
    """
    A custom loading widget that displays a loading animation (GIF) and a label.
    The label can be positioned relative to the GIF (left, right, top, bottom).
    """

    def __init__(
        self,
        label_text: str = "Processing data...",
        gif_path: str = resource_path("../../assets/loading.gif"),
        label_position: Literal["top", "right", "bottom", "left"] = "left",
        label_style: str = "font-family: Montserrat; font-size: 18px; font-weight: bold; color: #50b3d7",
        gif_size: QSize = QSize(36, 36),
        spacing: int = 20,
        visible: bool = False,
        parent: QWidget = None,
    ):
        """
        Initializes the LoadingWidget.

        Parameters
        ----------
        label_text : str, optional
            The text to be displayed on the label (default is "Processing data...").
        gif_path : str
            The path to the GIF file for the loading animation.
        label_position : Literal["top", "right", "bottom", "left"], optional
            The position of the label relative to the GIF (default is "left").
        label_style : str, optional
            The stylesheet to apply to the label (default provides a custom Montserrat style).
        gif_size : QSize, optional
            The size of the loading GIF (default is QSize(36, 36)).
        spacing : int, optional
            The spacing between the label and the GIF (default is 20).
        visible : bool, optional
            Whether the widget is initially visible (default is False).            
        parent : QWidget, optional
            The parent widget for this loading widget (default is None).
        """
        super().__init__(parent)

        # Initialize the label with the provided text and style
        self.loading_text = QLabel(label_text)
        if label_style is not None:
            self.loading_text.setStyleSheet(label_style)
        # Initialize the GIF animation
        self.gif_label = QLabel()
        loading_gif = QMovie(gif_path)
        loading_gif.setScaledSize(gif_size)
        self.gif_label.setMovie(loading_gif)
        loading_gif.start()
        # Create the layout based on the label position
        self.layout = self._create_layout(label_position, spacing)
        self.setLayout(self.layout)
        # Initially hide the widget
        self.set_visible(visible)

    def _create_layout(
        self, position: Literal["top", "right", "bottom", "left"], spacing: int
    ) -> QLayout:
        """
        Creates and returns a layout for the widget based on the label's position.

        Parameters
        ----------
        position : Literal["top", "right", "bottom", "left"]
            The position of the label relative to the GIF.
        spacing : int
            The amount of space between the label and the GIF.

        Returns
        -------
        layout : QLayout
            The layout with the label and the GIF in the specified position.
        """
        if position in ["left", "right"]:
            layout = QHBoxLayout()
        else:
            layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the widgets to the layout based on the position
        if position == "left":
            layout.addWidget(self.loading_text, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addSpacing(spacing)
            layout.addWidget(self.gif_label, alignment=Qt.AlignmentFlag.AlignCenter)
        elif position == "right":
            layout.addWidget(self.gif_label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addSpacing(spacing)
            layout.addWidget(self.loading_text, alignment=Qt.AlignmentFlag.AlignCenter)
        elif position == "top":
            layout.addWidget(self.loading_text, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addSpacing(spacing)
            layout.addWidget(self.gif_label, alignment=Qt.AlignmentFlag.AlignCenter)
        else:  # position == "bottom"
            layout.addWidget(self.gif_label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addSpacing(spacing)
            layout.addWidget(self.loading_text, alignment=Qt.AlignmentFlag.AlignCenter)

        return layout

    def set_visible(self, visible: bool):
        """
        Sets the visibility of the widget.

        Parameters
        ----------
        visible : bool
            If True, the widget is made visible; if False, it is hidden.
        """
        self.setVisible(visible)

    def set_label_text(self, text: str):
        """
        Sets the text for the loading label.

        Parameters
        ----------
        text : str
            The new text to display in the label.
        """
        self.loading_text.setText(text)

    def set_label_style(self, stylesheet: str):
        """
        Sets the stylesheet for the loading label.

        Parameters
        ----------
        stylesheet : str
            The new stylesheet to apply to the label.
        """
        self.loading_text.setStyleSheet(stylesheet)

    def start(self):
        """
        Starts the loading animation and makes the widget visible.
        """
        self.gif_label.movie().start()
        self.set_visible(True)

    def stop(self):
        """
        Stops the loading animation and hides the widget.
        """
        self.gif_label.movie().stop()
        self.set_visible(False)

class OverlayLoadingWidget(QWidget):
    pass
