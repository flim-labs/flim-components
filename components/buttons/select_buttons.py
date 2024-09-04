from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
)
from PyQt6.QtCore import QSize, Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from typing import List, Tuple, Optional
from styles.buttons_styles import ButtonStyles


class SelectButton(QPushButton):
    def __init__(
        self,
        text: str,
        selected: bool = False,
        icon: Optional[str] = None,
        icon_size: QSize | None = None,
        fg_color_selected: str = "#ffffff",
        fg_color_unselected: str = "#ffffff",
        fg_color_disabled_selected: str = "#ffffff",
        fg_color_disabled_unselected: str = "#ffffff",
        bg_color_selected: str = "#11468F",
        bg_color_unselected: str = "transparent",
        bg_color_disabled_selected: str = "#3c3c3c",
        bg_color_disabled_unselected: str = "transparent",
        border_color_selected: str = "transparent",
        border_color_unselected: str = "#3b3b3b",
        border_color_disabled_selected: str = "#3b3b3b",
        border_color_disabled_unselected: str = "#3b3b3b",
        bg_color_hover: str = "#0053a4",
        bg_color_pressed: str = "#003d7a",   
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(text, parent)
        self.selected = selected
        self.fg_color_selected = fg_color_selected
        self.fg_color_unselected = fg_color_unselected
        self.fg_color_disabled_selected = fg_color_disabled_selected
        self.fg_color_disabled_unselected = fg_color_disabled_unselected
        self.bg_color_selected = bg_color_selected
        self.bg_color_unselected = bg_color_unselected
        self.bg_color_disabled_selected = bg_color_disabled_selected
        self.bg_color_disabled_unselected = bg_color_disabled_unselected
        self.border_color_selected = border_color_selected
        self.border_color_unselected = border_color_unselected
        self.border_color_disabled_selected = border_color_disabled_selected
        self.border_color_disabled_unselected = border_color_disabled_unselected
        self.bg_color_hover = bg_color_hover
        self.bg_color_pressed = bg_color_pressed
        self._initUI(icon, icon_size)

    def _initUI(self, icon_path: Optional[str], icon_size: QSize | None) -> None:
        if icon_path:
            self.setIcon(QIcon(icon_path))
            if icon_size is not None:
                self.setIconSize(icon_size)
        self.setFlat(True)
        self._updateStyleSheet(self.selected, self.isEnabled())
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_selected(self, selected: bool) -> None:
        self.selected = selected
        self._updateStyleSheet()

    def _updateStyleSheet(self, selected: bool, enabled: bool) -> None:
        if selected:
            if enabled:
                fg_color = self.fg_color_selected
                bg_color = self.bg_color_selected
                border_color = self.border_color_selected
            else:
                fg_color = self.fg_color_disabled_selected                
                bg_color = self.bg_color_disabled_selected
                border_color = self.border_color_disabled_selected
        else:
            if enabled:
                fg_color = self.fg_color_unselected                
                bg_color = self.bg_color_unselected
                border_color = self.border_color_unselected
            else:
                fg_color = self.fg_color_disabled_unselected                
                bg_color = self.bg_color_disabled_unselected
                border_color = self.border_color_disabled_unselected

        self.setStyleSheet(
            ButtonStyles.select_button_style(
                fg_color,
                bg_color_base=bg_color,
                bg_color_hover=self.bg_color_hover,
                bg_color_pressed=self.bg_color_pressed,
                border_color=border_color
            )
        )


class SelectButtonGroup(QWidget):
    """
        A group of selectable buttons with a customizable layout.
        
        Parameters
        ----------
        button_configs : List[Tuple[str, str, str]]
            A list of tuples where each tuple contains:
            - The text displayed on the button.
            - A unique identifier for the button.
            - The file path to the icon displayed on the button (can be None if no icon).
        layout_type : str
            The layout type for the buttons. Options are "horizontal", "vertical", "grid".
        layout_options : Optional[dict]
            Configuration options for the layout. For "grid" layout, specify "rows" and "columns".
        default_selected : Optional[str]
            The key of the button to be selected by default (default is None).
        icon_size : Optional[QSize], optional
            The size of the icon displayed on the button (default is None).
        fg_color_selected : str, optional
            The foreground color when a button is selected (default is "#ffffff").
        fg_color_unselected : str, optional
            The foreground color when a button is unselected (default is "#ffffff").
        fg_color_disabled_selected : str, optional
            The foreground color when a button is disabled and selected (default is "#ffffff").
        fg_color_disabled_unselected : str, optional
            The foreground color when a button is disabled and unselected (default is "#ffffff").
        bg_color_selected : str, optional
            The background color when a button is selected (default is "#11468F").
        bg_color_unselected : str, optional
            The background color when a button is unselected (default is "transparent").
        bg_color_disabled_selected : str, optional
            The background color when a button is disabled and selected (default is "#3c3c3c").
        bg_color_disabled_unselected : str, optional
            The background color when a button is disabled and unselected (default is "transparent").
        border_color_selected : str, optional
            The border color when a button is selected (default is "transparent").
        border_color_unselected : str, optional
            The border color when a button is unselected (default is "#3b3b3b").
        border_color_disabled_selected : str, optional
            The border color when a button is disabled and selected (default is "#3b3b3b").
        border_color_disabled_unselected : str, optional
            The border color when a button is disabled and unselected (default is "#3b3b3b").
        bg_color_hover : str, optional
            The background color when a button is hovered (default is "#0053a4").
        bg_color_pressed : str, optional
            The background color when a button is pressed (default is "#003d7a").
        parent : Optional[QWidget], optional
            The parent widget of the `SelectButtonGroup` (default is None).
            
            
        Signals
        -------
        selected : pyqtSignal(str)
            Emitted when a button is selected, providing its key.
            
    """

    
    selected = pyqtSignal(str)

    def __init__(
        self,
        button_configs: List[Tuple[str, str, str]],
        layout_type: str = "horizontal",
        layout_options: Optional[dict] = None,
        default_selected: Optional[str] = None,
        icon_size: Optional[QSize] = None,
        fg_color_selected: str = "#ffffff",
        fg_color_unselected: str = "#ffffff",
        fg_color_disabled_selected: str = "#ffffff",
        fg_color_disabled_unselected: str = "#ffffff",
        bg_color_selected: str = "#11468F",
        bg_color_unselected: str = "transparent",
        bg_color_disabled_selected: str = "#3c3c3c",
        bg_color_disabled_unselected: str = "transparent",
        border_color_selected: str = "transparent",
        border_color_unselected: str = "#3b3b3b",
        border_color_disabled_selected: str = "#3b3b3b",
        border_color_disabled_unselected: str = "#3b3b3b",
        bg_color_hover: str = "#0053a4",
        bg_color_pressed: str = "#003d7a",      
        parent: Optional[QWidget] = None
    ) -> None:
        super().__init__(parent)
        self.button_configs = button_configs
        self.default_selected = default_selected
        self.icon_size = icon_size
        self.layout_type = layout_type
        self.layout_options = layout_options or {}
        self.buttons: List[Tuple[SelectButton, str]] = []
        self.fg_color_selected = fg_color_selected
        self.fg_color_unselected = fg_color_unselected
        self.fg_color_disabled_selected = fg_color_disabled_selected
        self.fg_color_disabled_unselected = fg_color_disabled_unselected
        self.bg_color_selected = bg_color_selected
        self.bg_color_unselected = bg_color_unselected
        self.bg_color_disabled_selected = bg_color_disabled_selected
        self.bg_color_disabled_unselected = bg_color_disabled_unselected
        self.border_color_selected = border_color_selected
        self.border_color_unselected = border_color_unselected
        self.border_color_disabled_selected = border_color_disabled_selected
        self.border_color_disabled_unselected = border_color_disabled_unselected
        self.bg_color_hover = bg_color_hover
        self.bg_color_pressed = bg_color_pressed
        self._create_layout()
        self._create_buttons()

    def _create_layout(self) -> None:
        if self.layout_type == "horizontal":
            self.layout = QHBoxLayout()
        elif self.layout_type == "vertical":
            self.layout = QVBoxLayout()
        elif self.layout_type == "grid":
            self.layout = QGridLayout()
            rows = self.layout_options.get("rows", 1)
            columns = self.layout_options.get("columns", len(self.button_configs))
            self.layout.setRowStretch(rows - 1, 1)
            self.layout.setColumnStretch(columns - 1, 1)
        else:
            raise ValueError(f"Unsupported layout type: {self.layout_type}")
        self.layout.setSpacing(self.layout_options.get("spacing", 0))
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def _create_buttons(self) -> None:
        for index, (text, key, icon_path) in enumerate(self.button_configs):
            button = SelectButton(
                text=text,
                icon=icon_path,
                icon_size=self.icon_size,
                fg_color_selected=self.fg_color_selected,
                fg_color_unselected=self.fg_color_unselected,
                fg_color_disabled_selected=self.fg_color_disabled_selected,
                fg_color_disabled_unselected=self.fg_color_disabled_unselected,
                bg_color_selected=self.bg_color_selected,
                bg_color_unselected=self.bg_color_unselected,
                bg_color_disabled_selected=self.bg_color_disabled_selected,
                bg_color_disabled_unselected=self.bg_color_disabled_unselected,
                border_color_selected=self.border_color_selected,
                border_color_unselected=self.border_color_unselected,
                border_color_disabled_selected=self.border_color_disabled_selected,
                border_color_disabled_unselected=self.border_color_disabled_unselected,
                bg_color_hover=self.bg_color_hover,
                bg_color_pressed=self.bg_color_pressed,
            )
            self.buttons.append((button, key))
            
            if self.layout_type == "grid":
                row = index // self.layout_options.get("columns", 1)
                column = index % self.layout_options.get("columns", 1)
                self.layout.addWidget(button, row, column)
            else:
                self.layout.addWidget(button)

            button.clicked.connect(lambda _, k=key: self._on_button_clicked(k))
            button.set_selected(self.default_selected == key)

    def _on_button_clicked(self, key: str) -> None:
        for button, bkey in self.buttons:
            button.set_selected(bkey == key)
        self.selected.emit(key)    
        
    
    def toggle_enable_state(self, state: bool):
        """
        Enable or disable all buttons.

        Parameters
        ----------
        state : bool
            Whether to enable (True) or disable (False) the buttons.
        """
        for button, _ in self.buttons:
            if button is not None and isinstance(button, SelectButton):
                button.setEnabled(state)
                

    def toggle_visible_state(self, state: bool):
        """
        Show or hide all buttons.

        Parameters
        ----------
        state : bool
            Whether to show (True) or hide (False) the buttons.
        """
        for button, _ in self.buttons:
            if button is not None and isinstance(button, SelectButton):
                button.setVisible(state) 
            

