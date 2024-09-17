from typing import Literal, Optional
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QSizePolicy

from flim_components.layouts.compact_layout import CompactLayout

class LayoutSeparator(QWidget):
    """
    A customizable layout separator widget, used to visually separate sections 
    in a layout with a horizontal or vertical line and optional spacing.

    Parameters
    ----------
    line_width : int, optional
        The thickness of the separator line. Default is 1.
    color : str, optional
        The color of the separator line in hex format. Default is "#282828".
    horizontal_space : int, optional
        The width of the spacer in the horizontal direction (for spacing around the separator). Default is 1.
    vertical_space : int, optional
        The height of the spacer in the vertical direction (for spacing around the separator). Default is 10.
    layout_type : Literal["horizontal", "vertical"], optional
        The type of layout separator: "horizontal" for a horizontal line, 
        or "vertical" for a vertical line. Default is "horizontal".
    visible : bool, optional
        If True, the separator is initially visible. Default is True.
    parent : Optional[QWidget], optional
        The parent widget, if any. Default is None.
    """

    def __init__(
        self,
        line_width: int = 1,
        color: str = "#282828",
        horizontal_space: int = 1,
        vertical_space: int = 10,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        visible: bool = True,
        parent: Optional["QWidget"] = None,
    ):
        super().__init__(parent)
        self.layout = CompactLayout(QVBoxLayout())
        
        spacer = QWidget()
        spacer.setFixedSize(horizontal_space, vertical_space)

        separator = QFrame()
        if layout_type == 'horizontal':
            separator.setFrameShape(QFrame.Shape.HLine)
        else: 
            separator.setFrameShape(QFrame.Shape.VLine)    
        separator.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        separator.setLineWidth(line_width)
        separator.setStyleSheet(f"QFrame{{color: {color};}}")
     
        self.layout.addWidget(spacer)
        self.layout.addWidget(separator)

        self.setLayout(self.layout)
        self.set_visible(visible)
        
    def set_visible(self, visible: bool):
        """
        Show or hide the layout separator.

        Parameters
        ----------
        visible : bool
            If True, makes the layout separator visible; if False, hides it.
        """
        self.setVisible(visible)
