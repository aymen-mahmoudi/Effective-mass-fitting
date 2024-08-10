from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
 

import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from functions import*

#  import the gui :
gui_py = True

if gui_py == True :
    from gui import Ui_Form  as ui
else:
    ui, _ = loadUiType('gui.ui')

class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        #self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        # desactivate buttons
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # First empty plot
        self.plot_layout()
        # function to setup buttons
        self.HandleButtons()
        
        
    def HandleButtons(self):
        self.clickHere_pushButton.clicked.connect(self.essential_values)
        self.clickHere_pushButton.clicked.connect(self.plot)
        # output (set)
        self.clickHere_pushButton.clicked.connect(self.set_mass)
        self.clickHere_pushButton.clicked.connect(self.set_seebeck)
        self.clickHere_pushButton.clicked.connect(self.set_path)
        # browsing buton
        self.browse_pushButton.clicked.connect(self.load_image)

    def plot_layout(self):
        self.fig = plt.figure(facecolor='#a5a6a5')
        self.canvas = FigureCanvas(self.fig)
        toolbar = NavigationToolbar(self.canvas, self)
        self.plottingSpace_verticalLayout.addWidget(toolbar)
        self.plottingSpace_verticalLayout.addWidget(self.canvas)

    def load_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName = QFileDialog.getOpenFileName(self, 'choose image',"", "",
        options=options)
        # Check If The User Did not Entered File Name To Save Configuration Into
        if self.fileName[0] == '':
            return 
        else : 
            print(self.fileName[0])




    

    def plot(self):
        print('here ' , self.fileName[0])
        print('nnnnn',self.n)
        print('ttttt',self.T)
        self.fig.clear()
        ax = self.fig.add_subplot(111, facecolor='green')
        ax.set_aspect('equal')
       
        

        #self.pic = plt.imread(r"C:/Users/aymen.mahmoudi/Sync_Drive_2/Thése/Python Tools/Seebeck Calculator/flake1_5.jpg")
        ax.imshow(self.pic,extent=[self.kmin,self.kmax,self.Emin,self.Emax],aspect='auto')
        #ax.imshow(self.pic,extent=[1,3,self.Emin,self.Emax],aspect='auto')
        #ax.imshow(self.pic,extent=[self.kmin,self.kmax,self.Emin,self.Emax],aspect = 'auto')
        #ax.imshow(self.pic,extent=[2,3,44,35],aspect = 'auto')
        #ax.imshow(self.pic,extent = [self.kmin,22,4,self.Emax],aspect = 'auto')

        x = np.linspace(self.curve_center-self.curve_length,self.curve_center+self.curve_length,100)
        y = self.concavity*np.power((x-self.curve_center),2) + self.curve_E0
        concavity_converted = self.concavity * (1E-20)*(1.60218E-19)
        self.m = np.power(hbar,2)/(2*concavity_converted*m0)
        self.m=np.abs(self.m)

        print('verif', min(x),max(x))
        print(type(self.curve_length))

        # Saving image settings :

        ax.plot(x, y,color = self.color, ls = self.ls,lw = self.lw)
        print ('Concavity in J/m2 : ',concavity_converted)
        print('m*/m0 : ',m)


        print('energy',self.Emin,self.Emax)
        print('verrii', self.color,self.ls,self.lw)
            

        #ax.hlines(0, 0, self.GK, colors='b', lw = 3, linestyles='--')
        #ax.vlines(0, 0, self.GM, colors='b', lw = 3,linestyles='--')
       
        # ax.add_line(line1)
        # ax.add_line(line2)

        #ax.set_xlim(0,10)
        #ax.set_ylim(0,3)

        

        ax.set_title('Parabolic approximation',fontsize = 16)
        ax.set_xlabel('k$_{x}$ (A$^{-1}$)', fontsize=16)
        ax.set_ylabel('E - E$_{F}$ (eV)', fontsize=16)

        #plt.axis('scaled')
        plt.autoscale(enable = True)
        #plt.axis("off")
        

        self.fig.tight_layout()
        self.canvas.draw()

        print('here ' , self.fileName[0])

        
        
        

       

                

    
    def essential_values(self):
        # Global Varilables

        print ('essential values here')
        self.T = 0 ; self.E = 0 ; self.n = 0 ; self.kmin = 0 ; self.kmax = 0 ; self.Emin = 0 ; self.Emax = 0 ;  self.pic = 0 
        self.curve_length =0 ;  self.curve_center = 0 ; self.concavity = 0 ; self.curve_E0 = 0 
        self.m = 0
        self.ls = ''
        self.lw = 0
        self.color = ''

        # if self.ls == '':
        #     return


        self.pic = plt.imread(self.fileName[0])
        self.T = float(self.get_T())
        self.E = float(self.get_E())
        self.n = float(self.get_n())

        print('hhhhhhhhhhhhhhh')

        self.kmin = float(self.get_kmin())
        self.kmax = float(self.get_kmax())
        self.Emin = float(self.get_Emin())
        self.Emax = float(self.get_Emax())

        self.curve_length = float(self.get_curve_length())
        self.concavity = float(self.get_concavity())
        self.curve_center = float(self.get_curve_center())
        self.curve_E0 = float(self.get_curve_E0())
        
        self.ls = self.get_ls()
        self.lw = int(self.get_lw())
        self.color = self.get_color()

        
        
     

       
        

    def get_T(self):
        T = self.T_lineEdit.text()
        return T


    def get_E(self):
        E = self.E_lineEdit.text()
        return E
    
    def get_n(self):
        n = self.n_lineEdit.text()
        return n

    def get_kmin(self):
        kmin = self.kmin_lineEdit.text()
        return kmin

    def get_kmax(self):
        kmax = self.kmax_lineEdit.text()
        return kmax

    def get_Emin(self):
        Emin = self.Emin_lineEdit.text()
        return Emin

    def get_Emax(self):
        Emax = self.Emax_lineEdit.text()
        return Emax

    def get_curve_length(self):
        curve_length = self.curve_length_lineEdit.text()
        return curve_length


    def get_curve_E0(self):
        curve_E0 = self.curve_E0_lineEdit.text()
        return curve_E0

    def get_curve_center(self):
        curve_center = self.curve_center_lineEdit.text()
        return curve_center

    def get_concavity(self):
        concavity = self.concavity_lineEdit.text()
        return concavity

    def get_ls(self):
        ls = self.ls_comboBox.currentText()
        return ls

    def get_lw(self):
        lw = self.lw_comboBox.currentText()
        return lw

    def get_color(self):
        color = self.color_comboBox.currentText()
        return color
        

  

  


    #function showing value

    def set_seebeck(self):
        self.seebeck_output_label.setText(str(seebeck(self.T,self.m,self.n)))

    def set_mass(self):
        self.mass_output_label.setText(str(np.round(self.m,4)))

    def set_path(self):
        self.path_output_label.setText(self.fileName[0])

    



        


 

            
                
                



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()



