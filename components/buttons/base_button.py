from PyQt6.QtWidgets import QPushButton, QWidget
from typing import Optional
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon

from styles.buttons_styles import ButtonStyles



class BaseButton(QPushButton):
    """
        A button with a primary style, typically used for main actions in the UI.

        Parameters
        ----------
        text : str
            The text to be displayed on the button.
        width : int, optional
            The width of the button in pixels (default is 110).
        height : int, optional
            The height of the button in pixels (default is 55).
        enabled : bool, optional
            Whether the button is enabled or disabled (default is True).
        visible : bool, optional
            Whether the button is visible or hidden (default is True).
        icon : str | None, optional
            The file path to the icon to be displayed on the button, if any (default is None).
        icon_size : QSize | None, optional
            The size of the icon displayed on the button, if any (default is None).            
        fg_color : str, optional
            The foreground (text) color of the button (default is "#ffffff").
        border_color : str, optional
            The border color of the button (default is "#13B6B4").
        bg_color_base : str, optional
            The background color of the button in its default state (default is "#13B6B4").
        bg_color_hover : str, optional
            The background color of the button when hovered (default is "#1EC99F").
        bg_color_pressed : str, optional
            The background color of the button when pressed (default is "#1AAE88").
        bg_color_disabled : str, optional
            The background color of the button when disabled (default is "#cecece").
        border_color_disabled : str, optional
            The border color of the button when disabled (default is "#cecece").
        fg_color_disabled : str, optional
            The foreground (text) color of the button when disabled (default is "#8c8b8b").
        stylesheet : str | None, optional
            A custom stylesheet to apply to the button, if any (default is None).
        parent : Optional[QWidget], optional
            The parent widget of the button, if any (default is None).
    """

    def __init__(
        self,
        text: str,
        width: int = 110,
        height: int = 55,
        enabled: bool = True,
        visible: bool = True,
        icon: str | None = None,
        icon_size: QSize | None = None,
        fg_color: str = "#ffffff",
        border_color: str = "#13B6B4",
        bg_color_base: str = "#13B6B4",
        bg_color_hover: str = "#1EC99F",
        bg_color_pressed: str = "#1AAE88",
        bg_color_disabled: str = "#cecece",
        border_color_disabled: str = "#cecece",
        fg_color_disabled: str = "#8c8b8b",
        stylesheet: str | None = None,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.set_text(text)
        self.set_icon(icon, icon_size)
        self.setEnabled(enabled)
        self.setVisible(visible)
        self.set_default_size(width, height)
        self.setFlat(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._set_default_style(
            fg_color,
            fg_color_disabled,
            bg_color_base,
            bg_color_hover,
            bg_color_pressed,
            bg_color_disabled,
            border_color,
            border_color_disabled,
            stylesheet,
        )
        
    def set_text(self, text: str) -> None:
        """
        Set the button text.

        Parameters
        ----------
        text : str
        """
        self.setText(text)        

    def _set_default_style(
        self,
        fg_color: str,
        fg_color_disabled: str,
        bg_color_base: str,
        bg_color_hover: str,
        bg_color_pressed: str,
        bg_color_disabled: str,
        border_color: str,
        border_color_disabled: str,
        stylesheet: str | None,
    ) -> None:
        if stylesheet is not None:
            self.setStyleSheet(stylesheet)
        else:
            self.setStyleSheet(
                ButtonStyles.base_button_style(
                    fg_color,
                    bg_color_base,
                    border_color,
                    bg_color_hover,
                    bg_color_pressed,
                    bg_color_disabled,
                    border_color_disabled,
                    fg_color_disabled,
                )
            )

    def _set_default_size(self, width: int = 110, height: int = 55) -> None:
        self.setFixedSize(QSize(width, height))
        
    def set_icon(self, icon: str | None, icon_size: QSize | None) -> None:
        """
        Set the icon for the button.

        Parameters
        ----------
        icon : str | None
            The file path to the icon to be displayed on the button, if any.
        icon_size: QSize | None
            The size of the icon, if any    
        """
        if icon is not None:
            self.setIcon(QIcon(icon))  
            if icon_size is not None:
                self.setIconSize(icon_size)  

    def set_enabled(self, state: bool) -> None:
        """
        Toggle the enabled state of the button.

        Parameters
        ----------
        state : bool
        """
        self.setEnabled(state)

    def set_visible(self, state: bool) -> None:
        """
        Toggle the visibility state of the button.

        Parameters
        ----------
        state : bool
        """
        self.setVisible(state)

    def set_style(self, stylesheet: str) -> None:
        """
        Apply a custom stylesheet to the button.

        Parameters
        ----------
        stylesheet : str
            The stylesheet string to be applied to the button.
        """
        self.setStyleSheet(stylesheet)
        
    
    def update_text_and_style(self, text: str, stylesheet: str):
        """
        Apply a text and a custom stylesheet to the button.
        Useful when you want to change the button appearance depending on some trigger

        Parameters
        ----------
        text: str
        stylesheet : str
        """        
        self.set_text(text)
        self.set_style(stylesheet)
          
