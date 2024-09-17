from PyQt6.QtWidgets import QWidget, QLabel
from typing import List, Optional
import numpy as np
from flim_components.styles.SBR_styles import SBRStyles
from flim_components.utils.flim_utils import FlimUtils


class SBRWidget(QLabel):
    """
    A widget for displaying the Signal-to-Background Ratio (SBR).

    This widget shows the SBR value as a label, with customizable text, font size, background color,
    foreground color, and visibility. It also updates the SBR value based on input data.

    Parameters
    ----------
    text : str, optional
        The initial text to be displayed on the label (default is "0 SBR").
    font_size : str, optional
        The font size of the text (default is "22px").
    bg_color : str, optional
        The background color of the label (default is "#0a0a0a").
    fg_color : str, optional
        The foreground (text) color of the label (default is "#f72828").
    visible : bool, optional
        Whether the label is visible or hidden (default is True).
    parent : Optional[QWidget], optional
        The parent widget of the label, if any (default is None).
    """

    def __init__(
        self,
        text: str = "0 SBR",
        font_size: str = "22px",
        bg_color: str = "#0a0a0a",
        fg_color: str = "#f72828",
        visible: bool = True,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.setText(text)
        self.set_style(bg_color, fg_color, font_size)
        if not visible:
            self.hide()

    def update_SBR(self, y_data: np.ndarray | List[int] | List[float], decimals: int = 2) -> None:
        """
        Update the SBR value displayed on the label based on new data.

        This method calculates the SBR value from the input data and updates the text of the label
        to display the new SBR value with a customizable number of decimal places.

        Parameters
        ----------
        y_data : np.ndarray | List[int] | List[float]
            The input data for which the SBR is calculated. Can be a numpy array, or a list of integers or floats.
        decimals : int, optional
            The number of decimal places to display in the SBR value (default is 2).
        """
        SBR_value = FlimUtils.calculate_SBR(np.array(y_data))
        self.setText(f"{SBR_value:.{decimals}f} SBR")
        

    def set_style(self, bg_color: str, fg_color: str, font_size: str) -> None:
        """
        Set the style of the label including background color, foreground color, and font size.

        Parameters
        ----------
        bg_color : str
            The background color of the label.
        fg_color : str
            The foreground (text) color of the label.
        font_size : str
            The font size of the text.
        """
        self.setStyleSheet(SBRStyles.SBR_label_style(fg_color, bg_color, font_size))

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the label.

        Parameters
        ----------
        visible : bool
            Whether the label should be visible or hidden.
        """
        self.setVisible(visible)
