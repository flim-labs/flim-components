class LayoutUtils:
    """
    A utility class providing static methods for manipulating layouts in PyQt6.
    """

    @staticmethod
    def hide_layout(layout):
        """
        Recursively hide all widgets within a given layout.

        Parameters
        ----------
        layout : QLayout
            The layout whose widgets and nested layouts will be hidden.

        Notes
        -----
        This method traverses the layout and hides all widgets contained within it.
        It also recursively hides widgets in any nested layouts.
        """
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().hide()
            elif item.layout():
                LayoutUtils.hide_layout(item.layout())

    @staticmethod
    def show_layout(layout):
        """
        Recursively show all widgets within a given layout.

        Parameters
        ----------
        layout : QLayout
            The layout whose widgets and nested layouts will be shown.

        Notes
        -----
        This method traverses the layout and shows all widgets contained within it.
        It also recursively shows widgets in any nested layouts.
        """
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().show()
            elif item.layout():
                LayoutUtils.show_layout(item.layout())

    @staticmethod
    def clear_layout(layout):
        """
        Recursively remove all widgets and sub-layouts from a given layout.

        Parameters
        ----------
        layout : QLayout
            The layout to be cleared of all widgets and sub-layouts.

        Notes
        -----
        This method removes and deletes all widgets and sub-layouts from the specified
        layout. It also ensures that any memory associated with the removed items is
        properly cleaned up by calling `deleteLater()` on them.
        """
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    sub_layout = item.layout()
                    if sub_layout is not None:
                        LayoutUtils.clear_layout(sub_layout)
            layout.deleteLater()
