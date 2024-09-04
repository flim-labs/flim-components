from PyQt6.QtWidgets import QLayout

class CompactLayout:
    """
    A utility class to compact a given QLayout by setting its spacing and content margins to 0.

    Parameters
    ----------
    layout : QLayout
        The layout to be compacted.
    """

    def __init__(self, layout: QLayout):
        """
        Initialize the CompactLayout with the provided layout.

        Parameters
        ----------
        layout : QLayout
            The layout to be compacted.
        """
        self.layout = layout
        self._apply_compact_settings()

    def _apply_compact_settings(self):
        """
        Apply compact settings to the layout, setting spacing and content margins to 0.
        """
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)