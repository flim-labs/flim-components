import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from flim_components.components.buttons.collapse_button import CollapseButton
from flim_components.utils.resource_path import get_asset_path


class CollapseButtonExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Collapse Button Example")
        self.setStyleSheet("background-color: #121212;")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout(self)

        # Create a collapsible widget
        self.collapsible_widget = QLabel(
            "This is the content inside the collapsible widget.\n"
            "It can be expanded or collapsed using the button below."
        )
        self.collapsible_widget.setStyleSheet(
            "background-color: blue; color: white; padding: 10px;"
        )

        expanded_icon = get_asset_path("assets/arrow-up-dark-grey.png")
        collapsed_icon = get_asset_path("assets/arrow-down-dark-grey.png")

        # Create the collapse button
        self.collapse_button = CollapseButton(
            collapsible_widget=self.collapsible_widget,
            expanded_icon=expanded_icon,
            collapsed_icon=collapsed_icon,
            width=50,
            height=50,
            enabled=True,
            visible=True,
            expanded=True,
            border_radius="45px",
        )

        # Add widgets to layout
        layout.addWidget(self.collapsible_widget)
        layout.addWidget(self.collapse_button)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

        # Connect the collapse button to the toggle function
        self.collapse_button.collapse_button.clicked.connect(
            self.collapse_button.toggle_collapsible_widget
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CollapseButtonExampleWindow()
    window.show()
    app.exec()
