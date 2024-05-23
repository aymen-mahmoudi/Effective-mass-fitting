import numpy as np


# Physical constants
h = 6.62607015E-34
hbar = 1.05457182E-34
m = 9.1093837E-31
kb = 1.380649E-23
e = 1.60217663E-19
m0 = 9.1093837E-31


def seebeck(T,m_r,n):
    alpha = (8*np.power((kb*np.pi)/h,2)/(3*e))*np.power(np.pi/(3*n*10E6),2/3) *m_r*m0* T
    #alpha = 33
    print ('Coeifficient de Seebeck pour T = '+str(T)+'K vaut : '+str(alpha*10E6)+' \u03BCV/K')
    return alpha




















# class Utilities:


#     def __init__(self):
#         # Physical constants
#         self.hbar = 1.05457182E-34
#         self.m = 9.1093837E-31
        



#     def k2theta(self,E,k):
#         Ejoule = E *1.6E-19
#         theta = np.arcsin((k/np.sqrt(Ejoule))*(self.hbar/np.sqrt(2*self.m)))
#         return theta
