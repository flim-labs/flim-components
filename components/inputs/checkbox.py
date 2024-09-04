from PyQt6.QtWidgets import QWidget, QCheckBox
from PyQt6.QtCore import Qt
from styles.inputs_styles import InputStyles

class Checkbox(QCheckBox):
    """
    A customizable checkbox that extends QCheckBox, offering options for 
    customizing colors, label text, initial state, and overall appearance.

    Parameters
    ----------
    key : int
        A unique identifier for the checkbox, useful for distinguishing between 
        different checkboxes when handling events.
    label : str
        The text displayed next to the checkbox, providing a description or label 
        for the checkbox.
    event_callback : callable
        The function to be called whenever the checkbox's state changes.
    checked : bool, optional
        The initial checked state of the checkbox. Defaults to False.
    enabled : bool, optional
        Whether the checkbox is enabled (True) or disabled (False). Defaults to True.
    visible : bool, optional
        Whether the checkbox is visible (True) or hidden (False). Defaults to True.
    checkbox_color : str, optional
        The color of the checkbox when it is checked. Defaults to "#1E90FF".
    checkbox_color_unchecked : str, optional
        The color of the checkbox when it is unchecked. Defaults to "#6b6a6a".
    label_color : str, optional
        The color of the label text. Defaults to "#f8f8f8".
    border_color : str, optional
        The color of the checkbox border. Defaults to "#252525".
    stylesheet : str, optional
        An optional stylesheet for further customizing the checkbox's appearance. 
        If not provided, a default style will be applied. Defaults to None.
    parent : QWidget, optional
        The parent widget of this checkbox. Defaults to None.
    """

    def __init__(
        self,
        key: int,
        label: str,
        event_callback,
        checked: bool = False,
        enabled: bool = True,
        visible: bool = True,
        checkbox_color: str = "#1E90FF",
        checkbox_color_unchecked: str = "#6b6a6a",
        label_color: str = "#f8f8f8",
        border_color: str = "#252525",
        stylesheet: str | None = None,
        parent: QWidget = None,
    ):
        super().__init__(label, parent)
        self.key = key
        self.label = label
        self.checkbox_color = checkbox_color
        self.checkbox_color_unchecked = checkbox_color_unchecked
        self.label_color = label_color
        self.border_color = border_color
        self.setChecked(checked)
        self.setEnabled(enabled)
        self.setVisible(visible)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.set_style(stylesheet)
        self.stateChanged.connect(event_callback)

    def set_style(self, stylesheet: str | None):
        """
        Apply the provided stylesheet or the default checkbox style.

        Parameters
        ----------
        stylesheet : str, optional
            The stylesheet string to apply to the checkbox. If not provided, 
            a default style based on the provided colors will be applied.
        """
        self.setStyleSheet(
            stylesheet
            if stylesheet is not None
            else InputStyles.checkbox_style(
                self.checkbox_color,
                self.checkbox_color_unchecked,
                self.label_color,
                self.border_color,
            )
        )
