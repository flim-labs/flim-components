class ButtonStyles:
    @staticmethod
    def base_button_style(
        fg_color: str,
        bg_color_base: str,
        border_color: str,
        bg_color_hover: str,
        bg_color_pressed: str,
        bg_color_disabled: str,
        border_color_disabled: str,
        fg_color_disabled: str,
    ):
        return f"""
            QPushButton {{
                background-color: {bg_color_base};
                border: 1px solid {border_color};
                font-family: "Montserrat";
                color: {fg_color};
                letter-spacing: 0.1em;
                padding: 8px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {bg_color_hover};
                border: 2px solid {bg_color_hover};
            }}
            QPushButton:focus {{
                background-color: {bg_color_pressed};
                border: 2px solid {bg_color_pressed};
            }}
            QPushButton:pressed {{
                background-color: {bg_color_pressed};
                border: 2px solid {bg_color_pressed};
            }}
            QPushButton:disabled {{
                background-color: {bg_color_disabled};
                border: 2px solid {border_color_disabled};
                color: {fg_color_disabled};
            }}
        """

    @staticmethod
    def toggle_button_style(
        fg_color: str, bg_color: str, is_first: bool = False, is_last: bool = False
    ) -> str:
        border_radius_styles = ""

        if is_first:
            border_radius_styles += """
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
            """
        if is_last:
            border_radius_styles += """
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            """

        return f"""
        QPushButton {{
            font-family: "Montserrat";
            letter-spacing: 0.1em;
            padding: 10px 12px;
            font-size: 14px;
            font-weight: bold;
            min-width: 60px;
            color: {fg_color};
            background-color: {bg_color};
            {border_radius_styles}
        }}
        """

    @staticmethod
    def collapse_button_style(
        bg_color: str, border_color: str, border_radius: str, icon_size: str
    ):
        return f"""
            QPushButton{{
                background-color: {bg_color};
                border-radius: {border_radius};
                qproperty-iconSize: {icon_size};
                border: 1px solid {border_color};
            }}
        """

    @staticmethod
    def select_button_style(
        fg_color: str,
        bg_color_base: str,
        bg_color_hover: str,
        bg_color_pressed: str,
        border_color: str,
    ):
        return f"""
            QPushButton {{
                font-family: "Montserrat";
                font-size: 12px;
                font-weight: thin;
                border: 1px solid {border_color};
                border-radius: 0px;
                height: 20px;
                color: {fg_color};
                padding: 5px;
                background-color: {bg_color_base};
            }}
            QPushButton:hover {{
                background-color: {bg_color_hover};
            }}
            QPushButton:pressed {{
                background-color: {bg_color_pressed};
            }}
        """

    @staticmethod
    def tab_button_style(
        fg_color: str,
        fg_color_inactive: str,
        bg_color_base: str,
        bg_color_hover: str,
        bg_color_pressed: str,
        bg_color_inactive: str,
        border_color: str,
        border_color_inactive: str,
        bg_color_disabled: str,
        fg_color_disabled: str,
        border_color_disabled: str
    ):
        return f"""
            QPushButton {{
                background-color: {bg_color_inactive};
                border: 1px solid transparent;
                border-bottom: 1px solid {border_color_inactive};
                font-family: "Montserrat";
                color: {fg_color_inactive};
                letter-spacing: 0.1em;
                padding: 8px 10px;
                border-radius: 0;
                font-size: 14px;
                font-weight: bold;
            }}        
            QPushButton:hover {{
                background-color: {bg_color_hover};
                border: 1px solid {bg_color_hover};
            }}
            QPushButton:focus {{
                background-color: {bg_color_pressed};
                border: 1px solid {bg_color_pressed};
            }}
            QPushButton:pressed {{
                background-color: {bg_color_pressed};
                border: 1px solid {bg_color_pressed};
            }}
            QPushButton:checked {{
                background-color: {bg_color_base}; 
                color: {fg_color};
                border: 1px solid {border_color};
            }}    
            QPushButton:disabled {{
                background-color: {bg_color_disabled};
                border: 2px solid {border_color_disabled};
                color: {fg_color_disabled};
            }}                          
        """
