from typing import Literal
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget

from flim_components.styles.inputs_styles import InputStyles
from flim_components.utils.layout_utils import LayoutUtils

class InputText(QWidget):
    """
    A widget for single-line text input with a label, customizable layout, and optional placeholder text.

    Parameters
    ----------
    label : str
        The text to be displayed as the label for the input.
    placeholder : str, optional
        The placeholder text to display when the input is empty (default is None).
    event_callback : callable
        A function that is called whenever the input text changes.
    enabled : bool, optional
        Whether the input field is initially enabled (default is True).
    visible : bool, optional
        Whether the widget is initially visible (default is True).               
    layout_type : Literal ["horizontal", "vertical"], optional
        The layout type for the input and label, either "vertical" (default) or "horizontal".
    text : str, optional
        The initial text to set in the input field (default is an empty string).
    width : int, optional
        The default fixed input field width (default is None).        
    stylesheet : str, optional
        An optional stylesheet to customize the appearance of the input widget (default is None).
    parent : QWidget, optional
        The parent widget of this input control, if any (default is None).
    """

    def __init__(
        self,
        label: str,
        event_callback,
        enabled: bool = True,
        visible: bool = True,
        placeholder: str | None = None,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        text: str = "",
        width: int | None = None,
        stylesheet: str | None = None,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.q_label = QLabel(label)
        self.control_layout = (
            QVBoxLayout() if layout_type == "vertical" else QHBoxLayout()
        )
        self.input = QLineEdit()
        if placeholder is not None:
            self.input.setPlaceholderText(placeholder)
        self.input.setText(text)
        self.input.textChanged.connect(event_callback)
        if width is not None:
            self.input.setFixedWidth(width)
        self.set_style(
            stylesheet if stylesheet is not None else InputStyles.input_text_style()
        )
        self.control_layout.addWidget(self.q_label)
        self.control_layout.addWidget(self.input)
        self.setLayout(self.control_layout)
        self.set_enabled(enabled)
        self.set_visible(visible)

    def set_style(self, stylesheet: str):
        """
        Apply a custom stylesheet to the input widget.

        Parameters
        ----------
        stylesheet : str
            The stylesheet string to apply to the input widget.
        """
        self.input.setStyleSheet(stylesheet)

    def get_text(self) -> str:
        """
        Get the current text of the input.

        Returns
        -------
        str
            The current text in the input widget.
        """
        return self.input.text()

    def set_text(self, text: str):
        """
        Set new text for the input widget.

        Parameters
        ----------
        text : str
            The new text to set in the input widget.
        """
        self.input.setText(text)

    def clear_text(self):
        """
        Clear the text in the input widget.
        """
        self.input.clear()

    def set_enabled(self, state: bool):
        """
        Enable or disable the input widget.

        Parameters
        ----------
        state : bool
            If True, enables the input widget; if False, disables it.
        """
        self.input.setEnabled(state)

    def set_visible(self, state):
        """
        Show or hide the control layout and all its child widgets.

        Parameters
        ----------
        state : bool
            If True, makes the control layout visible; if False, hides it.
        """
        if state:
            LayoutUtils.show_layout(self.control_layout)
        else:
            LayoutUtils.hide_layout(self.control_layout)    

    def is_enabled(self) -> bool:
        """
        Check if the input widget is enabled.

        Returns
        -------
        bool
            True if the input widget is enabled, False otherwise.
        """
        return self.input.isEnabled()

    def set_label_text(self, text: str):
        """
        Set the text for the label associated with the input widget.

        Parameters
        ----------
        text : str
            The text to display on the label.
        """
        self.q_label.setText(text)

    def set_tooltip(self, text: str):
        """
        Set a tooltip for the input widget.

        Parameters
        ----------
        text : str
            The text to display as a tooltip when the user hovers over the input widget.
        """
        self.input.setToolTip(text)
