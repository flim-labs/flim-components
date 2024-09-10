import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from typing import Any, Dict, Literal, Optional, Tuple

from models.models import (
    PlotAxisParams,
    PlotDimensionsParams,
    PlotGridParams,
    PlotScatterStyleParams,
    PlotTextItemParams,
)
from utils.flim_utils import FlimUtils


class FlimPlot(pg.PlotWidget):
    """
    A class which extends pyqtgraph PlotWidget functionalities.

    Parameters
    ----------
    parent : Optional[QWidget]
        The parent widget for the plot (default is None).
    title : str, optional
        The title of the plot (default is an empty string).
    x_axis : PlotAxisParams, optional
        Configuration parameters for the X-axis, including label, axis color, label color, and units.
    y_axis : PlotAxisParams, optional
        Configuration parameters for the Y-axis, including label, axis color, label color, and units.
    background : str, optional
        Background color of the plot (default is 'default').
    grid : PlotGridParams, optional
        Parameters for the grid, including visibility for X and Y axes and alpha transparency.
    dimensions : PlotDimensionsParams, optional
        Parameters defining the plot's size and constraints (default is None).
    visible : bool, optional
        Whether the plot widget should be visible upon initialization (default is True).

    Signals
    -------
    roi_changed : pyqtSignal()
        Emitted when the plot selected ROI changes
    """

    roi_changed = pyqtSignal()

    def __init__(
        self,
        title: str = "",
        x_axis: PlotAxisParams = {
            "label": "X Axis",
            "axis_color": "white",
            "label_color": "white",
            "units": "",
        },
        y_axis: PlotAxisParams = {
            "label": "Y Axis",
            "axis_color": "white",
            "label_color": "white",
            "units": "",
        },
        background: str = "default",
        grid: PlotGridParams = {"show_x": False, "show_y": False, "alpha": 0.3},
        dimensions: PlotDimensionsParams | None = None,
        visible: bool = True,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        # Initialize data attributes
        self.plot_data: Dict[str, pg.PlotDataItem] = {}
        self.plot_items: Dict[str, pg.GraphicsItem] = {}
        self.cached_x_data: Dict[str, np.ndarray] = (
            {}
        )  # Backup for original X data sets
        self.cached_y_data: Dict[str, np.ndarray] = (
            {}
        )  # Backup for original Y data sets
        self.x_region_data: Dict[str, np.ndarray] = {}
        self.y_region_data: Dict[str, np.ndarray] = {}

        # Configure plot
        self.set_plot_background(background)
        if dimensions:
            self.set_plot_dimensions(dimensions)
        self.set_plot_title(title)
        self.set_axis_config(x_axis, y_axis)
        self.show_grid(grid)
        self.set_visible(visible)

        # Placeholder for ROI (Plot Region)
        self.region = None
        self.region_bounds: Tuple[int | float, int | float] | None = None

    def set_plot_title(self, title: str) -> None:
        """
        Set the title of the plot.
        Parameters
        ----------
        title : str
            The title for the plot

        """
        self.setTitle(title)

    def set_plot_background(self, background: str) -> None:
        """
        Set the background color of the plot.
        Parameters
        ----------
        background : str
            The background color for the plot

        """
        self.setBackground(background)

    def init_plot(
        self,
        x: np.ndarray,
        y: np.ndarray,
        data_set_key: str,
        pen: Optional[pg.mkPen],
        log_mode: bool,
        legend_name: str | None = None,
        legend_offset: Tuple[int, int] | None = None,
        plot_grid_config: PlotGridParams = {
            "show_x": False,
            "show_y": False,
            "alpha": 0.3,
        },
        axis_lin_log: Literal["x", "y"] = "y",
        format_ticks: bool = False,
        max_ticks: int = 10,
        axis_shift: Literal["x", "y"] = "y",
        axis_auto_range: Literal["x", "y"] = "y",
        shift: int = 0,
        auto_range: bool = True,
        min_val_range: float | None = None,
        max_val_range: float | None = None,
        padding: float = 0,
        auto_si_prefix_x: bool = False,
        auto_si_prefix_y: bool = False,
    ) -> None:
        """
        Initialize and configure the plot with the provided data.

        Parameters
        ----------
        x : np.ndarray
            The X-axis data points.
        y : np.ndarray
            The Y-axis data points.
        data_set_key : str
            A data-set key to identify the set of data
        pen : Optional[pg.mkPen]
            Pen to draw the plot (default is a red line if None).
        log_mode : bool
            Whether to use logarithmic scale for the plot (default is False).
        legend_name : str | None
            The data label inside del legend if set (default is None).
        legend_offset : Tuple[int, int] | None
            The legend offset if set (default is None).
        plot_grid_config : PlotGridParams
            Configuration for the grid visibility and alpha value.
        axis_lin_log : Literal["x", "y"], optional
            The axis to apply logarithmic or linear scaling (default is "y").
        format_ticks : bool, optional
            Wether to format the axis ticks depending on logarithmic/linear scaling (default is False).
        max_ticks : int, optional
            The number of axis ticks to visualize. This is only used in lin mode (default is 10).
        axis_shift : Literal["x", "y"], optional
            The axis to apply data shifting (default is "y").
        axis_auto_range : Literal["x", "y"], optional
            The axis to apply automatic range scaling (default is "y").
        shift : int, optional
            Value by which to shift the axis data (default is 0).
        auto_range : bool, optional
            If True, automatically adjust the plot range based on data (default is True).
        min_val_range : float | None, optional
            Minimum value for auto-range (default is None).
        max_val_range : float | None, optional
            Maximum value for auto-range (default is None).
        padding : float, optional
            Padding for the auto-range (default is 0).
        auto_si_prefix_x : bool, optional
            If True, enables the SI prefixes on the x-axis (bottom axis). Default is False.
        auto_si_prefix_y : bool, optional
            If True, enables the SI prefixes on the y-axis (left axis). Default is False.
        """
        # add legend
        if legend_name is not None:
            self.add_legend(offset=legend_offset)

        # Log data
        if log_mode:
            x_data, y_data, ticks = self.set_log_mode(axis_lin_log, data_set_key, x, y)
        # Lin data
        else:
            x_data, y_data, ticks = self.set_lin_mode(
                axis_lin_log, data_set_key, x, y, max_ticks
            )
        # Axis shift
        x_data, y_data = self.set_values_shift(
            axis_shift, data_set_key, x_data, y_data, shift
        )

        # Set ticks
        if format_ticks:
            if axis_lin_log == "y":
                self.getAxis("left").setTicks([ticks])
            else:
                self.getAxis("bottom").setTicks([ticks])

        # Init data
        self.plot_data[data_set_key] = self.plot(
            x_data,
            y_data,
            pen=pen if pen is not None else pg.mkPen(color="#f72828", width=2),
            name=legend_name,
        )
        # plot auto range
        if auto_range:
            self._auto_range(axis_auto_range, min_val_range, max_val_range, padding)
        # show grid
        self.show_grid(plot_grid_config)
        # auto SI prefix
        self.enable_auto_si_prefix(auto_si_prefix_x, auto_si_prefix_y)
        # Store data
        self.cached_x_data[data_set_key] = x_data
        self.cached_y_data[data_set_key] = y_data

    def update_plot(
        self,
        x: np.ndarray,
        y: np.ndarray,
        data_set_key: str,
        log_mode: bool,
        plot_grid_config: PlotGridParams = {
            "show_x": False,
            "show_y": False,
            "alpha": 0.3,
        },
        axis_lin_log: Literal["x", "y"] = "y",
        format_ticks: bool = False,
        max_ticks: int = 10,
        axis_shift: Literal["x", "y"] = "y",
        axis_auto_range: Literal["x", "y"] = "y",
        shift: int = 0,
        auto_range: bool = True,
        min_val_range: float | None = None,
        max_val_range: float | None = None,
        padding: float = 0,
        clear_prev_data: bool = False,
    ) -> None:
        """
        Update the plot with new data, store the original data for backup before processing and optionally clear previous data.

        Parameters
        ----------
        x : np.ndarray
            The new X-axis data points.
        y : np.ndarray
            The new Y-axis data points.
        data_set_key : str
            A data-set key to identify the set of data
        log_mode : bool
            Whether to use logarithmic scaling for the plot.
        plot_grid_config : PlotGridParams
            Grid configuration parameters.
        axis_lin_log : Literal["x", "y"], optional
            The axis to apply logarithmic or linear scaling (default is "y").
        format_ticks : bool, optional
            Wether to format the axis ticks depending on logarithmic/linear scaling (default is False).
        max_ticks : int, optional
            The number of axis ticks to visualize. This is only used in lin mode (default is 10).
        axis_shift : Literal["x", "y"], optional
            The axis to apply data shifting (default is "y").
        axis_auto_range : Literal["x", "y"], optional
            The axis for automatic range scaling (default is "y").
        shift : int, optional
            Value by which to shift the axis data (default is 0).
        auto_range : bool, optional
            Whether to adjust the plot range automatically (default is True).
        min_val_range : float | None, optional
            Minimum value for auto-ranging (default is None).
        max_val_range : float | None, optional
            Maximum value for auto-ranging (default is None).
        padding : float, optional
            Padding for auto-ranging (default is 0).
        clear_prev_data : bool, optional
            If True, clear previous data before updating the plot (default is False).
        """

        if (
            (data_set_key not in self.cached_x_data)
            or (data_set_key not in self.cached_y_data)
            or (data_set_key not in self.plot_data)
        ):
            raise ValueError(
                "You must provide a valid data-set key to be able to update the correct data-set"
            )

        if clear_prev_data:
            self.clear_plot()  # Clear the plot before adding new data (if not in realtime mode)

        # Store a backup of the original data
        self.cached_x_data[data_set_key] = (
            np.array(x) if clear_prev_data else np.append(self.cached_x_data, x)
        )  # Store a copy of the X data
        self.cached_y_data[data_set_key] = (
            np.array(y) if clear_prev_data else np.append(self.cached_y_data, y)
        )  # Store a copy of the Y data
        # Log data
        if log_mode:
            x_data, y_data, ticks = self.set_log_mode(axis_lin_log, data_set_key, x, y)
        # Lin data
        else:
            x_data, y_data, ticks = self.set_lin_mode(
                axis_lin_log, data_set_key, x, y, max_ticks
            )
        # Axis shift
        x_data, y_data = self.set_values_shift(
            axis_shift, data_set_key, x_data, y_data, shift
        )
        # Update plot
        self.plot_data[data_set_key].setData(x_data, y_data)
        # Set ticks
        if format_ticks:
            if axis_lin_log == "y":
                self.getAxis("left").setTicks([ticks])
            else:
                self.getAxis("bottom").setTicks([ticks])
        # plot auto range
        if auto_range:
            self._auto_range(axis_auto_range, min_val_range, max_val_range, padding)
        # show plot grid
        self.show_grid(plot_grid_config)

    def set_plot_dimensions(self, dimensions: PlotDimensionsParams) -> None:
        """
        Set the dimensions of the plot widget.

        Parameters
        ----------
        dimensions : PlotDimensionsParams
            A dictionary containing width, height, minimum width, minimum height,
            maximum width, and maximum height for the plot widget.
        """
        if dimensions["width"] is not None:
            self.setWidth(dimensions["width"])
        if dimensions["height"] is not None:
            self.setHeight(dimensions["height"])
        if dimensions["min_width"] is not None:
            self.setMinimumWidth(dimensions["min_width"])
        if dimensions["min_height"] is not None:
            self.setMinimumHeight(dimensions["min_height"])
        if dimensions["max_width"] is not None:
            self.setMaximumWidth(dimensions["max_width"])
        if dimensions["max_height"] is not None:
            self.setMaximumHeight(dimensions["max_height"])

    def set_axis_config(self, x_axis: PlotAxisParams, y_axis: PlotAxisParams) -> None:
        """
        Configure the X and Y axes of the plot.

        Parameters
        ----------
        x_axis : PlotAxisParams
            Configuration parameters for the X-axis.
        y_axis : PlotAxisParams
            Configuration parameters for the Y-axis.
        """
        self.setLabel("left", y_axis["label"], color=y_axis["label_color"])
        self.setLabel("bottom", x_axis["label"], color=x_axis["label_color"])
        self.getAxis("left").setPen(y_axis["axis_color"])
        self.getAxis("bottom").setPen(x_axis["axis_color"])

    def enable_auto_si_prefix(self, x: bool = False, y: bool = False) -> None:
        """
        Enables or disables the automatic use of SI (International System of Units) prefixes
        on the x and y axes of the plot.

        Parameters:
        ----------
        x : bool, optional
            If True, enables the SI prefixes on the x-axis (bottom axis). Default is False.
        y : bool, optional
            If True, enables the SI prefixes on the y-axis (left axis). Default is False.

        Returns:
        -------
        None
        """
        self.plotItem.getAxis("left").enableAutoSIPrefix(y)
        self.plotItem.getAxis("bottom").enableAutoSIPrefix(x)

    def show_grid(self, params: PlotGridParams | None) -> None:
        """
        Show or hide the grid on the plot.

        Parameters
        ----------
        params : PlotGridParams | None
            A dictionary containing visibility for X and Y axes and alpha transparency for the grid.
        """
        if params is not None:
            self.showGrid(x=params["show_x"], y=params["show_y"], alpha=params["alpha"])

    def clear_plot(self) -> None:
        """
        Clear the plot, removing all data and any active ROI.

        This method resets all stored data and removes any existing plot regions.
        """
        self.clear()
        if self.region is not None:
            self.removeItem(self.region)
            self.region = None
        for item in self.plot_items:
            if item is not None:
                self.removeItem(item)
        # Clear the stored data
        self.cached_x_data.clear()
        self.cached_y_data.clear()
        self.region_bounds = None
        self.x_region_data.clear()
        self.y_region_data.clear()
        self.plot_items.clear()

    def get_plot_instance(self) -> pg.PlotWidget:
        """
        Get the PyQtGraph plot widget instance.

        Returns
        -------
        pg.PlotWidget
            The instance of the plot widget.
        """
        return self

    def get_plot_data(self, data_set_key: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Retrieve the current data from the plot widget.

        Parameters
        ----------
        data_set_key : str
            The data-set key to identify the set of data

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            The X and Y data arrays from the plot widget.
        """
        if data_set_key not in self.plot_data:
            raise ValueError(
                "You must provide a valid data-set key to be able to retrieve the correct data-set"
            )

        x, y = self.plot_data[data_set_key].getData()
        return x, y

    def get_cached_plot_data(self, data_set_key: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Retrieve the current cached data from the plot widget.

        Parameters
        ----------
        data_set_key : str
            The data-set key to identify the set of data

        Returns
        -------
        Tuple[np.ndarray, np.ndarray]
            The X and Y cached data arrays from the plot widget.
        """
        if (data_set_key not in self.cached_x_data) or (
            data_set_key not in self.cached_y_data
        ):
            raise ValueError(
                "You must provide a valid data-set key to be able to retrieve the correct cached data-set"
            )

        x = self.cached_x_data[data_set_key]
        y = self.cached_y_data[data_set_key]
        return x, y

    def clear_data(self, data_set_key: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Clear a specific dataset from the plot widget. It also delete relative data from memory.

        Parameters
        ----------
        data_set_key : str
            The data-set key to identify the set of data to remove
        """
        if data_set_key not in self.plot_data:
            raise ValueError(
                "You must provide a valid data-set key to be able to remove the correct data-set"
            )
        self.removeItem(self.plot_data[data_set_key])
        del self.plot_data[data_set_key]
        if data_set_key in self.cached_x_data:
            del self.cached_x_data[data_set_key]
        if data_set_key in self.cached_y_data:
            del self.cached_y_data[data_set_key]
        if data_set_key in self.x_region_data:
            del self.x_region_data[data_set_key]
        if data_set_key in self.y_region_data:
            del self.y_region_data[data_set_key]

    def remove_item(self, data_set_key: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Remove a specific item from the plot widget. It also delete relative data from memory

        Parameters
        ----------
        data_set_key : str
            The data-set key to identify the item to remove
        """
        if data_set_key not in self.plot_items:
            raise ValueError(
                "You must provide a valid data-set key to be able to remove the correct item"
            )
        self.removeItem(self.plot_items[data_set_key])
        del self.plot_items[data_set_key]
        if data_set_key in self.cached_x_data:
            del self.cached_x_data[data_set_key]
        if data_set_key in self.cached_y_data:
            del self.cached_y_data
        if data_set_key in self.x_region_data:
            del self.x_region_data[data_set_key]
        if data_set_key in self.y_region_data:
            del self.y_region_data[data_set_key]

    def set_range(
        self,
        x_range: Optional[Tuple[float | int, float | int, int]] = None,
        y_range: Optional[Tuple[float | int, float | int, int]] = None,
    ) -> None:
        """
        Set the visible range of the plot.

        Parameters
        ----------
        x_range : Optional[Tuple[float | int, float | int, int]]
            The range for the X-axis, including minimum value, maximum value, and padding.
        y_range : Optional[Tuple[float | int, float | int, int]]
            The range for the Y-axis, including minimum value, maximum value, and padding.
        """
        if x_range:
            self.setXRange(x_range[0], x_range[1], padding=x_range[2])
        if y_range:
            self.setYRange(y_range[0], y_range[1], padding=y_range[2])

    def _auto_range(
        self,
        axis: Literal["x", "y"],
        min_val: float | None,
        max_val: float | None,
        padding: float,
    ) -> None:
        """
        Automatically adjust the range of the specified axis.

        Parameters
        ----------
        axis : str
            The axis to adjust, either 'x' or 'y'.
        min_val : float | None
            The minimum value for the axis. If None, use the current minimum.
        max_val : float | None
            The maximum value for the axis. If None, use the current maximum.
        padding : float
            The amount of padding to apply to the range.
        """
        self.plotItem.autoRange()
        view_range = self.viewRange()
        current_min, current_max = view_range[0] if axis == "x" else view_range[1]
        new_min = min_val if min_val is not None else current_min
        new_max = max_val if max_val is not None else current_max
        if axis == "x":
            self.setXRange(new_min, new_max, padding=padding)
        elif axis == "y":
            self.setYRange(new_min, new_max, padding=padding)

    def auto_range_x(
        self, x_min: float | None = None, x_max: float | None = None, padding: float = 0
    ) -> None:
        """
        Automatically adjust the range for the X-axis.

        Parameters
        ----------
        x_min : float | None
            The minimum value for the X-axis. If None, use the current value.
        x_max : float | None
            The maximum value for the X-axis. If None, use the current value.
        padding : float
            The amount of padding to apply to the range.
        """
        self._auto_range("x", x_min, x_max, padding)

    def auto_range_y(
        self, y_min: float | None = None, y_max: float | None = None, padding: float = 0
    ) -> None:
        """
        Automatically adjust the range for the Y-axis.

        Parameters
        ----------
        y_min : float | None
            The minimum value for the Y-axis. If None, use the current value.
        y_max : float | None
            The maximum value for the Y-axis. If None, use the current value.
        padding : float
            The amount of padding to apply to the range.
        """
        self._auto_range("y", y_min, y_max, padding)

    def set_log_mode(
        self,
        axis: Literal["x", "y"],
        data_set_key: str,
        x_data: np.ndarray | None = None,
        y_data: np.ndarray | None = None,
    ) -> Tuple[np.ndarray, np.ndarray, list[tuple[Any, str]]]:
        """
        Sets the logarithmic scale for the selected axis ("x" or "y"). If no data is provided,
        cached data is used. Recalculates the values and ticks for the selected axis in log mode.

        Parameters:
        - axis: Literal["x", "y"]
            Specifies which axis ("x" or "y") to convert to logarithmic scale.
        - data_set_key : str
            A data-set key to identify the set of data
        - x_data: np.ndarray | None, optional
            Data for the x-axis (optional, uses cached data if not provided).
        - y_data:  np.ndarray | None, optional
            Data for the y-axis (optional, uses cached data if not provided).

        Returns:
        - Tuple[np.ndarray, np.ndarray, list[tuple[Any, str]]]:
        A tuple containing the updated x_data or y_data (depending on the axis), and the list of
        logarithmic ticks formatted as tuples (value, label).
        """
        if (x_data is None and data_set_key not in self.cached_x_data) or (
            y_data is None and data_set_key not in self.cached_y_data
        ):
            raise ValueError(
                "You must provide x_data/y_data or a valid data-set key to be able to use cached data"
            )
        x_data = x_data if x_data is not None else self.cached_x_data[data_set_key]
        y_data = y_data if y_data is not None else self.cached_y_data[data_set_key]
        if axis == "y":
            y_data, log_ticks, _, __ = FlimUtils.calc_log_mode_values_and_ticks(y_data)
        else:
            x_data, log_ticks, _, __ = FlimUtils.calc_log_mode_values_and_ticks(x_data)
        return x_data, y_data, log_ticks

    def set_lin_mode(
        self,
        axis: Literal["x", "y"],
        data_set_key: str,
        x_data: np.ndarray | None = None,
        y_data: np.ndarray | None = None,
        max_ticks: int = 10,
    ) -> Tuple[np.ndarray, np.ndarray, list[int] | list[tuple[Any, str]]]:
        """
        Sets the linear scale for the selected axis ("x" or "y"). If no data is provided,
        cached data is used. Recalculates the values and ticks for the selected axis in linear mode.

        Parameters:
        - axis: Literal["x", "y"]
            Specifies which axis ("x" or "y") to convert to linear scale.
        - data_set_key : str
            A data-set key to identify the set of data
        - x_data: np.ndarray | None, optional
            Data for the x-axis (optional, uses cached data if not provided).
        - y_data: np.ndarray | None, optional
            Data for the y-axis (optional, uses cached data if not provided).
        - max_ticks: int, optional
            Specifies the max number of axis ticks to visualize

        Returns:
        - Tuple[np.ndarray, np.ndarray, list[int] | list[tuple[Any, str]]]:
        A tuple containing the updated x_data or y_data (depending on the axis), and the list of
        linear ticks, which could either be a list of integers or formatted tuples (value, label).
        """
        if (x_data is None and data_set_key not in self.cached_x_data) or (
            y_data is None and data_set_key not in self.cached_y_data
        ):
            raise ValueError(
                "You must provide x_data/y_data or a valid data-set key to be able to use cached data"
            )
        x_data = x_data if x_data is not None else self.cached_x_data[data_set_key]
        y_data = y_data if y_data is not None else self.cached_y_data[data_set_key]
        if axis == "y":
            y_data, log_ticks = FlimUtils.calc_lin_mode_values_and_ticks(
                y_data, max_ticks
            )
        else:
            x_data, log_ticks = FlimUtils.calc_lin_mode_values_and_ticks(
                x_data, max_ticks
            )
        return x_data, y_data, log_ticks

    def set_values_shift(
        self,
        axis: Literal["x", "y"],
        data_set_key: str,
        x_data: np.ndarray | None = None,
        y_data: np.ndarray | None = None,
        shift: int = 0,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Applies a shift to the values on the selected axis ("x" or "y"). If no data is provided,
        cached data is used. The function shifts the values of the specified axis by the given amount.

        Parameters:
        - axis: Literal["x", "y"]
            Specifies which axis ("x" or "y") to shift.
        - data_set_key : str
            A data-set key to identify the set of data
        - x_data: np.ndarray | None, optional
            Data for the x-axis (optional, uses cached data if not provided).
        - y_data: np.ndarray | None, optional
            Data for the y-axis (optional, uses cached data if not provided).
        - shift: int, optional
            Number of positions to shift the data. (default is 0)

        Returns:
        - Tuple[np.ndarray, np.ndarray]:
        A tuple containing the updated x_data and y_data after applying the shift.
        """
        if (x_data is None and data_set_key not in self.cached_x_data) or (
            y_data is None and data_set_key not in self.cached_y_data
        ):
            raise ValueError(
                "You must provide x_data/y_data or a valid data-set key to be able to use cached data"
            )
        x_data = x_data if x_data is not None else self.cached_x_data[data_set_key]
        y_data = y_data if y_data is not None else self.cached_y_data[data_set_key]
        if axis == "y":
            y_data = np.roll(y_data, shift)
            pass
        else:
            x_data = np.roll(x_data, shift)
        return x_data, y_data

    def add_legend(self, offset: Tuple[int, int] | None = None) -> None:
        """
        Add a legend to the plot.

        Parameters
        ----------
        offset : Tuple[int, int] | None, optional
            The offset for the legend position (default is None). If None, the legend is added with default position.
        """
        if offset is None:
            legend = self.addLegend()
            legend.setParent(self)
        else:
            legend = self.addLegend(offset=offset)
            legend.setParent(self)

    def add_scatter_point(
        self,
        x: np.ndarray,
        y: np.ndarray,
        scatter_key: str,
        text_item_key: str | None = None,
        text_item: PlotTextItemParams | None = None,
        style: PlotScatterStyleParams = {
            "size": 20,
            "pen": None,
            "brush": "red",
            "symbol": "o",
        },
        points_z_index: int | None = None,
        text_z_index: int | None = None,
        points_ignore_bounds: bool = False,
        text_ignore_bounds: bool = False,
    ) -> None:
        """
        Add scatter points to the plot.

        Parameters
        ----------
        x : np.ndarray
            The X-axis coordinates of the scatter points.
        y : np.ndarray
            The Y-axis coordinates of the scatter points.
        scatter_key : str
            A key to identify the scatter plot
        text_item_key: str | None, optional
            A key to identify the text item (required only if you want to add a TextItem)
        text_item : PlotTextItemParams | None, optional
            Parameters for the text items to be displayed at the scatter points (default is None).
        style : PlotScatterStyleParams, optional
            Style parameters for the scatter points, including size, pen, brush, and symbol (default is a red circle with size 20).
        points_z_index : int | None, optional
            The Z-index for the scatter points, which determines their drawing order (default is None).
        text_z_index : int | None, optional
            The Z-index for the text items, which determines their drawing order (default is None).
        points_ignore_bounds : bool, optional
            Whether to ignore plot bounds for scatter points (default is False).
        text_ignore_bounds : bool, optional
            Whether to ignore plot bounds for text items (default is False).
        """
        if text_item is not None and text_item_key is None:
            raise ValueError(
                "You must provide the parameter text_item_key to identify the TextItem"
            )
        scatter = pg.ScatterPlotItem(
            x, y, size=style["size"], brush=style["brush"], pen=style["pen"]
        )
        if points_z_index is not None:
            scatter.setZValue(points_z_index)
        self.addItem(scatter, ignoreBounds=points_ignore_bounds)

        if text_item is not None:
            self.add_text_item(
                params=text_item,
                z_index=text_z_index,
                ignore_bounds=text_ignore_bounds,
                key=text_item_key,
            )
            self.plot_items[text_item_key] = text_item
        self.cached_x_data[scatter_key] = x
        self.cached_y_data[scatter_key] = y
        self.plot_items[scatter_key] = scatter

    def add_line(
        self,
        key:str,
        x: float | int | None,
        y: float | int | None,
        color: str = "w",
        pen_style: Qt.PenStyle = Qt.PenStyle.DashLine,
    ) -> None:
        """
        Adds a horizontal or vertical line to the plot.

        Parameters
        ----------
        - key: str
            An identifier for the line item
        - x: float | int | None
            X-coordinate for a vertical line, or None if adding a horizontal line. Ignored if `y` is specified.
        - y: float | int | None
            Y-coordinate for a horizontal line, or None if adding a vertical line. Ignored if `x` is specified.
        - color: str, optional
            The color for the line. If not provided, a default white line will be used.
        - pen_style: Qt.PenStyle, optional
            The pen style for the line. If not provided, a default dashed line will be used (style: `Qt.PenStyle.DashLine`).
        """
        self.plot_items[key] = self.addLine(y=y, x=x, pen=pg.mkPen(color, style=pen_style))

    def add_colorbar(
        self,
        item_key: str,
        min_value: int | float,
        max_value: int | float,
        colormap_type: Literal["hot", "cool"] = "cool",
    ) -> None:
        """
        Adds a color bar to the plot based on the specified colormap and value range. The color bar
        visually represents the mapping of data values to colors, using either a 'cool' or 'hot' colormap.

        Parameters:
        ----------
        item_key : str
            The key used to store and reference the color bar within the plot items dictionary.
        min_value : int | float
            The minimum value represented by the color bar (corresponds to the lower bound of the colormap).
        max_value : int | float
            The maximum value represented by the color bar (corresponds to the upper bound of the colormap).
        colormap_type : Literal["hot", "cool"], optional
            The type of colormap to use for the color bar. Options are:
            - "cool": The colormap transitions from cyan to magenta (default).
            - "hot": The colormap transitions from black to red, yellow, and white.
        """
        colorbar = pg.GradientLegend((10, 100), (10, 100))
        if colormap_type == "cool":
            pos, color = FlimUtils.create_cool_colormap(0, 1)
            colormap = pg.ColorMap(pos, color)
        else:
            pos, color = FlimUtils.create_hot_colormap()
            colormap = pg.ColorMap(pos, color)
        colorbar.setColorMap(colormap)
        colorbar.setLabels({f"{min_value}": 0, f"{max_value}": 1})
        self.addItem(colorbar)
        self.plot_items[item_key] = colorbar

    def draw_semi_circle(
    self,
    data_set_key: str,
    center_x: float = 0.5,
    center_y: float = 0,
    radius: float = 0.5,
    num_points: int = 1000,
    color: str = "#1E90FF",
    width: int = 2,
    orientation: Literal["up", "down", "left", "right"] = "up",
    ) -> None:
        """
        Draws a semi-circle on the plot, customizable by center position, radius, color, width, and orientation.

        Parameters:
        - data_set_key : str
            A data-set key to identify the set of data
        - center_x: float, optional
            X-coordinate of the center of the semi-circle.
        - center_y: float, optional
            Y-coordinate of the center of the semi-circle.
        - radius: float, optional
            Radius of the semi-circle.
        - num_points: int, optional
            Number of points to generate the semi-circle (default is 1000).
        - color: str, optional
            Color of the semi-circle (default is "#1E90FF").
        - width: int, optional
            Line width of the semi-circle (default is 2).
        - orientation: Literal["up", "down", "left", "right"], optional
            Orientation of the semi-circle, can be "up", "down", "left", "right" (default is "up").
        """
        # Generate x values depending on the orientation
        if orientation in ["up", "down"]:
            x = np.linspace(center_x - radius, center_x + radius, num_points)
            y = np.sqrt(
                radius**2 - (x - center_x) ** 2
            )  # Calculate y-values for the semi-circle
            if orientation == "down":
                y = -y
            # Ensure y values are within the bounds
            y = np.clip(y + center_y, center_y - radius, center_y + radius)
        elif orientation in ["left", "right"]:
            y = np.linspace(center_y - radius, center_y + radius, num_points)
            x = np.sqrt(radius**2 - (y - center_y) ** 2)
            if orientation == "left":
                x = -x
            # Ensure x values are within the bounds
            x = np.clip(x + center_x, center_x - radius, center_x + radius)

        # Plot the semi-circle
        self.plot_data[data_set_key] = self.plot(
            x, y, pen=pg.mkPen(color=color, width=width)
        )
        # Optionally plot the base of the semi-circle (line)
        if orientation in ["up", "down"]:
            self.plot(
                [center_x - radius, center_x + radius],
                [center_y, center_y],
                pen=pg.mkPen(color=color, width=width),
            )
        elif orientation in ["left", "right"]:
            self.plot(
                [center_x, center_x],
                [center_y - radius, center_y + radius],
                pen=pg.mkPen(color=color, width=width),
            )

    def add_text_item(
        self,
        key: str,
        params: PlotTextItemParams,
        z_index: int | None = None,
        ignore_bounds: bool = False,
    ) -> None:
        """
        Add a text item to the plot.

        Parameters
        ----------
        key: str
            A key to identify the TextItem
        params : PlotTextItemParams
            Parameters for the text item, including text content, font size, color, and anchor.
        z_index : int | None, optional
            The Z-index for the text item, which determines its drawing order (default is None).
        ignore_bounds : bool, optional
            Whether to ignore plot bounds for the text item (default is False).
        """
        if params["is_html"]:
            text_item = pg.TextItem(html=params["text"])
        else:
            font = QFont()
            font.setPixelSize(params["pixel_size"])
            text_item = pg.TextItem(
                text=params["text"], color=params["color"], anchor=params["anchor"]
            )
            text_item.setFont(font)

        if params["position"] is not None:
            text_item.setPos(params["position"][0], params["position"][1])
        if z_index is not None:
            text_item.setZValue(z_index)
        self.addItem(text_item, ignoreBounds=ignore_bounds)
        self.plot_items[text_item] = text_item

    def add_plot_region(
        self,
        start: float,
        end: float,
        color: str | Tuple[int, int, int] | Tuple[int, int, int, int] | None,
    ) -> None:
        """
        Add a region of interest (ROI) to the plot.

        Parameters
        ----------
        start : float
            Starting point of the region along the X-axis.
        end : float
            Ending point of the region along the X-axis.
        color : str, Tuple[int,int,int], Tuple[int,int,int,int], optional
            The color of the region (default is None).
        """
        if self.region is None:
            self.region = pg.LinearRegionItem(values=(start, end), brush=color)
            self.addItem(self.region)
            self.region.sigRegionChanged.connect(self._region_changed_callback)

    def set_plot_region_data(self, data_set_key: str) -> None:
        """
        Update the stored data for the current region of interest.

        Parameters
        ----------
        data_set_key : str
            A data-set key to identify the set of data

        This method computes the data points within the current ROI and updates
        the stored region data.
        """
        if (
            data_set_key not in self.cached_x_data
            or data_set_key not in self.cached_y_data
        ):
            raise ValueError(
                "You must provide a valid data-set key to be able to identify the correct set of data"
            )
        min_x, max_x = self.region.getRegion()
        mask = (self.cached_x_data[data_set_key] >= min_x) & (
            self.cached_x_data[data_set_key] <= max_x
        )
        selected_x = self.cached_x_data[data_set_key][mask]
        selected_y = self.cached_y_data[data_set_key][mask]
        self.x_region_data = selected_x[data_set_key]
        self.y_region_data = selected_y[data_set_key]
        self.region_bounds = (min_x, max_x)

    def get_plot_region_data(
        self, data_set_key: str
    ) -> Tuple[np.ndarray, np.ndarray, Optional[Tuple[float, float]]]:
        """
        Retrieve the data for the current region of interest.

        Parameters
        ----------
        data_set_key : str
            A data-set key to identify the set of data

        Returns
        -------
        Tuple[np.ndarray, np.ndarray, Optional[Tuple[float, float]]]
            The X and Y data points within the ROI, and the bounds of the ROI.
        """
        if (
            data_set_key not in self.x_region_data
            or data_set_key not in self.y_region_data
        ):
            raise ValueError(
                "You must provide a valid data-set key to be able to identify the correct set of data"
            )
        return (
            self.x_region_data[data_set_key],
            self.y_region_data[data_set_key],
            self.region_bounds,
        )

    def remove_plot_region(self) -> None:
        """
        Remove the active region of interest (ROI) from the plot.

        This method clears the ROI from the plot widget and resets related attributes.
        """
        if self.region is not None:
            self.removeItem(self.region)
            self.region = None

    def _region_changed_callback(self) -> None:
        """Callback function to handle changes in the ROI."""
        self.roi_changed.emit()

    def get_region_bounds(self) -> Optional[Tuple[float, float]]:
        """
        Get the current bounds of the active region of interest.

        Returns
        -------
        Optional[Tuple[float, float]]
            The (min, max) values of the ROI along the X-axis, or None if no ROI is active.
        """
        if self.region is not None:
            return self.region.getRegion()
        return None

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the plot widget.

        Parameters
        ----------
        visible : bool
            Whether the plot widget should be visible (True) or hidden (False).
        """
        self.setVisible(visible)
