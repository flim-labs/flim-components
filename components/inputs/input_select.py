from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QWidget
from typing import List, Callable, Optional

from styles.inputs_styles import InputStyles


class InputSelect(QWidget):
    """
    A widget for a dropdown menu with a label, customizable layout, and options.

    Parameters
    ----------
    label : str
        The text to be displayed as the label for the dropdown menu.
    selected_value : int
        The index of the initially selected option in the dropdown menu.
    options : List[str]
        A list of strings representing the options to display in the dropdown menu.
    event_callback : Callable[[int], None]
        A function that is called whenever the selected index in the dropdown menu changes.
    layout_type : str, optional
        The layout type for the dropdown menu and label, either "vertical" (default) or "horizontal".
    stylesheet : str, optional
        An optional stylesheet to customize the appearance of the dropdown menu (default is None).        
    width : int, optional
        The fixed width of the dropdown menu, if any (default is None).
    parent : QWidget, optional
        The parent widget of this control, if any (default is None).
    """
    
    def __init__(
        self,
        label: str,
        selected_value: int,
        options: List[str],
        event_callback: Callable[[int], None],
        layout_type: str = "vertical",
        stylesheet: str | None = None,
        width: Optional[int] = None,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.q_label = QLabel(label)
        self.control_layout = (
            QVBoxLayout() if layout_type == "vertical" else QHBoxLayout()
        )
        self.dropdown = QComboBox()
        if width is not None:
            self.dropdown.setFixedWidth(width)
        for option in options:
            self.dropdown.addItem(option)
        self.dropdown.setCurrentIndex(selected_value)
        self.dropdown.currentIndexChanged.connect(event_callback)
        self.dropdown.setStyleSheet(stylesheet if stylesheet is not None else InputStyles.input_select_style())
        self.control_layout.addWidget(self.q_label)
        self.control_layout.addWidget(self.dropdown)
        self.setLayout(self.control_layout)

    def get_selected_index(self) -> int:
        """
        Get the index of the currently selected option in the dropdown menu.

        Returns
        -------
        int
            The index of the selected option.
        """
        return self.dropdown.currentIndex()

    def set_selected_index(self, index: int):
        """
        Set the selected index of the dropdown menu.

        Parameters
        ----------
        index : int
            The index of the option to select.
        """
        self.dropdown.setCurrentIndex(index)
        
    def add_option(self, option: str):
        """
        Add a new option to the dropdown menu.

        Parameters
        ----------
        option : str
            The new option to add to the dropdown menu.
        """
        self.dropdown.addItem(option)        
        

    def add_options(self, options: List[str], clear: bool = False):
        """
        Add a new options to the dropdown menu.

        Parameters
        ----------
        options : List[str]
            The new options to add to the dropdown menu.
        clear: bool
            If a preventive cleaning of the existing options is necessary (default is False)  
        """
        if clear:
            self.dropdown.clear()
        for option in options:    
            self.dropdown.addItem(option)

    def remove_option(self, index: int):
        """
        Remove an option from the dropdown menu by its index.

        Parameters
        ----------
        index : int
            The index of the option to remove.
        """
        self.dropdown.removeItem(index)
        

    def toggle_enable_state(self, state):
        """
        Enable or disable the input widget.

        Parameters
        ----------
        state : bool
            If True, enables the input widget; if False, disables it.
        """        
        self.dropdown.setEnabled(state) 
        
        
    def toggle_visible_state(self, state):
        """
        Show or hide the input widget.

        Parameters
        ----------
        state : bool
            If True, makes the input widget visible; if False, hides it.
        """        
        self.dropdown.setVisible(state)             

    def is_enabled(self) -> bool:
        """
        Check if the input widget is enabled.

        Returns
        -------
        bool
            True if the input widget is enabled, False otherwise.
        """        
        return self.dropdown.isEnabled()        


    def set_label_text(self, text: str):
        """
        Set the text for the label associated with the dropdown menu.

        Parameters
        ----------
        text : str
            The text to display on the label.
        """
        self.q_label.setText(text)

    def set_tooltip(self, text: str):
        """
        Set a tooltip for the dropdown menu.

        Parameters
        ----------
        text : str
            The text to display as a tooltip when the user hovers over the dropdown menu.
        """
        self.dropdown.setToolTip(text)
