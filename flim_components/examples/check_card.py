import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

from flim_components.components.misc.check_card import CheckCardWidget
from flim_components.layouts.compact_layout import CompactLayout


class CheckCardWidgetExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Check Card Widget Example")
        self.setStyleSheet("background-color: #121212; color: white;")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        widget_container = QWidget()
        widget_container.setFixedHeight(50)
        container_layout = CompactLayout(QVBoxLayout())
        self.check_card_widget = CheckCardWidget(button_height=50)
        self.check_card_widget.check_button.clicked.connect(self.update_card_status)
        container_layout.addWidget(self.check_card_widget)
        widget_container.setLayout(container_layout)
        layout.addWidget(widget_container)
   
        layout.addStretch()
        self.update_card_status()
        self.setLayout(layout)


    def update_card_status(self):
        from random import randint
        error = randint(0, 1) == 1
        card_id = randint(1000, 9999) 
        if error:
            self.check_card_widget.update_message(
                "Card Not Found",
                error=True,
                message_color="#ff4d4d",
                bg_color="#242424",
                border_color="#ff4d4d",
            )
        else:
            self.check_card_widget.update_message(
                f"{card_id}",
                error=False,
                message_color="#285da6",
                bg_color="#242424",
                border_color="#285da6",
            )



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckCardWidgetExampleWindow()
    window.show()
    sys.exit(app.exec())
