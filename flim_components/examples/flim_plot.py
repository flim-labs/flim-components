import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import numpy as np
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt6.QtCore import QTimer
from components.plots.flim_plot import FlimPlot


class BasePlotExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Base Plot Example")
        self.setStyleSheet("background-color: #121212; color: white;")

        # Create a grid layout for the plots
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Create plots and add them to layout
        self.create_plots()

    def create_plots(self):
        # Plot 1: Static Sine Curves
        self.plot1 = FlimPlot(title="Static Sine Curves", visible=True)
        self.layout.addWidget(self.plot1, 0, 0)  # Add to row 0, column 0
        self.plot_static_sine()

        # Plot 2: Static Scatter Plot with Labels and Legend
        self.plot2 = FlimPlot(title="Static Scatter Plot", visible=True)
        self.layout.addWidget(self.plot2, 0, 1)  # Add to row 0, column 1
        self.plot_static_scatter()

        # Plot 3: Real-Time Updating Sine Curve
        self.plot3 = FlimPlot(title="Real-Time Sine Curve", visible=True)
        self.layout.addWidget(self.plot3, 1, 0)  # Add to row 1, column 0

        # Timer for updating the real-time plot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_real_time_plot)
        self.timer.start(100)  # Update every 100 ms

        # Initialize real-time plot data
        self.plot_real_time_sine()

        # Plot 4: Region Example
        self.plot4 = FlimPlot(title="Plot with Region", visible=True)
        self.layout.addWidget(self.plot4, 1, 1)  # Add to row 1, column 1
        self.plot_region_example()

    def plot_static_sine(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x) * 100000 + 100000
        y2 = np.sin(2 * x) * 100000 + 100000
        self.plot1.init_plot(
            x=x,
            y=y,
            data_set_key="static_sine_1",
            log_mode=True,
            format_ticks=True,
            plot_grid_config=None,
            pen=pg.mkPen(color="b", width=2),
            legend_name="Sine Curve 1",
            legend_offset=(0, 20),
        )
        self.plot1.init_plot(
            x=x,
            y=y2,
            data_set_key="static_sine_2",
            log_mode=True,
            format_ticks=True,
            plot_grid_config=None,
            pen=pg.mkPen(color="r", width=2),
            legend_name="Sine Curve 2",
            legend_offset=(0, 20),
        )
       

    def plot_static_scatter(self):
        np.random.seed(0)
        x = np.random.uniform(0, 1, 100) 
        y = np.random.uniform(0, 0.5, 100)
        text_items = [
            {
                "text": f"Point {i + 1}",
                "is_html": False,
                "position": (x[i], y[i]),
                "pixel_size": 20,
                "color": "yellow",
                "anchor": (0, 0),
            }
            for i in range(len(x))
        ]
        self.plot2.setAspectLocked(True)
        self.plot2.add_scatter_point(
            x=np.array(x),
            y=np.array(y),
            scatter_key="scatter",
            text_item_key="scatter_text",
            text_item=text_items[0],  # Add one text item for demonstration
            style={"size": 10, "pen": None, "brush": "r", "symbol": "o"},
        )
        self.plot2.set_range(x_range=(0,1,0), y_range=(0, 0.5, 0))  # Limit x-axis from 0 to 1
        self.plot2.add_legend(offset=(10, 20))
        self.plot2.draw_semi_circle(data_set_key="semi_circle_1", color="purple")
        self.plot2.add_line("line", None, 0.2)

    def plot_real_time_sine(self):
        self.max_x = 10  # Maximum x value for the plot
        self.num_points = 100  # Number of points to display

        # Initialize x and y data
        self.real_time_x = np.linspace(0, self.max_x, self.num_points)
        self.real_time_y = np.sin(self.real_time_x) * 100000

        # Init the plot
        self.plot3.init_plot(
            x=self.real_time_x,
            y=self.real_time_y,
            data_set_key="realtime_sine",
            log_mode=True,
            format_ticks=True,
            plot_grid_config={"show_x": True, "show_y": True, "alpha": 0.3},
            pen=pg.mkPen(color="g", width=2),
        )

    def update_real_time_plot(self):
        # Shift data left
        self.real_time_x[:-1] = self.real_time_x[1:]
        self.real_time_y[:-1] = self.real_time_y[1:]

        # Append new data to the end
        self.real_time_x[-1] += self.max_x / self.num_points
        self.real_time_y[-1] = np.sin(self.real_time_x[-1]) * 100000

        # Update plot
        self.plot3.update_plot(
            x=self.real_time_x,
            y=self.real_time_y,
            data_set_key="realtime_sine",
            log_mode=True,
            format_ticks=True,
            plot_grid_config={"show_x": True, "show_y": True, "alpha": 0.3},
        )

    def plot_region_example(self):
        # Create data for the region plot
        x = np.linspace(0, 25, 256)
        y = np.array(
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                2715,
                129675,
                156859,
                156862,
                156855,
                156859,
                156855,
                156862,
                156857,
                156855,
                156862,
                156859,
                156857,
                156861,
                156864,
                156855,
                151141,
                20378,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        )

        # Update the plot
        self.plot4.init_plot(
            x=x,
            y=y,
            data_set_key="region_plot",
            log_mode=False,
            format_ticks=False,
            pen=pg.mkPen(color="y", width=2),
            shift=100
        )
        # Define the region to highlight
        region_start = 2
        region_end = 4

        # Add region to the plot
        self.plot4.add_plot_region(
            start=region_start, end=region_end, color=(255, 255, 0, 76)
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasePlotExampleWindow()
    window.show()
    sys.exit(app.exec())
