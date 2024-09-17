from typing import List
import numpy as np

from flim_components.utils.constants import HETERODYNE_FACTOR, PHASOR_LIFETIMES
from flim_components.utils.data_converter import DataConverter
from flim_components.utils.data_formatter import DataFormatter

class FlimUtils:
    """
    A generic class for Flim utilities and calculations.
    """

    @staticmethod
    def calc_log_mode_values_and_ticks(values: List[int] | List[float] | np.ndarray):
        """
        Calculate logarithmic values and corresponding axis ticks for visualization on a log-scale axis.

        Parameters
        ----------
        values : List[int] | List[float] | np.ndarray
            The input list or array of values to be transformed into logarithmic scale.

        Returns
        -------
        tuple
            A tuple containing:
            - log_values : ndarray
                The logarithmic values of the input data.
            - log_ticks : List[tuple]
                A list of tick labels formatted as powers of ten.
            - exponents_lin_space_int : ndarray
                Linearly spaced integer exponents for the logarithmic scale.
            - max_exponents_int : int
                The maximum exponent found in the input values.
        """
        log_values, exponents_lin_space_int, max_exponents_int = (
            FlimUtils.calc_log_mode_values(values)
        )
        log_ticks = FlimUtils.calc_log_mode_axis_ticks(exponents_lin_space_int)
        return log_values, log_ticks, exponents_lin_space_int, max_exponents_int

    @staticmethod
    def calc_log_mode_values(values: List[int] | List[float] | np.ndarray):
        """
        Calculate the logarithmic values of the input data and generate corresponding exponents.

        Parameters
        ----------
        values : List[int] | List[float] | np.ndarray
            The input values to be transformed into a logarithmic scale.

        Returns
        -------
        tuple
            A tuple containing:
            - log_values : ndarray
                The logarithmic values of the input data.
            - exponents_lin_space_int : ndarray
                Linearly spaced integer exponents for the logarithmic scale.
            - max_exponents_int : int
                The maximum exponent found in the input values.
        """
        values = np.array(values)
        values = np.where(
            values <= 0, 1e-9, values
        )  # Avoid negative or zero values for log calculation
        log_values = np.log10(values)
        log_values = np.where(
            log_values < 0, -0.1, log_values
        )  # Adjust negative logs to a small negative value
        exponents_int = log_values.astype(int)
        exponents_lin_space_int = np.linspace(
            0, max(exponents_int), len(exponents_int)
        ).astype(int)
        return log_values, exponents_lin_space_int, max(exponents_int)

    @staticmethod
    def calc_log_mode_axis_ticks(int_exponents: np.ndarray):
        """
        Generate tick labels for a logarithmic axis using the provided integer exponents.

        Parameters
        ----------
        int_exponents : np.ndarray
            A numpy array of integer exponents to be used for generating the tick labels.

        Returns
        -------
        List[tuple]
            A list of tuples where each tuple contains:
            - The exponent (int)
            - The formatted string representing the exponent as a power of ten (e.g., '10^3').
        """
        ticks = [(i, DataFormatter.format_power_of_ten(i)) for i in int_exponents]
        return ticks

    @staticmethod
    def calc_lin_mode_values_and_ticks(
        values: List[int] | List[float] | np.ndarray, max_ticks=10
    ):
        """
        Calculate linear values and corresponding axis ticks for visualization on a linear scale.

        Parameters
        ----------
        values : List[int] | List[float] | np.ndarray
            The input values to be represented on a linear scale.
        max_ticks : int, optional
            The maximum number of ticks to display on the axis (default is 10).

        Returns
        -------
        tuple
            A tuple containing:
            - values : List[int] | List[float] | np.ndarray
                The original input values.
            - ticks : List[tuple]
                A list of tick values and their string representations.
        """
        max_value = max(values)
        ticks = FlimUtils.calculate_lin_mode_axis_ticks(max_value, max_ticks)
        return values, ticks

    @staticmethod
    def calculate_lin_mode_axis_ticks(max_value, max_ticks):
        """
        Generate axis tick labels for a linear axis based on the maximum value and desired tick count.

        Parameters
        ----------
        max_value : int | float
            The maximum value of the input data, used to define the scale of the axis.
        max_ticks : int
            The maximum number of tick marks to generate on the axis.

        Returns
        -------
        List[tuple]
            A list of tuples where each tuple contains:
            - The tick value (float)
            - The formatted tick label as a string.
        """
        if max_value <= 0:
            return [0]
        step = 10 ** (np.floor(np.log10(max_value)) - 1)
        ticks = np.arange(0, max_value + step, step)
        while len(ticks) > max_ticks:
            step *= 2
            ticks = np.arange(0, max_value + step, step)
        ticks = [(value, str(int(value))) for value in ticks]
        return ticks

    @staticmethod
    def calculate_phasor_tau(
        g: float, s: float, freq_mhz: float, harmonic: int
    ) -> tuple[float | None, float | None]:
        """
        Calculates the phasor lifetime components (tau_phi and tau_m) based on input parameters
        such as fluorescence intensity parameters (g, s), frequency in MHz, and harmonic.

        Parameters:
        ----------
        g : float
            The 'g' component of the phasor plot.
        s : float
            The 's' component  of the phasor plot.
        freq_mhz : float
            The modulation frequency in megahertz (MHz). If freq_mhz is 0, the function returns None.
        harmonic : int
            The harmonic number, used for frequency scaling.

        Returns:
        -------
        tau_phi : float or None
            The calculated phase lifetime (tau_phi) in picoseconds, or None if freq_mhz is 0.
        tau_m : float or None
            The calculated modulation lifetime (tau_m) in picoseconds, or None if the tau_m component is negative.
        """
        if freq_mhz == 0.0:
            return None, None
        tau_phi = (1 / (2 * np.pi * freq_mhz * harmonic)) * (s / g) * 1e3
        tau_m_component = (1 / (s**2 + g**2)) - 1
        if tau_m_component < 0:
            tau_m = None
        else:
            tau_m = (
                (1 / (2 * np.pi * freq_mhz * harmonic)) * np.sqrt(tau_m_component) * 1e3
            )
        return tau_phi, tau_m

    @staticmethod
    def calculate_phasor_points(
        harmonic: int,
        laser_period_ns: float,
        frequency_mhz: float,
        tau_m: np.ndarray = PHASOR_LIFETIMES,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Calculate phasor points (g, s) based on the given lifetimes (tau_m), harmonic, laser period, and frequency.

        Parameters:
        ----------
        tau_m : np.ndarray
            Array of lifetime values. (default is [ 0.1e-9, 0.5e-9, 1e-9, 2e-9, 3e-9, 4e-9, 5e-9, 6e-9, 7e-9, 8e-9, 9e-9, 10e-9])
        harmonic : int
            Harmonic number used in the calculation.
        laser_period_ns : float
            The period of the laser in nanoseconds.
        frequency_mhz : float
            The frequency in MHz, which might affect the range of tau values.

        Returns:
        -------
        tuple[np.ndarray, np.ndarray, np.ndarray]
            - g: The G values (real part of the phasor).
            - s: The S values (imaginary part of the phasor).
            - tau_m: The (possibly extended) lifetime values used in the calculation.
        """
        if frequency_mhz in [10, 20]:
            additional_tau = np.arange(10e-9, 26e-9, 5e-9)
            tau_m = np.concatenate((tau_m, additional_tau))
        fex = (1 / laser_period_ns) * 10e8
        k = 1 / (2 * np.pi * harmonic * fex)
        phi = np.arctan(tau_m / k)
        factor = (tau_m / k) ** 2
        m = np.sqrt(1 / (1 + factor))
        g = m * np.cos(phi)
        s = m * np.sin(phi)
        return g, s, tau_m

    @staticmethod
    def calculate_phasor_points_mean(
        points: list[tuple[float, float]]
    ) -> tuple[float | None, float | None]:
        """
        Calculates the mean phasor coordinates (g, s) from a list of phasor points.

        Parameters:
        ----------
        points : list[tuple[float, float]]
            A list of tuples where each tuple contains two float values representing
            the g and s  coordinates of a phasor point.

        Returns:
        -------
        tuple[float | None, float | None]
            A tuple containing:
            - mean_g : float or None
            The mean of the g values. Returns None if input is empty or contains only NaN values.
            - mean_s : float or None
            The mean of the s values. Returns None if input is empty or contains only NaN values.
        """
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        g_values = np.array(x)
        s_values = np.array(y)
        if (
            g_values.size == 0
            or s_values.size == 0
            or np.all(np.isnan(g_values))
            or np.all(np.isnan(s_values))
        ):
            return None, None
        mean_g = np.nanmean(g_values)
        mean_s = np.nanmean(s_values)
        return mean_g, mean_s

    @staticmethod
    def calculate_quantization(
        x: list[float], y: list[float], bins: int = 64
    ) -> tuple[np.ndarray, float, float, bool]:
        """
        Calculates points 2D histogram (quantization).

        Parameters:
        ----------
        x : list[float]
            List of x coordinates (g values) of the phasor points.
        y : list[float]
            List of y coordinates (s values) of the phasor points.
        bins : int, optional
            Number of bins for the histogram, default is 64.

        Returns:
        -------
        h : np.ndarray
            The normalized 2D histogram array.
        h_min : float
            The minimum non-zero value in the histogram.
        h_max : float
            The maximum value in the histogram.
        all_zeros : bool
            A flag indicating whether the histogram contains only zeros.
        """
        if not x or not y:
            return None, None, None, True  # No data to quantize
        # Create 2D histogram
        h, xedges, yedges = np.histogram2d(
            x, y, bins=bins * 4, range=[[-2, 2], [-2, 2]]
        )
        # Check for non-zero values
        non_zero_h = h[h > 0]
        all_zeros = len(non_zero_h) == 0
        if all_zeros:
            return h, None, None, all_zeros
        # Find the minimum and maximum values in the non-zero elements
        h_min = np.min(non_zero_h)
        h_max = np.max(h)
        # Normalize the histogram
        h = h / h_max
        h[h == 0] = np.nan
        return h, h_min, h_max, all_zeros

    @staticmethod
    def create_hot_colormap() -> tuple[np.ndarray, np.ndarray]:
        """
        Creates a 'hot' colormap by defining positions and corresponding RGBA colors that transition from black
        to red, to yellow, and finally to white. This data can be used to generate a colormap for visualizing
        intensity levels in heatmaps or other visual data.

        The color map is constructed by specifying four color stops at different positions:
        - Black (0, 0, 0) at position 0.0.
        - Red (255, 0, 0) at position 0.33.
        - Yellow (255, 255, 0) at position 0.67.
        - White (255, 255, 255) at position 1.0.

        Returns:
        -------
        tuple[np.ndarray, np.ndarray]
            A tuple containing:
            - pos : np.ndarray
            An array of float values representing the positions of the color stops in the range [0.0, 1.0].
            - color : np.ndarray
            An array of RGBA values corresponding to each position, where each color is a 4-element array of integers.
        """
        # Define positions for color stops
        pos = np.array([0.0, 0.33, 0.67, 1.0])
        # Define RGBA colors corresponding to the positions
        color = np.array(
            [
                [0, 0, 0, 255],  # Black
                [255, 0, 0, 255],  # Red
                [255, 255, 0, 255],  # Yellow
                [255, 255, 255, 255],  # White
            ],
            dtype=np.ubyte,
        )
        return pos, color

    @staticmethod
    def create_cool_colormap(
        start: float = 0.0, end: float = 1.0
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Creates a 'cool' colormap by defining positions and corresponding RGBA colors that transition
        from cyan to magenta. This data can be used to generate a colormap for visualizing various data
        with a cool color scheme.

        The color map is constructed by specifying two color stops at given positions:
        - Cyan (0, 255, 255) at the 'start' position.
        - Magenta (255, 0, 255) at the 'end' position.

        Parameters:
        ----------
        start : float, optional
            The starting position for the cyan color, default is 0.0.
        end : float, optional
            The ending position for the magenta color, default is 1.0.

        Returns:
        -------
        tuple[np.ndarray, np.ndarray]
            A tuple containing:
            - pos : np.ndarray
            An array of two float values representing the start and end positions of the color stops.
            - color : np.ndarray
            An array of RGBA values corresponding to the start and end positions, where each color is
            a 4-element array of integers.
        """
        # Define positions for color stops (cyan at 'start', magenta at 'end')
        pos = np.array([start, end])
        # Define RGBA colors for cyan and magenta
        color = np.array(
            [
                [0, 255, 255, 255],  # Cyan
                [255, 0, 255, 255],  # Magenta
            ],
            dtype=np.float32,
        )
        return pos, color
    
    
    @staticmethod
    def bin_to_time_ns(bin: int, frequency_mhz: float) -> float:
        """
        Convert a time bin to nanoseconds based on the laser frequency.

        This function calculates the time in nanoseconds corresponding to a specific bin value 
        in a FLIM measurement, using the modulation 
        frequency of the laser.

        Parameters
        ----------
        bin : int
            The time bin to be converted into nanoseconds.
        frequency_mhz : float
            The modulation frequency of the laser in megahertz (MHz).

        Returns
        -------
        float
            The time in nanoseconds corresponding to the given bin, adjusted by the heterodyne factor.
        """
        laser_period_ns = 0.0 if frequency_mhz == 0.0 else DataConverter.mhz_to_ns(frequency_mhz)
        return ((bin * laser_period_ns) / 256) * HETERODYNE_FACTOR
    

    @staticmethod
    def time_ns_to_bin(micro_time_ns: float, frequency_mhz: float) -> int:
        """
        Convert time in nanoseconds to a corresponding bin value based on the laser frequency.

        This function converts a time in nanoseconds back to the corresponding bin value for 
        FLIM measurements, using the modulation frequency of the laser.

        Parameters
        ----------
        micro_time_ns : float
            The time in nanoseconds to be converted into a bin value.
        frequency_mhz : float
            The modulation frequency of the laser in megahertz (MHz).

        Returns
        -------
        int
            The corresponding bin value for the given time in nanoseconds, adjusted by the heterodyne factor.
        """
        laser_period_ns = 0.0 if frequency_mhz == 0.0 else DataConverter.mhz_to_ns(frequency_mhz)
        if laser_period_ns == 0.0:
            return 0  
        return (micro_time_ns * 256) / (HETERODYNE_FACTOR * laser_period_ns)
    
    
    @staticmethod
    def calculate_SBR(y: np.ndarray) -> float:
        """
        Calculate the Signal-to-Background Ratio (SBR) of a given array.

        The SBR is computed as the ratio of the mean (signal) to the standard deviation (noise) 
        of the input data, expressed in decibels (dB).

        Parameters
        ----------
        y : np.ndarray
            The input array of numerical values representing the signal.

        Returns
        -------
        float
            The Signal-to-Background Ratio (SBR) in decibels (dB).
        """
        signal = np.mean(y)
        noise = np.std(y)
        return 10 * np.log10(signal / noise)
    
    
