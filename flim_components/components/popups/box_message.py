from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from components.popups.popup import Popup
from styles.popups_styles import PopupsStyles


class MessageBox(Popup):
    """
    A customizable message box for displaying messages to the user.
    This class provides a static method to create and show a message box with
    customizable title, message, icon, and stylesheet.
    """
    @staticmethod
    def show(title: str, message: str, icon: QIcon, stylesheet: str = None):
        """
        Create and show a message box with the specified parameters.

        Parameters
        ----------
        title : str
            The title of the message box window.
        message : str
            The message to be displayed in the message box.
        icon : QIcon
            The icon to be displayed in the message box.
        stylesheet : str, optional
            The CSS stylesheet to apply to the message box. If not provided, default styling is used.
        """

        message_box = QMessageBox()
        message_box.setIcon(icon)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setStyleSheet(
            stylesheet if stylesheet is not None else PopupsStyles.message_box_style()
        )
        message_box.exec()


class CriticalMessage(MessageBox):
    """
    A message box specifically for displaying critical error messages.
    Uses the Critical icon and allows for additional styling customization.
    """

    @staticmethod
    def show(title: str, message: str, stylesheet: str = None):
        """
        Create and show a critical message box with the specified parameters.

        Parameters
        ----------
        title : str
            The title of the message box window.
        message : str
            The message to be displayed in the message box.
        stylesheet : str, optional
            The CSS stylesheet to apply to the message box. If not provided,
            default styling is used.
        """
        MessageBox.show(
            title,
            message,
            QMessageBox.Icon.Critical,
            stylesheet
        )


class WarningMessage(MessageBox):
    """
    A message box specifically for displaying warning messages.
    Uses the Warning icon and allows for additional styling customization.
    """

    @staticmethod
    def show(title: str, message: str, stylesheet: str = None):
        """
        Create and show a warning message box with the specified parameters.

        Parameters
        ----------
        title : str
            The title of the message box window.
        message : str
            The message to be displayed in the message box.
        stylesheet : str, optional
            The CSS stylesheet to apply to the message box. If not provided,
            default styling is used.
        """
        MessageBox.show(
            title,
            message,
            QMessageBox.Icon.Warning,
            stylesheet
        )


class InformationMessage(MessageBox):
    """
    A message box specifically for displaying informational messages.
    Uses the Information icon and allows for additional styling customization.
    """

    @staticmethod
    def show(title: str, message: str, stylesheet: str = None):
        """
        Create and show an informational message box with the specified parameters.

        Parameters
        ----------
        title : str
            The title of the message box window.
        message : str
            The message to be displayed in the message box.
        stylesheet : str, optional
            The CSS stylesheet to apply to the message box. If not provided,
            default styling is used.
        """
        MessageBox.show(
            title,
            message,
            QMessageBox.Icon.Information,
            stylesheet
        )
