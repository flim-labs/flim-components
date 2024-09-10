from math import floor, log

import numpy as np


class DataConverter:
    """
    A utility class for converting various data types and units,
    particularly for time and numerical conversions. This class provides
    methods to convert between time units, numerical types (between numpy
    and Python), and formats numbers for human-readable output.
    """

    @staticmethod
    def ns_to_mhz(ns_value):
        """
        Converts a time value in nanoseconds (ns) to frequency in megahertz (MHz).

        Parameters:
        - ns_value (float): The value in nanoseconds.

        Returns:
        - float: The equivalent frequency in MHz.
        """
        s_value = ns_value * 1e-9
        hz = 1 / s_value
        mhz = hz / 1e6
        return mhz

    @staticmethod
    def mhz_to_ns(mhz_value):
        """
        Converts a frequency value in megahertz (MHz) to time in nanoseconds (ns).

        Parameters:
        - mhz_value (float): The frequency in MHz.

        Returns:
        - float: The equivalent time in nanoseconds.
        """
        hz = mhz_value * 1e6
        s = 1 / hz
        ns = s * 1e9
        return ns

    @staticmethod
    def humanize_number(number):
        """
        Converts a large number into a human-readable string format
        with units like K (thousands), M (millions), etc.

        Parameters:
        - number (float or int): The number to humanize.

        Returns:
        - str: The number formatted with an appropriate suffix (K, M, G, etc.).
        """
        if number == 0:
            return "0"
        units = ["", "K", "M", "G", "T", "P"]
        k = 1000.0
        magnitude = int(floor(log(number, k)))
        scaled_number = number / k**magnitude
        return f"{int(scaled_number)}.{str(scaled_number).split('.')[1][:2]}{units[magnitude]}"

    @staticmethod
    def convert_ndarray_to_list(data):
        """
        Converts a numpy ndarray to a Python list.

        Parameters:
        - data (np.ndarray): The ndarray to convert.

        Returns:
        - list: The converted list. If the input is not an ndarray, the original data is returned.
        """
        if isinstance(data, np.ndarray):
            return data.tolist()
        return data

    @staticmethod
    def convert_np_num_to_py_num(data):
        """
        Converts numpy numeric types (e.g., np.int64, np.float64) to native Python numeric types.

        Parameters:
        - data (np.int64, np.float64, or other): The numpy numeric value to convert.

        Returns:
        - int or float: The equivalent Python numeric value. If the input is not a numpy type, the original data is returned.
        """
        if isinstance(data, (np.int64, np.float64)):
            return data.item()
        return data

    @staticmethod
    def convert_py_num_to_np_num(output_data):
        """
        Converts Python numeric types (int, float) to numpy numeric types (np.int64, np.float64).

        Parameters:
        - output_data (int or float): The Python numeric value to convert.

        Returns:
        - np.int64 or np.float64: The equivalent numpy numeric value. If the input is not an int or float, the original data is returned.
        """
        if isinstance(output_data, (int, float)):
            return (
                np.float64(output_data)
                if isinstance(output_data, float)
                else np.int64(output_data)
            )
        return output_data

    @staticmethod
    def convert_time(value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert time between different units.

        Parameters
        ----------
        value : float
            The value to be converted.
        from_unit : str
            The current unit of the value. One of: "m", "s", "ms",
            "us", "ns".
        to_unit : str
            The target unit of the value. One of: "m", "s", "ms",
            "us", "ns".

        Returns
        -------
        float
            The converted value in the target unit.
        """

        # Conversion factors to seconds
        to_seconds = {
            "m": 60,  # 1 minute = 60 seconds
            "s": 1,  # 1 second = 1 second
            "ms": 1e-3,  # 1 millisecond = 1/1000 seconds
            "us": 1e-6,  # 1 microsecond = 1/1,000,000 seconds
            "ns": 1e-9,  # 1 nanosecond = 1/1,000,000,000 seconds
        }

        # Conversion factors from seconds
        from_seconds = {
            "m": 1 / 60,  # 1 second = 1/60 minutes
            "s": 1,  # 1 second = 1 second
            "ms": 1e3,  # 1 second = 1000 milliseconds
            "us": 1e6,  # 1 second = 1,000,000 microseconds
            "ns": 1e9,  # 1 second = 1,000,000,000 nanoseconds
        }

        # Check if the units are valid
        if from_unit not in to_seconds or to_unit not in from_seconds:
            raise ValueError(
                f"Unsupported unit conversion from '{from_unit}' to '{to_unit}'"
            )

        # Convert the value to seconds, then to the target unit
        value_in_seconds = value * to_seconds[from_unit]
        converted_value = value_in_seconds * from_seconds[to_unit]

        return converted_value
