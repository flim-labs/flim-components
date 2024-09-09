
from PyQt6.QtGui import QGuiApplication, QCursor
from PyQt6.QtWidgets import QWidget


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

    @staticmethod
    def center_window(window: QWidget) -> None:
        """
        Centers the given window on a specified screen. 

        Parameters:
        ----------
        window : QWidget
            The window to be centered. It must be a QWidget or subclass thereof.
        """
        # Determine which screen to use
        screen_number = LayoutUtils.get_current_screen()
        if screen_number == -1:
            screen = QGuiApplication.primaryScreen()
        else:
            screen = QGuiApplication.screens()[screen_number]        
        # Get the screen and window geometry
        screen_geometry = screen.geometry()
        window_geometry = window.frameGeometry()
        # Center the window on the screen
        screen_center = screen_geometry.center()
        window_geometry.moveCenter(screen_center)
        window.move(window_geometry.topLeft())
    
    @staticmethod
    def get_current_screen() -> int:
        """
        Determines the index of the screen currently under the cursor.

        The function checks the position of the cursor and determines which of the available screens 
        contains the cursor. It iterates through all connected screens and returns the index of the 
        screen that contains the cursor. If the cursor is not over any screen, it returns -1.

        Returns:
        -------
        int
            The index of the screen containing the cursor, or -1 if no screen contains the cursor.
        """
        cursor_pos = QCursor.pos()
        screens = QGuiApplication.screens()
        for screen_number, screen in enumerate(screens):
            if screen.geometry().contains(cursor_pos):
                return screen_number
        return -1