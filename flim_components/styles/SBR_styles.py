class SBRStyles:

    @staticmethod
    def SBR_label_style(fg_color: str, bg_color: str, font_size: str):
        return f"""
            QLabel {{
                color: {fg_color};
                font-family: "Montserrat";
                font-size: {font_size};
                font-weight: bold;
                background-color: {bg_color}; 
                padding: 2px;
            }}              
        """
