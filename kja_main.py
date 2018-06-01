# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:37:31 2018

@author: Yunus Önür
"""
import socket,struct,sys,time
from scipy.signal import kaiserord, lfilter, firwin, freqz
import gui_main
import scipy as sp
import bluetooth
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from numpy.linalg import norm
import matplotlib.pyplot as plt
import math
import sys
from numpy.random import rand
from Tkinter import *
import pyqtgraph
from os.path import join
import time

bd_addr = "20:17:03:08:54:67"
port = 1
data2 = []
class First(QMainWindow,gui_main.Ui_MainWindow):
    bluetoothsoket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    bluetoothsoket.settimeout(4)
    def __init__(self,parent=None):
        super(First,self).__init__(parent)
        self.setupUi(self)
        self.anglegraph.setTitle(title="Estimated Angle")
        self.anglegraph.showGrid(x=True,y=True,alpha=True)
        self.acceksenx.showGrid(x=True,y=True,alpha=True)
        self.accekseny.showGrid(x=True,y=True,alpha=True)
        self.acceksenz.showGrid(x=True,y=True,alpha=True)
        self.disconnectbutton.clicked.connect(self.disconnect)
        self.getfilebutton.clicked.connect(self.getfilesd)
        self.connectbutton.clicked.connect(self.connect)
        self.openfilebutton.clicked.connect(self.openfile)
        self.filterapply.clicked.connect(self.filterl)
#        self.anglegraph.setYRange(-180,180, padding=0)
    def filterl(self):
        cindex = self.comboBox.currentIndex()
        if cindex == 1:
            self.anglegraph.clear()
            b = firwin(13,0.15,pass_zero =True)
            signal = lfilter(b, 1, angle)
            self.anglegraph.plot(signal,pen='r')
        if cindex == 2:
            self.anglegraph.clear()
            b = firwin(13,0.0001,pass_zero =False)
            signal = lfilter(b, 1, angle)
            self.anglegraph.plot(signal,pen='r')
        if cindex == 0:
            self.anglegraph.clear()
            y1 = sp.signal.medfilt(angle,21)
            self.anglegraph.plot(y1,pen='r')
        if cindex == 3:
            self.anglegraph.clear()
            self.anglegraph.plot(angle,pen='b')
    def openfile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Choose file')
        data = np.loadtxt(fname,delimiter=',')
        global angle
        angle=list(map(lambda x,y:np.rad2deg(np.arccos(norm(np.dot(x,y))/norm(x)/norm(y))),data[:,:3],data[:,3:]))
        self.anglegraph.clear()
        self.acceksenx.clear()
        self.accekseny.clear()
        self.acceksenz.clear()
        self.anglegraph.plot(angle,pen='b')
        self.acceksenx.plot(data[:,0],pen='b')
        self.acceksenx.plot(data[:,3],pen='r')
        self.accekseny.plot(data[:,1],pen='b')
        self.accekseny.plot(data[:,4],pen='r')
        self.acceksenz.plot(data[:,2],pen='b')
        self.acceksenz.plot(data[:,5],pen='r')
    def getfilesd(self):
        data = "H"
        self.bluetoothsoket.settimeout(2)
        self.bluetoothsoket.send(data)
        time.sleep(2)
        file = open("deney",'w') 
        dataman=''
        cde = True
        print("1.kontrol")
        try:
            while cde:
                data2 = self.bluetoothsoket.recv(1024)
                dataman += data2
        except:
            print("2.kontrol")
            file.write(dataman)
            file.close()
            self.anglegraph.clear()
        print("3.kontrol")
        file = open("deney",'r')
        global angle
        data = np.loadtxt(file,delimiter=',')
        angle=list(map(lambda x,y:np.rad2deg(np.arccos(norm(np.dot(x,y))/norm(x)/norm(y))),data[:,:3],data[:,3:]))
        self.anglegraph.plot(angle,pen='b')
        self.acceksenx.clear()
        self.accekseny.clear()
        self.acceksenz.clear()
        self.acceksenx.plot(data[:,0],pen='b')
        self.acceksenx.plot(data[:,3],pen='r')
        self.accekseny.plot(data[:,1],pen='b')
        self.accekseny.plot(data[:,4],pen='r')
        self.acceksenz.plot(data[:,2],pen='b')
        self.acceksenz.plot(data[:,5],pen='r')
    def disconnect(self):
        self.bluetoothsoket.close()
    def connect(self):
        try:
            self.bluetoothsoket.connect((bd_addr,port))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Connection is succesful.")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Connection is failed. Try again.")
            msg.setWindowTitle("Bluetooth Connection")
            msg.setDetailedText('The details are as follows:''/n' 
                                    "Check is bluetooth busy?""/t"
                                    "Check your bluetooth app"
                                    "Check system power connection"
                                    "")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
appp=QApplication(sys.argv)
form=First()
form.show()
appp.exec_()
