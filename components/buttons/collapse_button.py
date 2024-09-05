from PyQt6.QtWidgets import QWidget, QHBoxLayout
from typing import Optional
from PyQt6.QtCore import QPropertyAnimation, QTimer

from components.buttons.base_button import BaseButton
from layouts.compact_layout import CompactLayout
from styles.buttons_styles import ButtonStyles

class CollapseButton(QWidget):
    """
    A button that toggles the visibility of a collapsible widget with an animation.
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
        self.collapsed_icon = collapsed_icon

        self.layout = CompactLayout(QHBoxLayout()) 
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
        self.collapsible_widget.setMaximumHeight(
            self.collapsible_widget.sizeHint().height() if self.expanded else 0
        )
        self.animation = QPropertyAnimation(self.collapsible_widget, b"maximumHeight")
        self.animation.setDuration(animation_duration)        
        QTimer.singleShot(0, self._update_initial_state)

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
    
    def _update_initial_state(self):
        """Update the initial state of the collapsible widget."""
        self.animation.setStartValue(self.collapsible_widget.maximumHeight())
        self.animation.setEndValue(
            self.collapsible_widget.sizeHint().height() if self.expanded else 0
        )

    def toggle_collapsible_widget(self):
        """
        Toggle the state of the collapsible widget between collapsed and expanded.
        """        
        self.expanded = not self.expanded
        if self.expanded:
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.collapsible_widget.sizeHint().height())
            self.collapse_button.set_icon(icon=self.expanded_icon, icon_size=None)  
        else:
            self.animation.setStartValue(self.collapsible_widget.sizeHint().height())
            self.animation.setEndValue(0)
            self.collapse_button.set_icon(icon=self.collapsed_icon, icon_size=None)  
        self.animation.start()

    def set_enabled(self, state: bool) -> None:
        """
        Toggle the enabled state of the button.
        """
        self.collapse_button.setEnabled(state)

    def set_visible(self, state: bool) -> None:
        """
        Toggle the visibility state of the button.
        """
        self.collapse_button.setVisible(state)
