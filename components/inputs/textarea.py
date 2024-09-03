from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPlainTextEdit, QWidget

from styles.inputs_styles import InputStyles


class TextArea(QWidget):
    """
    A widget for multi-line text input with a label, customizable layout, and optional placeholder text.
    This widget also supports character limit enforcement.

    Parameters
    ----------
    label : str
        The text to be displayed as the label for the text area.
    placeholder : str, optional
        The placeholder text to display when the text area is empty (default is None).
    event_callback : callable
        A function that is called whenever the text area content changes.
    max_chars : int, optional
        The maximum number of characters allowed in the text area (default is None).
    layout_type : str, optional
        The layout type for the text area and label, either "vertical" (default) or "horizontal".
    text : str, optional
        The initial text to set in the text area (default is an empty string).
    width : int, optional
        The default fixed textarea width (default is None).          
    stylesheet : str, optional
        An optional stylesheet to customize the appearance of the text area (default is None).
    parent : QWidget, optional
        The parent widget of this text area control, if any (default is None).
    """

    def __init__(
        self,
        label: str,
        event_callback,
        max_chars: int | None = None,
        placeholder: str | None = None,
        layout_type: str = "vertical",
        text: str = "",
        width: int | None = None,
        stylesheet: str | None = None,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.max_chars = max_chars
        self.q_label = QLabel(label)
        self.control_layout = (
            QVBoxLayout() if layout_type == "vertical" else QHBoxLayout()
        )
        self.textarea = QPlainTextEdit()
        self.textarea.setPlaceholderText(placeholder)
        self.textarea.setPlainText(text)
        self.textarea.textChanged.connect(self.limit_characters)
        self.textarea.textChanged.connect(event_callback)
        if width is not None:
            self.setFixedWidth(width)
        self.set_style(
            stylesheet if stylesheet is not None else InputStyles.input_text_style()
        )
        self.control_layout.addWidget(self.q_label)
        self.control_layout.addWidget(self.textarea)
        self.setLayout(self.control_layout)

    def set_style(self, stylesheet: str):
        """
        Apply a custom stylesheet to the text area widget.

        Parameters
        ----------
        stylesheet : str
            The stylesheet string to apply to the text area widget.
        """
        self.textarea.setStyleSheet(stylesheet)

    def get_text(self) -> str:
        """
        Get the current text of the text area.

        Returns
        -------
        str
            The current text in the text area widget.
        """
        return self.textarea.toPlainText()

    def set_text(self, text: str):
        """
        Set new text for the text area widget.

        Parameters
        ----------
        text : str
            The new text to set in the text area widget.
        """
        self.textarea.setPlainText(text)

    def clear_text(self):
        """
        Clear the text in the text area widget.
        """
        self.textarea.clear()

    def toggle_enable_state(self, state: bool):
        """
        Enable or disable the text area widget.

        Parameters
        ----------
        state : bool
            If True, enables the text area widget; if False, disables it.
        """
        self.textarea.setEnabled(state)

    def toggle_visible_state(self, state: bool):
        """
        Show or hide the text area widget.

        Parameters
        ----------
        state : bool
            If True, makes the text area widget visible; if False, hides it.
        """
        self.textarea.setVisible(state)

    def is_enabled(self) -> bool:
        """
        Check if the text area widget is enabled.

        Returns
        -------
        bool
            True if the text area widget is enabled, False otherwise.
        """
        return self.textarea.isEnabled()

    def set_label_text(self, text: str):
        """
        Set the text for the label associated with the text area widget.

        Parameters
        ----------
        text : str
            The text to display on the label.
        """
        self.q_label.setText(text)

    def set_tooltip(self, text: str):
        """
        Set a tooltip for the text area widget.

        Parameters
        ----------
        text : str
            The text to display as a tooltip when the user hovers over the text area widget.
        """
        self.textarea.setToolTip(text)

    def limit_characters(self):
        self.textarea.textChanged.disconnect(self.limit_characters)
        """
        Limit the number of characters in the text area to the maximum allowed.
        """
        if self.max_chars is None:
            return
        current_text = self.textarea.toPlainText()
        if len(current_text) > self.max_chars:
            # Truncate the text and update the text area
            text = self.textarea.toPlainText()
            cursor_pos = self.textarea.textCursor().position()
            truncated_text = text[:self.max_chars]
            selected_text = text[cursor_pos:]
            truncated_text += selected_text
            self.textarea.setPlainText(truncated_text)
            cursor = self.textarea.textCursor()
            cursor.setPosition(len(truncated_text))
            self.textarea.setTextCursor(cursor)            
        self.textarea.textChanged.connect(self.limit_characters)    
