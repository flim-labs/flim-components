class TimeCounterStyles:
    @staticmethod
    def time_counter_style(color: str, font_size: str):
        return f"""
            QLabel {{
                color: {color};
                font-size: {font_size};
            }}
        """   
