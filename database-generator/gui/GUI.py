import PyQt5 as pq5
import sys
        

from scripts_gui.ventana_ui import * 

# class MainWindow(QtWidgets.QDialog, Ui_Dialog):
#     def __init__(self, *args, **kwargs):
#         QtWidgets.QDialog.__init__(self, *args, **kwargs)
#         self.Dialog = QtWidgets.QDialog()
#         self.setupUi(self.Dialog)
    


class GUI(): 
    def __init__(self):
        print("Creating GUI...")
        self.setup()

    def setup(self): 
        print("Config...")
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_Dialog()
        self.Dialog = QtWidgets.QDialog()
        self.ui.setupUi(self.Dialog)

        print(self.ui.label)

        self.ui.label.setText("Haz clic en el botón")
        self.ui.pushButton.setText("Presióname")
        self.ui.pushButton.clicked.connect(self.update)

    def display(self): 
       
        self.Dialog.show()
        sys.exit(self.app.exec_())

    def update(self):
        self.ui.label.setText("Hola Mundo")



    
        
