from datetime import datetime

class DateTimeUtils:
    """
    A utility class for working with date and time functions.
    """

    @staticmethod
    def calc_timestamp() -> float:
        """
        Calculate the current timestamp as a float value.

        This method returns the current time as the number of seconds since the epoch (Unix timestamp),
        represented as a floating-point number. It includes fractional seconds.

        Returns
        -------
        float
            The current timestamp as a float value.
        """
        return datetime.now().timestamp()
    
    @staticmethod
    def calc_int_timestamp() -> int:
        """
        Calculate the current timestamp as an integer value.

        This method returns the current time as the number of seconds since the epoch (Unix timestamp),
        represented as an integer. The fractional part of the timestamp is discarded.

        Returns
        -------
        int
            The current timestamp as an integer value.
        """
        return int(datetime.now().timestamp())
