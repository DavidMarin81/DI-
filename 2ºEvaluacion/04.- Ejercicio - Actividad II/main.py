import clients
import events
from ventana import *
import sys, var

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.btnAceptar.clicked.connect(events.Eventos.Saludo)
        var.ui.etDNI.editingFinished.connect(events.Eventos.validarDNI)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
