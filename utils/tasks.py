from PyQt6.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
import matplotlib.pyplot as plt

class TaskSignals(QObject):
    """
    Signals for task completion and errors.
    """
    success = pyqtSignal(str)
    error = pyqtSignal(str)
    

class SavePlotImageTask(QRunnable):
    def __init__(self, plot, base_path: str, signals: TaskSignals, formats: list = None):
        """
        Initialize the SavePlotImageTask with plot, base path, signals, and optional formats.

        Parameters:
        ----------
        plot : plt.Figure
            The matplotlib plot to save.
        base_path : str
            The base path (without extension) where the plot will be saved.
        signals : TaskSignals
            The signals object to emit success or error messages.
        formats : list of str
            List of formats to save the plot in (e.g., ['png', 'eps']). Defaults to ['png', 'eps'].
        """
        super().__init__()
        self.plot = plot
        self.base_path = base_path
        self.signals = signals
        self.formats = formats if formats else ['png', 'eps']

    @pyqtSlot()
    def run(self):
        """
        Execute the task of saving the plot in specified formats.
        """
        try:
            for format in self.formats:
                file_path = f"{self.base_path}.{format}"
                self.plot.savefig(file_path, format=format)
            plt.close(self.plot)
            self.signals.success.emit(
                f"Plot images saved successfully as {', '.join([f'{self.base_path}.{format}' for format in self.formats])}"
            )
        except Exception as e:
            plt.close(self.plot)
            self.signals.error.emit(str(e))