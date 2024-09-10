from PyQt6.QtGui import QColor, QPalette, QFont
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QLabel


class AppThemeStyles:
   
    @staticmethod        
    def customize_theme(window, bg = QColor(28, 28, 28, 128), fg = QColor(255, 255, 255)):
        palette = QPalette()
        background_color = bg
        palette.setColor(QPalette.ColorRole.Window, background_color)
        palette.setColor(QPalette.ColorRole.WindowText, fg)
        window.setPalette(palette)  
        window.setStyleSheet(
            """
        QLabel {
            color: #f8f8f8;
            font-family: "Montserrat";
        }
        """
        )  

    @staticmethod
    def set_fonts(font_name="Montserrat", font_size=10):
        general_font = QFont("Montserrat", 10)
        QApplication.setFont(general_font)

    @staticmethod
    def set_fonts_deep(root):
        if root is None:
            return
        for child in root.findChildren(QWidget):
            if child.objectName() == "font":
                child.setFont(QFont("Montserrat", 14, QFont.Weight.Thin))
            if child.metaObject().className() == "QPushButton":
                child.setFont(QFont("Montserrat", 14, QFont.Weight.Thin))
            AppThemeStyles.set_fonts_deep(child)
        for child in root.findChildren(QLabel):
            child.setFont(QFont("Montserrat", 14, QFont.Weight.Bold))
            AppThemeStyles.set_fonts_deep(child)   