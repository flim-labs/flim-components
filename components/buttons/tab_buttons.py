from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from typing import List, Optional
from PyQt6.QtCore import pyqtSignal
from components.buttons.base_button import BaseButton
from layouts.compact_layout import CompactLayout
from models.models import Toggleable
from styles.buttons_styles import ButtonStyles


class Tabs(QWidget):
    """
    A customizable tab widget that allows for the creation of multiple toggleable tabs.

    Parameters
    ----------
    tabs_config : List[Toggleable]
        A list of configurations for each tab, where each configuration is a dictionary
        that includes the tab text, its unique key, and its active state.
    enabled : bool, optional
        Determines if all tabs are initially enabled (default is True).
    visible : bool, optional
        Determines if all tabs are initially visible (default is True).
    fg_color_active : str, optional
        The foreground color of the active tab (default is "#ffffff").
    fg_color_inactive : str, optional
        The foreground color of the inactive tabs (default is "#ffffff").
    bg_color_active : str, optional
        The background color of the active tab (default is "#D01B1B").
    bg_color_inactive : str, optional
        The background color of the inactive tabs (default is "transparent").
    border_color_active : str, optional
        The border color of the active tab (default is "transparent").
    border_color_inactive : str, optional
        The border color of the inactive tabs (default is "#D01B1B").
    bg_color_hover : str, optional
        The background color of the tab when hovered (default is "#E23B3B").
    bg_color_pressed : str, optional
        The background color of the tab when pressed (default is "#B01010").
    bg_color_disabled : str, optional
        The background color of the tab when disabled (default is "#cecece").
    border_color_disabled : str, optional
        The border color of the tab when disabled (default is "#cecece").
    fg_color_disabled : str, optional
        The foreground color of the tab when disabled (default is "#8c8b8b").
    parent : Optional[QWidget], optional
        The parent widget of the tab control, if any (default is None).
    stylesheet : str | None, optional
        A custom stylesheet to apply to the tabs, if any (default is None).

    Signals
    -------
    active : pyqtSignal(str)
        Emitted when a tab is clicked, providing the key of the active tab.
    """

    active = pyqtSignal(str)

    def __init__(
        self,
        tabs_config: List[Toggleable],
        enabled: bool = True,
        visible: bool = True,
        fg_color_active: str = "#ffffff",
        fg_color_inactive: str = "#ffffff",
        bg_color_active: str = "#D01B1B",
        bg_color_inactive: str = "transparent",
        border_color_active: str = "transparent",
        border_color_inactive: str = "#D01B1B",
        bg_color_hover: str = "#E23B3B",
        bg_color_pressed: str = "#B01010",
        bg_color_disabled: str = "#cecece",
        border_color_disabled: str = "#cecece",
        fg_color_disabled: str = "#8c8b8b",
        stylesheet: str | None = None,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.tabs_config = tabs_config
        self.enabled = enabled
        self.visible = visible
        self.fg_color_active = fg_color_active
        self.fg_color_inactive = fg_color_inactive
        self.bg_color_active = bg_color_active
        self.bg_color_inactive = bg_color_inactive
        self.border_color_active = border_color_active
        self.border_color_inactive = border_color_inactive
        self.bg_color_hover = bg_color_hover
        self.bg_color_pressed = bg_color_pressed
        self.bg_color_disabled = bg_color_disabled
        self.fg_color_disabled = fg_color_disabled
        self.border_color_disabled = border_color_disabled
        self.stylesheet = stylesheet

        self.tabs: List[BaseButton] = []

        self.layout = CompactLayout(layout=QVBoxLayout)
        self.tabs_layout = self._build_tabs()
        self.layout.addLayout(self.tabs_layout)
        self.setLayout(self.layout)

    def _build_tabs(self) -> QHBoxLayout:
        tabs_layout = CompactLayout(layout=QHBoxLayout)
        for i, tab_config in enumerate(self.tabs_config):
            tab = self._build_tab(tab_config)
            tabs_layout.addWidget(tab)
            self.tabs.append(tab)
        return tabs_layout

    def _build_tab(self, tab_config: Toggleable) -> BaseButton:
        tab = BaseButton(
            text=tab_config["text"],
            enabled=self.enabled,
            visible=self.visible,
            stylesheet=(
                self.stylesheet
                if self.stylesheet is not None
                else ButtonStyles.tab_button_style(
                    self.fg_color_active,
                    self.fg_color_inactive,
                    self.bg_color_active,
                    self.bg_color_hover,
                    self.bg_color_pressed,
                    self.bg_color_inactive,
                    self.border_color_active,
                    self.border_color_inactive,
                    self.bg_color_disabled,
                    self.fg_color_disabled,
                    self.border_color_disabled,
                )
            ),
        )
        tab.setCheckable(True)
        tab.setChecked(tab_config["active"])
        tab.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        tab.clicked.connect(lambda _, k=tab_config["key"]: self._on_tab_clicked(k))
        return tab

    def _on_tab_clicked(self, key: str):
        for i, tab in enumerate(self.tabs):
            tab_config = self.tabs_config[i]
            if tab_config["key"] == key:
                tab_config["active"] = True
                tab.setChecked(True)
            else:
                tab_config["active"] = False
                tab.setChecked(False)
        self.active.emit(key)

    def get_active_tab(self) -> Optional[str]:
        """
        Get the key of the currently active tab.

        Returns
        -------
        Optional[str]
            The key of the active tab, or None if no tab is active.
        """
        for tab_config, tab in zip(self.tabs_config, self.tabs):
            if tab.isChecked():
                return tab_config["key"]
        return None

    def set_enabled(self, state: bool):
        """
        Enable or disable all tabs.

        Parameters
        ----------
        state : bool
            Whether to enable (True) or disable (False) the tabs.
        """
        for tab in self.tabs:
            if tab is not None and isinstance(tab, BaseButton):
                tab.setEnabled(state)

    def set_visible(self, state: bool):
        """
        Show or hide all tabs.

        Parameters
        ----------
        state : bool
            Whether to show (True) or hide (False) the tabs.
        """
        for tab in self.tabs:
            if tab is not None and isinstance(tab, BaseButton):
                tab.setVisible(state)

    def set_checkable(self, state: bool):
        """
        Make all tabs checkable or not.

        Parameters
        ----------
        state : bool
            Whether to make the tabs checkable (True) or not (False).
        """
        for tab in self.tabs:
            if tab is not None and isinstance(tab, BaseButton):
                tab.setCheckable(state)

    def set_tab_enabled(self, key: str, state: bool):
        """
        Enable or disable a specific tab by its key.

        Parameters
        ----------
        key : str
            The key of the tab to enable or disable.
        state : bool
            Whether to enable (True) or disable (False) the tab.
        """
        for i, tab in enumerate(self.tabs):
            if self.tabs_config[i]["key"] == key:
                tab.setEnabled(state)
                break

    def set_tab_visible(self, key: str, state: bool):
        """
        Show or hide a specific tab by its key.

        Parameters
        ----------
        key : str
            The key of the tab to show or hide.
        state : bool
            Whether to show (True) or hide (False) the tab.
        """
        for i, tab in enumerate(self.tabs):
            if self.tabs_config[i]["key"] == key:
                tab.setVisible(state)
                break

    def set_tab_checkable(self, key: str, state: bool):
        """
        Make a specific tab checkable or not by its key.

        Parameters
        ----------
        key : str
            The key of the tab to make checkable or not.
        state : bool
            Whether to make the tab checkable (True) or not (False).
        """
        for i, tab in enumerate(self.tabs):
            if self.tabs_config[i]["key"] == key:
                tab.setCheckable(state)
                break
