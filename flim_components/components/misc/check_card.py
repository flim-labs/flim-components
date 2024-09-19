from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from typing import Optional
from flim_components.components.buttons.base_button import BaseButton
from flim_components.layouts.compact_layout import CompactLayout
from flim_components.styles.check_card_styles import CheckCardStyles
from flim_components.utils.resource_path import get_asset_path


class CheckCardWidget(QWidget):
    """
    A widget that contains a customizable button and a message label for displaying Flim card check status.

    This widget provides a button used to check the device status and a message label
    for displaying either success (Card ID) or error messages. The styles and visibility of the button and message
    can be customized.

    Parameters
    ----------
    button_text : str, optional
        The text displayed on the button (default is "CHECK DEVICE").
    button_width : int, optional
        The width of the button (default is None).
    button_height : int, optional
        The height of the button (default is 36).
    button_bg_color : str, optional
        The background color of the button (default is "#11468F").
    button_bg_color_hover : str, optional
        The background color of the button when hovered over (default is "#0053a4").
    button_bg_color_pressed : str, optional
        The background color of the button when pressed (default is "#0D3A73").
    button_border_color : str, optional
        The border color of the button (default is "#11468F").
    button_fg_color : str, optional
        The foreground (text) color of the button (default is "#ffffff").
    button_icon : str, optional
        The icon displayed on the button (default is None, which loads a default icon).
    message_color : str, optional
        The text color of the message label (default is "#285da6").
    message_bg_color : str, optional
        The background color of the message label (default is "#242424").
    message_border_color : str, optional
        The border color of the message label (default is "#285da6").
    visible : bool, optional
        Whether the widget is initially visible (default is True).
    enabled : bool, optional
        Whether the button is initially enabled (default is True).
    parent : Optional[QWidget], optional
        The parent widget for the CheckCardWidget (default is None).
    """

    def __init__(
        self,
        button_text: str = "CHECK DEVICE",
        button_width: int | None = None,
        button_height: int | None = 36,
        button_bg_color: str = "#11468F",
        button_bg_color_hover: str = "#0053a4",
        button_bg_color_pressed: str = "#0D3A73",
        button_border_color: str = "#11468F",
        button_fg_color: str = "#ffffff",
        button_icon: str | None = None,
        message_color: str = "#285da6",
        message_bg_color: str = "#242424",
        message_border_color: str = "#285da6",
        visible: bool = True,
        enabled: bool = True,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)

        self.layout = CompactLayout(QHBoxLayout())
        if button_icon is None:
            button_icon = get_asset_path("assets/card-icon.png")

        # Check button
        self.check_button = BaseButton(
            button_text,
            button_width,
            button_height,
            enabled,
            visible,
            button_icon,
            None,
            button_fg_color,
            button_border_color,
            button_bg_color,
            button_bg_color_hover,
            button_bg_color_pressed,
        )

        # Check message label
        self.check_message = QLabel("")
        self.set_message_style(message_color, message_bg_color, message_border_color)

        # Add widgets to layout
        self.layout.addWidget(self.check_button)
        self.layout.addSpacing(5)
        self.layout.addWidget(self.check_message)
        self.check_message.hide()  # Hide message by default

        self.setLayout(self.layout)

    def update_message(
        self,
        message: str,
        error: bool,
        message_color: str,
        bg_color: str,
        border_color: str,
    ) -> None:
        """
        Update the message displayed in the label.

        Depending on the value of `error`, the message will either be an error message or
        a success message showing the Card ID.

        Parameters
        ----------
        message : str
            The message to display.
        error : bool
            If True, the message will be treated as an error. If False, it will show a success message (Card ID).
        message_color : str
            The text color for the message.
        bg_color : str
            The background color for the message label.
        border_color : str
            The border color for the message label.
        """
        self.check_message.setText(message if error else f"Card ID: {message}")
        self.set_message_style(message_color, bg_color, border_color)
        if not self.check_message.isVisible():
            self.check_message.setVisible(True)

    def set_message_style(self, color: str, bg_color: str, border_color: str) -> None:
        """
        Set the style of the message label.

        This method updates the text color, background color, and border color of the message label.

        Parameters
        ----------
        color : str
            The text color of the message label.
        bg_color : str
            The background color of the message label.
        border_color : str
            The border color of the message label.
        """
        self.check_message.setStyleSheet(
            CheckCardStyles.message_style(color, bg_color, border_color)
        )

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the widget.

        Parameters
        ----------
        visible : bool
            If True, the widget will be shown. If False, it will be hidden.
        """
        self.setVisible(visible)

    def set_enabled(self, enabled: bool) -> None:
        """
        Enable or disable the check button.

        Parameters
        ----------
        enabled : bool
            If True, the button will be enabled. If False, the button will be disabled.
        """
        self.check_button.setEnabled(enabled)
