class ProgressBarStyles:
    @staticmethod
    def progress_bar_style(color: str):
        return f"""
            QLabel {{
                color: {color};
                font-family: "Montserrat";
                font-size: 18px;
                font-weight: bold;
                
            }} 
            QProgressBar {{
                color: transparent;
                background-color: white;
                padding: 0;
            }}
            QProgressBar::chunk {{
                background: {color};
                color: transparent;
            }}               
        """
