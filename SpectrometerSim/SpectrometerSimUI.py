from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from IonSimulator import IonSimulator as IonSim
import numpy as np  
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        plotOffset = 20
        plotDPI = 100
        plotWidth = 8
        plotHeight = 6
        windowWidth = 960
        windowHeight = 640
        widgetYSpacing = 10
        fontSize = 12
        buttonWidth = 100
        buttonHeight = 50
        inputWidths = 80
        inputHeights = 20

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(windowWidth, windowHeight)
        
        font = QtGui.QFont()
        font.setPointSize(fontSize)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        plotWithOffset = plotOffset + plotWidth*plotDPI
        buttonXPos = plotWithOffset + (windowWidth - plotWithOffset - buttonWidth)/2
        buttonYPos = plotOffset
        self.simulateButton = QtWidgets.QPushButton(self.centralwidget)
        self.simulateButton.setGeometry(QtCore.QRect(buttonXPos, buttonYPos, buttonWidth, buttonHeight))
        self.simulateButton.setBaseSize(QtCore.QSize(0, 0))
        self.simulateButton.setFont(font)
        self.simulateButton.setObjectName("simulateButton")
        
        inputXPos = plotWithOffset + (windowWidth - plotWithOffset - inputWidths)/2
        inputYPos = buttonYPos + buttonHeight + widgetYSpacing
        self.massLabel = QtWidgets.QLabel(self.centralwidget)
        self.massLabel.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.massLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.massLabel.setObjectName("massLabel")

        inputYPos += inputHeights + widgetYSpacing
        self.massInput = QtWidgets.QLineEdit(self.centralwidget)
        self.massInput.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.massInput.setAlignment(QtCore.Qt.AlignCenter)
        self.massInput.setObjectName("massInput")

        inputYPos += inputHeights + widgetYSpacing
        self.chargeLabel = QtWidgets.QLabel(self.centralwidget)
        self.chargeLabel.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.chargeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chargeLabel.setObjectName("chargeLabel")

        inputYPos += inputHeights + widgetYSpacing
        self.chargeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.chargeInput.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.chargeInput.setAlignment(QtCore.Qt.AlignCenter)
        self.chargeInput.setObjectName("chargeInput")

        inputYPos += inputHeights + widgetYSpacing
        self.fieldLabel = QtWidgets.QLabel(self.centralwidget)
        self.fieldLabel.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.fieldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel.setObjectName("fieldLabel")

        inputYPos += inputHeights + widgetYSpacing
        self.fieldInput = QtWidgets.QLineEdit(self.centralwidget)
        self.fieldInput.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.fieldInput.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldInput.setObjectName("fieldInput")

        inputYPos += inputHeights + widgetYSpacing
        self.delayLabel = QtWidgets.QLabel(self.centralwidget)
        self.delayLabel.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.delayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.delayLabel.setObjectName("delayLabel")

        inputYPos += inputHeights + widgetYSpacing
        self.delayInput = QtWidgets.QLineEdit(self.centralwidget)
        self.delayInput.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.delayInput.setAlignment(QtCore.Qt.AlignCenter)
        self.delayInput.setObjectName("delayInput")
        self.rampLabel = QtWidgets.QLabel(self.centralwidget)

        inputYPos += inputHeights + widgetYSpacing
        self.rampLabel.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.rampLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rampLabel.setObjectName("rampLabel")

        inputYPos += inputHeights + widgetYSpacing
        self.rampInput = QtWidgets.QLineEdit(self.centralwidget)
        self.rampInput.setGeometry(QtCore.QRect(inputXPos, inputYPos, inputWidths, inputHeights))
        self.rampInput.setAlignment(QtCore.Qt.AlignCenter)
        self.rampInput.setObjectName("rampInput")

        self.canvas = PlotCanvas(MainWindow,width=plotWidth, height=plotHeight)
        self.canvas.move(20,20)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.simulateButton.setText(_translate("MainWindow", "Simulate!"))
        self.massLabel.setText(_translate("MainWindow", "Mass"))
        self.chargeLabel.setText(_translate("MainWindow", "Charge"))
        self.fieldLabel.setText(_translate("MainWindow", "Field Strength"))
        self.delayLabel.setText(_translate("MainWindow", "Delay"))
        self.rampLabel.setText(_translate("MainWindow", "Ramp"))

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi) 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = self.figure.add_subplot(111)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self) 

 
    def plot(self,x,y,desc='r.'):

        self.axes.plot(x,y,desc)
        self.axes.set_xlabel('tof ($\mu$s)')
        self.axes.set_ylabel('pos (mm)')
        self.draw()

    def clear(self):
        self.axes.clear()
        
def simulate(simulator,ui):
    ui.canvas.clear()
    try:
        simulator.spectrometer.mass_in_amu = int(ui.massInput.text())
    except:
        ui.massInput.setText(str(simulator.spectrometer.mass_in_amu))
    try:
        simulator.spectrometer.charge_in_amu = int(ui.chargeInput.text())
    except:
        ui.chargeInput.setText(str(simulator.spectrometer.charge_in_e))
    try:
        simulator.spectrometer.E_max = int(ui.fieldInput.text())
    except:
        ui.fieldInput.setText(str(simulator.spectrometer.E_max))
    try:
        simulator.spectrometer.delay = int(ui.delayInput.text())
    except:
        ui.delayInput.setText(str(eformat(simulator.spectrometer.delay,3,1)))
    try:
        simulator.spectrometer.ramp = int(ui.rampInput.text())
    except:
        ui.delayInput.setText(str(eformat(simulator.spectrometer.ramp,3,1)))

    simulator.Simulate()
    ui.canvas.plot(simulator.data['tof']*10**6,np.sqrt(simulator.data['x']**2 + simulator.data['y']**2)*10**3)
    ui.canvas.plot(simulator.polyFitX,simulator.polyFitY,'b-')

def eformat(f, prec, exp_digits):
    s = "%.*e"%(prec, f)
    mantissa, exp = s.split('e')
    # add 1 to digits as 1 is taken by sign +/-
    return "%se%+0*d"%(mantissa, exp_digits+1, int(exp))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    simulator = IonSim()
    ui.massInput.setText(str(simulator.spectrometer.mass_in_amu))
    ui.chargeInput.setText(str(simulator.spectrometer.charge_in_e))
    ui.fieldInput.setText(str(simulator.spectrometer.E_max))
    ui.delayInput.setText(str(eformat(simulator.spectrometer.delay,3,1)))
    ui.rampInput.setText(str(eformat(simulator.spectrometer.ramp,3,1)))
    ui.simulateButton.clicked.connect(lambda: simulate(simulator,ui))
    MainWindow.show()
    sys.exit(app.exec_())

