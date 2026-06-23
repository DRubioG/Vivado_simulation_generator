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
        self.ui.setupUi(self)
        
        self.interconnection()
        self.init()

        self._sim = simulator_generator()


    def init(self):
        """Start method of the GUI.
        """
        self.json_option = True
        self.ui.pushButton_Search_XCI.setEnabled(False)
        self.ui.pushButton_Search_JSON.setEnabled(True)
        self.ui.radioButton_JSON.setChecked(True)
        self.ui.lineEdit_JSON.setEnabled(True)
        self.ui.lineEdit_XCI.setEnabled(False)
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
        self.ui.radioButton_XCI.pressed.connect(self.clicButton_JSON_XCI)
        self.ui.radioButton_JSON.pressed.connect(self.clicButton_JSON_XCI)
        self.ui.pushButton_Search_JSON.pressed.connect(self.clicButton_SearchJSON)
        self.ui.pushButton_Search_XCI.pressed.connect(self.clicButton_SearchXCI)




    def clicButton_SearchJSON(self):
        """Method to search JSONs files with the basic information of the IP.
        """
        self.path, _ = QFileDialog.getOpenFileName(
            self,
            "Search Files",
            "",
            "JSON (*.json)"
        )

        # Set the path in the GUI and remove the other
        self.ui.lineEdit_JSON.setText(self.path)
        self.ui.lineEdit_XCI.clear()
        

        


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
        self.ui.lineEdit_JSON.clear()



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
        

    def clicButton_JSON_XCI(self):
        """Callback to select which is the option JSON or XCI.
        """
        self.json_option = not self.json_option
        if self.json_option == True:
            self.ui.pushButton_Search_XCI.setEnabled(False)
            self.ui.pushButton_Search_JSON.setEnabled(True)
            self.ui.lineEdit_JSON.setEnabled(True)
            self.ui.lineEdit_XCI.setEnabled(False)
        else:
            self.ui.pushButton_Search_XCI.setEnabled(True)
            self.ui.pushButton_Search_JSON.setEnabled(False)
            self.ui.lineEdit_JSON.setEnabled(False)
            self.ui.lineEdit_XCI.setEnabled(True)

