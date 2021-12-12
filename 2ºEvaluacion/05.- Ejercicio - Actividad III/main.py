import clients
import events
from ventana import *
from windowaviso import *
import sys, var

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.etDNI.editingFinished.connect(events.Eventos.validarDNI)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSalir = Ui_Dialog()
        var.dlgSalir.setupUi(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.validarDNI)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgSalir = DialogSalir()
    window.show()
    sys.exit(app.exec())
