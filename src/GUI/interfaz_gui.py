from PySide6.QtWidgets import QMainWindow, QFileDialog
from UI.interface_ui import Ui_MainWindow
import json
from simulator.simulator_generator import *

class interfaz_gui(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.interconnection()
        self.init()

        self._sim = simulator_generator()


    def init(self):
        pass

    def interconnection(self):
        self.ui.pushButton_cancel.pressed.connect(self.clicButton_Cancel)
        self.ui.pushButton_generate.pressed.connect(self.clicButton_Generate)
        self.ui.pushButton_output_path.pressed.connect(self.clicButton_SearchOutputFiles)
        self.ui.radioButton_XCI.pressed.connect(self.clicButton_JSON_XCI)
        self.ui.radioButton_JSON.pressed.connect(self.clicButton_JSON_XCI)
        self.ui.pushButton_Search_JSON.pressed.connect(self.clicButton_SearchJSON)
        self.ui.pushButton_Search_XCI.pressed.connect(self.clicButton_SearchXCI)




    def clicButton_SearchJSON(self):
        self.path, _ = QFileDialog.getOpenFileName(
            self,
            "Search Files",
            "",
            "JSON (*.json)"
        )

        self.ui.lineEdit_JSON.setText(self.path)
        

        


    def clicButton_SearchXCI(self):
        pass

    def clicButton_SearchOutputFiles(self):
        pass

    def clicButton_Generate(self):
        if self.path:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._sim.simulator_generator(json_file=data)

    def clicButton_Cancel(self):
        pass

    def clicButton_simFolder(self):
        pass

    def clicButton_Readme(self):
        pass

    def clicButton_JSON_XCI(self):
        pass
