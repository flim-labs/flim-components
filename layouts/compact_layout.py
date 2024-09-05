from PyQt6.QtWidgets import QLayout, QLayoutItem, QWidget
from PyQt6.QtCore import QSize, QRect

class CompactLayout(QLayout):
    """
    A compact layout that extends QLayout and applies compact settings
    by setting its spacing and content margins to 0.
    """

    def __init__(self, layout: QLayout):
        super().__init__()
        self.layout = layout
        self._apply_compact_settings()

    def _apply_compact_settings(self):
        """
        Apply compact settings to the layout, setting spacing and content margins to 0.
        """
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def addItem(self, item: QLayoutItem) -> None:
        """
        Add a layout item to the layout.
        """
        self.layout.addItem(item)

    def itemAt(self, index: int) -> QLayoutItem | None:
        """
        Get the layout item at the given index.
        """
        return self.layout.itemAt(index)

    def takeAt(self, index: int) -> QLayoutItem | None:
        """
        Take the layout item at the given index.
        """
        return self.layout.takeAt(index)

    def setGeometry(self, rect: QRect) -> None:
        """
        Set the geometry of the layout.
        """
        super().setGeometry(rect)
        self.layout.setGeometry(rect)

    def sizeHint(self) -> QSize:
        """
        Return the size hint of the layout.
        """
        return self.layout.sizeHint()

    def minimumSize(self) -> QSize:
        """
        Return the minimum size of the layout.
        """
        return self.layout.minimumSize()

    def addWidget(self, widget: QWidget) -> None:
        """
        Add a widget to the layout.
        """
        self.layout.addWidget(widget)

    def addLayout(self, layout: QLayout) -> None:
        """
        Add a layout to the layout.
        """
        self.layout.addLayout(layout)

    def count(self) -> int:
        """
        Return the number of items in the layout.
        """
        return self.layout.count()