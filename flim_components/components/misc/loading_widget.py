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
from styles.loading_styles import LoadingStyles
from utils.resource_path import resource_path


class LoadingWidget(QWidget):
    """
    A custom loading widget that displays a loading animation (GIF) and a label.
    The label can be positioned relative to the GIF (left, right, top, bottom).

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

    def __init__(
        self,
        label_text: str = "Processing data...",
        gif_path: str = resource_path("assets/loading.gif"),
        label_position: Literal["top", "right", "bottom", "left"] = "left",
        label_style: str = "font-family: Montserrat; font-size: 18px; font-weight: bold; color: #50b3d7",
        gif_size: QSize = QSize(36, 36),
        spacing: int = 20,
        visible: bool = False,
        parent: QWidget = None,
    ):
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


class LoadingOverlayWidget(QWidget):
    
    """
    A custom loading overlay widget that displays a loading animation (GIF) and a label.
    
    Parameters
    ----------
    widget_alignment : Qt.AlignmentFlag, optional
        The alignment of the widget within its parent. Default is Qt.AlignmentFlag.AlignBottom.
    label_text : str, optional
        The text to display in the loading label. Default is "Processing data...".
    gif_path : str, optional
        The file path to the GIF animation. Default is "path/to/loading.gif".
    label_position : Literal["top", "right", "bottom", "left"], optional
        The position of the label relative to the GIF. Default is "left".
    label_style : str, optional
        The CSS style to apply to the label. Default is "font-family: Montserrat; font-size: 18px; font-weight: bold; color: #50b3d7".
    background_color : str, optional
        The background color of the loading widget. Default is "black".
    border_color : str, optional
        The color of the border. Default is "#50b3d7".
    border_position : Literal["top", "right", "bottom", "left"], optional
        The position of the border. Default is "top".
    gif_size : QSize, optional
        The size of the GIF animation. Default is QSize(36, 36).
    spacing : int, optional
        The space between the label and the GIF. Default is 20.
    parent : QWidget, optional
        The parent widget of the overlay. Default is None.    
    """    

    def __init__(
        self,
        widget_alignment: (
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignTop
        ) = Qt.AlignmentFlag.AlignBottom,
        label_text: str = "Processing data...",
        gif_path: str = resource_path("assets/loading.gif"),
        label_position: Literal["top", "right", "bottom", "left"] = "left",
        label_style: str = "font-family: Montserrat; font-size: 18px; font-weight: bold; color: #50b3d7",
        background_color: str = "black",
        border_color: str = "#50b3d7",
        border_position: Literal["top", "right", "bottom", "Left"] = "top",
        gif_size: QSize = QSize(36, 36),
        spacing: int = 20,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.app = parent
        self.setGeometry(parent.rect())
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint
        )
        self.loading_widget = QWidget()
        self.loading_widget.setObjectName("loading_widget")
        self.set_container_style(background_color, border_color, border_position)
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.loading_widget)

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
        self.layout.setAlignment(widget_alignment)
        self.loading_widget.setLayout(self.layout)
        self.setLayout(self.main_layout)
        self.hide()
        
        
    def _create_layout(
            self, position: Literal["top", "right", "bottom", "left"], spacing: int
        ) -> QLayout:
            if position in ["left", "right"]:
                layout = QHBoxLayout()
            else:
                layout = QVBoxLayout()

            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
            layout.setContentsMargins(15, 15, 15, 15)
            layout.addStretch()

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

            layout.addStretch()
            return layout

    def toggle_visibility(self):
        """
        Toggles the visibility of the loading overlay widget.
        """
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()

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

    def set_container_style(
        self,
        background_color: str,
        border_color: str,
        border_position: Literal["top", "right", "bottom", "left"]
    ) -> None:
        """
        Sets the style for the loading widget container.

        Parameters
        ----------
        background_color : str
            The background color of the loading widget.
        border_color : str
            The color of the border.
        border_position : Literal["top", "right", "bottom", "left"]
            The position of the border relative to the widget.
        """
        style = LoadingStyles.loading_overlay_widget_style(
            background_color, border_color, border_position
        )
        self.loading_widget.setStyleSheet(style)

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

    def resize_overlay(self, rect):
        """
        Resizes the overlay widget to match the dimensions of the specified rectangle.

        Parameters
        ----------
        rect : QRect
            The rectangle that defines the new size and position of the overlay.
        """
        self.setGeometry(rect)
        self.raise_()