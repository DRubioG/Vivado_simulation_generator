from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication, QStatusBar
from UI.interface_ui import Ui_SimulatorGenerator
import json
from simulator.simulator_generator import *

class interfaz_gui(QMainWindow):
    """Class that controlles the interface.

    Args:
        QMainWindow (Class): class that depends the interface.
    """
    def __init__(self):
        """Class constructor
        """
        super().__init__()
        self.ui = Ui_SimulatorGenerator()
        ()
        self.ui.setupUi(self)
        
        self.interconnection()
        self.init()

        self._sim = simulator_generator()


    def init(self):
        """Start method of the GUI.
        """
        
        self.ui.checkBox_sim_folder.setChecked(True)
        self.ui.checkBox_readme.setEnabled(False)

        # Version
        status_bar = QStatusBar()
        status_bar.showMessage("Version: 0.1")
        self.setStatusBar(status_bar)


    def interconnection(self):
        """Method that connects the interface with Python.
        """
        self.ui.pushButton_cancel.pressed.connect(self.clicButton_Cancel)
        self.ui.pushButton_generate.pressed.connect(self.clicButton_Generate)
        self.ui.pushButton_output_path.pressed.connect(self.clicButton_SearchOutputFiles)
        self.ui.pushButton_Search_XCI.pressed.connect(self.clicButton_SearchXCI)




        

        


    def clicButton_SearchXCI(self):
        """Method to search XCI files with the IP.
        """
        self.path, _ = QFileDialog.getOpenFileName(
            self,
            "Search Files",
            "",
            "XCI (*.xci)"
        )

        # Set the path in the GUI and remove the other
        self.ui.lineEdit_XCI.setText(self.path)



    def clicButton_SearchOutputFiles(self):
        """Method to select the path.
        """
        pass

    def clicButton_Generate(self):
        """Method to generate the files.
        """
        if self.path:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

                sim_folder = self.ui.checkBox_sim_folder.isChecked()
                self._sim.simulator_generator(json_file=data, sim_folder=sim_folder)

    def clicButton_Cancel(self):
        """Callback of the Cancel button.
        """
        QApplication.quit()
        

