from PyQt6.QtWidgets import QWidget, QHBoxLayout
from typing import Optional
from PyQt6.QtCore import QPropertyAnimation

from components.buttons.base_button import BaseButton
from layouts.compact_layout import CompactLayout
from styles.buttons_styles import ButtonStyles


class CollapseButton(QWidget):
    """
        A button that toggles the visibility of a collapsible widget with an animation.

        Parameters
        ----------
        collapsible_widget : QWidget
            The widget that will be collapsed or expanded when the button is clicked.
        expanded : bool, optional
            The initial state of the collapsible widget. If True, the widget starts in a expanded state (default is True).
        expanded_icon : str, optional
            The file path to the icon to be displayed when the widget is expanded (default is an 'arrow-up' icon).
        collapsed_icon : str, optional
            The file path to the icon to be displayed when the widget is collapsed (default is an 'arrow-down' icon).
        icon_size : str, optional
            The size of the icon displayed on the button (default is "15px"). This should be a valid CSS size string.
        width : int, optional
            The width of the button in pixels (default is 30).
        height : int, optional
            The height of the button in pixels (default is 30).
        enabled : bool, optional
            Whether the button is enabled or disabled (default is True).
        visible : bool, optional
            Whether the button is visible or hidden (default is True).
        bg_color : str, optional
            The background color of the button (default is "transparent").
        border_color : str, optional
            The border color of the button (default is "#808080").
        border_radius : str, optional
            The border radius of the button (default is "15px").
        animation_duration : int, optional
            The duration of the collapse/expand animation in milliseconds (default is 300).
        parent : Optional[QWidget], optional
            The parent widget of the `CollapseButton`, if any (default is None).
        """
    

    def __init__(
        self,
        collapsible_widget: QWidget,
        expanded=True,
        expanded_icon: str = "",
        collapsed_icon: str = "",
        icon_size: str = "15px",
        width: int = 30,
        height: int = 30,
        enabled: bool = True,
        visible: bool = True,
        bg_color: str = "transparent",
        border_color: str = "#808080",
        border_radius: str = "15px",
        animation_duration: int = 300,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.collapsible_widget = collapsible_widget
        self.expanded = expanded
        self.expanded_icon = expanded_icon
        self.collapses_icon = collapsed_icon
        self.layout = CompactLayout(layout=QHBoxLayout) 
        self.collapse_button = self._build_button(
            self.expanded_icon,
            icon_size,
            width,
            height,
            enabled,
            visible,
            bg_color,
            border_color,
            border_radius,
        )
        self.layout.addWidget(self.collapse_button)
        self.setLayout(self.layout)
        self.animation = QPropertyAnimation(self.collapsible_widget, b"maximumHeight")
        self.animation.setDuration(animation_duration)        

    def _build_button(
        self,
        icon: str,
        icon_size: str,
        width: int,
        height: int,
        enabled: bool,
        visible: bool,
        bg_color: str,
        border_color: str,
        border_radius: str,
    ) -> BaseButton:
        button = BaseButton(
            text="",
            width=width,
            height=height,
            enabled=enabled,
            visible=visible,
            icon=icon,
            stylesheet=ButtonStyles.collapse_button_style(
                bg_color, border_color, border_radius, icon_size
            ),
        )
        return button
    

    def toggle_collapsible_widget(self):
        """
        Toggle the state of the collapsible widget between collapsed and expanded.
        """        
        self.collapsed = not self.collapsed
        if self.collapsed:
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.collapsible_widget.sizeHint().height())
            self.collapse_button.set_icon(icon=self.collapses_icon)  
        else:
            self.animation.setStartValue(self.collapsible_widget.sizeHint().height())
            self.animation.setEndValue(0)
            self.collapse_button.set_icon(icon=self.expanded_icon)  
        self.animation.start()


    def set_enabled(self, state: bool) -> None:
        """
        Toggle the enabled state of the button.

        Parameters
        ----------
        state : bool
        """
        self.collapse_button.setEnabled(state)

    def set_visible(self, state: bool) -> None:
        """
        Toggle the visibility state of the button.

        Parameters
        ----------
        state : bool
        """
        self.collapse_button.setVisible(state)
        