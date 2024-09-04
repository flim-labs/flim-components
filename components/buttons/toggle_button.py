from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from typing import List, Optional, TypedDict
from PyQt6.QtCore import pyqtSignal


from components.buttons.base_button import BaseButton
from layouts.compact_layout import CompactLayout
from models.models import Toggleable
from styles.buttons_styles import ButtonStyles



class ToggleButton(QWidget):

    """
        A toggleable widget consisting of a set of child buttons, allowing one button to be active at a time.

        Parameters
        ----------
        toggleables : List[Toggleable]
            A list of dictionaries representing the toggleable buttons. Each dictionary should have the keys:
            - 'text': str
                The text to be displayed on the button.
            - 'key': str
                A unique key identifying the button.
            - 'active': bool
                Whether the button is initially active or not.
        enabled : bool, optional
            Whether the buttons are enabled or disabled (default is True).
        visible : bool, optional
            Whether the buttons are visible or hidden (default is True).
        fg_color_active : str, optional
            The foreground (text) color of the button when active (default is "#ffffff").
        fg_color_inactive : str, optional
            The foreground (text) color of the button when inactive (default is "#8c8b8b").
        bg_color_active : str, optional
            The background color of the button when active (default is "#DA1212").
        bg_color_inactive : str, optional
            The background color of the button when inactive (default is "#cecece").
        parent : Optional[QWidget], optional
            The parent widget of the `ToggleButton`, if any (default is None).
            
        Signals
        -------
        toggled : pyqtSignal(str)
            Emitted when a button is toggled, providing its key.            
    """
    
    toggled = pyqtSignal(str)

    def __init__(
        self,
        toggleables: List[Toggleable],
        enabled: bool = True,
        visible: bool = True,
        fg_color_active: str = "#ffffff",
        fg_color_inactive: str = "#8c8b8b",
        bg_color_active: str = "#DA1212",
        bg_color_inactive: str = "#cecece",
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.toggleables = toggleables
        self.enabled = enabled
        self.visible = visible
        self.fg_color_active = fg_color_active
        self.fg_color_inactive = fg_color_inactive
        self.bg_color_active = bg_color_active
        self.bg_color_inactive = bg_color_inactive
        self.buttons: List[BaseButton] = []
        self.layout = CompactLayout(layout=QVBoxLayout)  
        self.buttons_row_layout = self._build_buttons()
        self.layout.addLayout(self.buttons_row_layout)
        self.setLayout(self.layout)

    def _build_buttons(self) -> QHBoxLayout:
        buttons_row_layout = QHBoxLayout()
        buttons_row_layout.setSpacing(0)
        for i, toggleable in enumerate(self.toggleables):
            is_first = i == 0
            is_last = i == len(self.toggleables) - 1
            button = self._build_button(toggleable, is_first, is_last)
            buttons_row_layout.addWidget(button)
            self.buttons.append(button)
        return buttons_row_layout

    def _build_button(
        self, toggleable: Toggleable, is_first: bool, is_last: bool
    ) -> BaseButton:
        fg_color = (
            self.fg_color_active if toggleable["active"] else self.fg_color_inactive
        )
        bg_color = (
            self.bg_color_active if toggleable["active"] else self.bg_color_inactive
        )
        button = BaseButton(
            text=toggleable["text"],
            enabled=self.enabled,
            visible=self.visible,
            stylesheet=ButtonStyles.toggle_button_style(
                fg_color, bg_color, is_first, is_last
            ),
        )
        button.setCheckable(True)
        button.setChecked(toggleable["active"])
        button.clicked.connect(
            lambda _, k=toggleable["key"]: self._on_button_clicked(k)
        )
        return button

    def _on_button_clicked(self, key: str):
        for i, button in enumerate(self.buttons):
            toggleable = self.toggleables[i]
            if toggleable["key"] == key:
                toggleable["active"] = True
                button.setChecked(True)
            else:
                toggleable["active"] = False
                button.setChecked(False)
            is_first = i == 0
            is_last = i == len(self.toggleables) - 1
            self._set_style(button, is_first, is_last)
        self.toggled.emit(key)

    def _set_style(self, button: BaseButton, is_first: bool, is_last: bool):
        button_active = button.isChecked()
        fg_color = self.fg_color_active if button_active else self.fg_color_inactive
        bg_color = self.bg_color_active if button_active else self.bg_color_inactive
        button.set_style(
            ButtonStyles.toggle_button_style(fg_color, bg_color, is_first, is_last)
        )

    def get_active_button(self) -> Optional[str]:
        """
        Get the key of the currently active child button.

        Returns
        -------
        Optional[str]
            The key of the active button, or None if no button is active.
        """
        for toggleable, button in zip(self.toggleables, self.buttons):
            if button.isChecked():
                return toggleable["key"]
        return None

    def set_enabled(self, state: bool):
        """
        Enable or disable all child buttons.

        Parameters
        ----------
        state : bool
            Whether to enable (True) or disable (False) the buttons.
        """
        for button in self.buttons:
            if button is not None and isinstance(button, BaseButton):
                button.setEnabled(state)

    def set_visible(self, state: bool):
        """
        Show or hide all child buttons.

        Parameters
        ----------
        state : bool
            Whether to show (True) or hide (False) the buttons.
        """
        for button in self.buttons:
            if button is not None and isinstance(button, BaseButton):
                button.setVisible(state)

    def set_checkable(self, state: bool):
        """
        Make all child buttons checkable or not.

        Parameters
        ----------
        state : bool
            Whether to make the child buttons checkable (True) or not (False).
        """
        for button in self.buttons:
            if button is not None and isinstance(button, BaseButton):
                button.setCheckable(state)
