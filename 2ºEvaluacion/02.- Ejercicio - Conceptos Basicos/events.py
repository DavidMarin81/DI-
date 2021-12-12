import var

class Eventos():
    def Saludo(self):
        try:
            var.ui.lblHola.setText('Has pulsado el boton')
        except Exception as error:
            print('Error: %s ' % str(error))