import sys

from PySide2.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

#from PySide2.uic import loadUi
from ui.main_window_ui import Ui_MainWindow

from modules.audio_loop import AudioLoop

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()
        self.setup_plot()
        self.al = AudioLoop()
        self.refresh_int = 0.2
        self.fft_size = 1024

    def setup_plot(self):
        self.plot = FigureCanvas(Figure())
        self.horizontalLayout.takeAt(0)
        self.horizontalLayout.insertWidget(0,self.plot)
        self.horizontalLayout.setStretch(0,1)
        self._dynamic_ax = self.plot.figure.subplots()
        self._line = self._dynamic_ax.plot([1,-1,1,-1,1])


    def connectSignalsSlots(self):
        self.actionAbout.triggered.connect(self.about)

    def about(self):
        QMessageBox.about(
            self,
            "About Formorant",
            "<p> A vocal resonance andtuner trainer</p>"
            "<p> By the <a href=""https://www.phys.unsw.edu.au/music/"">music acoustics group at UNSW</a></p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )
    
    def update_canvas(self):
        self.al.get_data()
        self._line.set_data([0,0,0,0,0])
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())