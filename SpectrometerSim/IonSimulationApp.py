from SpectrometerSimUI import *
from IonSimulator import IonSimulator
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    simulator = IonSimulator()
    ui.massInput.setText(str(simulator.particle_mass_amu))
    ui.chargeInput.setText(str(simulator.particle_charge_C))
    ui.fieldInput.setText(str(simulator.spectrometer.E_max))
    ui.delayInput.setText(str(eformat(simulator.spectrometer.delay,3,1)))
    ui.rampInput.setText(str(eformat(simulator.spectrometer.ramp,3,1)))
    ui.simulateButton.clicked.connect(lambda: simulate(simulator,ui))
    MainWindow.show()
    sys.exit(app.exec_())