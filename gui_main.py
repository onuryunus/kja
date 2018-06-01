
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1292, 874)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1651, 921))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 20, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 114, 255), stop:1 rgba(0, 0, 164, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"border-width: 1px;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.openfilebutton = QtGui.QPushButton(self.centralwidget)
        self.openfilebutton.setGeometry(QtCore.QRect(620, 20, 151, 31))
        self.openfilebutton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 96, 255));\n"
"color: rgb(255, 255, 255);"))
        self.openfilebutton.setObjectName(_fromUtf8("openfilebutton"))
        self.getfilebutton = QtGui.QPushButton(self.centralwidget)
        self.getfilebutton.setGeometry(QtCore.QRect(490, 20, 131, 31))
        self.getfilebutton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 96, 255));\n"
"color: rgb(255, 255, 255);"))
        self.getfilebutton.setObjectName(_fromUtf8("getfilebutton"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 1251, 731))
        self.tabWidget.setStyleSheet(_fromUtf8("image: url(:/newPrefix/sa.png);"))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.anglegraph = PlotWidget(self.tab)
        self.anglegraph.setGeometry(QtCore.QRect(10, 80, 1221, 601))
        self.anglegraph.setStyleSheet(_fromUtf8(""))
        self.anglegraph.setObjectName(_fromUtf8("anglegraph"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(830, 20, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 114, 255), stop:1 rgba(0, 0, 164, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"border-width: 1px;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.filterapply = QtGui.QPushButton(self.tab)
        self.filterapply.setGeometry(QtCore.QRect(1130, 20, 91, 31))
        self.filterapply.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 96, 255));\n"
"color: rgb(255, 255, 255);"))
        self.filterapply.setObjectName(_fromUtf8("filterapply"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(910, 20, 221, 31))
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 74, 255), stop:1 rgba(0, 0, 114, 255));"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 1221, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Unicode"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 1221, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Unicode"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.acceksenx = PlotWidget(self.tab_3)
        self.acceksenx.setGeometry(QtCore.QRect(10, 30, 1231, 191))
        self.acceksenx.setObjectName(_fromUtf8("acceksenx"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 450, 1221, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Unicode"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.acceksenz = PlotWidget(self.tab_3)
        self.acceksenz.setGeometry(QtCore.QRect(10, 470, 1231, 191))
        self.acceksenz.setObjectName(_fromUtf8("acceksenz"))
        self.accekseny = PlotWidget(self.tab_3)
        self.accekseny.setGeometry(QtCore.QRect(10, 250, 1231, 191))
        self.accekseny.setObjectName(_fromUtf8("accekseny"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 114, 255), stop:1 rgba(0, 0, 164, 255));\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"border-width: 1px;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.connectbutton = QtGui.QPushButton(self.centralwidget)
        self.connectbutton.setGeometry(QtCore.QRect(150, 20, 91, 31))
        self.connectbutton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 96, 255));\n"
"color: rgb(255, 255, 255);"))
        self.connectbutton.setObjectName(_fromUtf8("connectbutton"))
        self.disconnectbutton = QtGui.QPushButton(self.centralwidget)
        self.disconnectbutton.setGeometry(QtCore.QRect(240, 20, 91, 31))
        self.disconnectbutton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 1, 38, 255), stop:0.522388 rgba(0, 0, 68, 255), stop:1 rgba(0, 0, 96, 255));\n"
"color: rgb(255, 255, 255);"))
        self.disconnectbutton.setObjectName(_fromUtf8("disconnectbutton"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 60, 1251, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-20, 10, 121, 51))
        self.label_4.setStyleSheet(_fromUtf8("image: url(:/newPrefix/das.png);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 10, 140, 46))
        self.label_5.setStyleSheet(_fromUtf8("image: url(:/newPrefix/asfsf.png);"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Knee Joint Analysis", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/sa.png\"/></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "       SD Card", None))
        self.openfilebutton.setText(_translate("MainWindow", "Open File from Computer", None))
        self.getfilebutton.setText(_translate("MainWindow", "Plot Last Experiment", None))
        self.label_8.setText(_translate("MainWindow", "Filters :", None))
        self.filterapply.setText(_translate("MainWindow", "Apply", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Median Filter", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Lowpass Filter", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Highpass Filter", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Return Original Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Estimated Angle", None))
        self.label_2.setText(_translate("MainWindow", "Y Raw Data", None))
        self.label_3.setText(_translate("MainWindow", "X Raw Data", None))
        self.label_9.setText(_translate("MainWindow", "Z Raw Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Raw Data", None))
        self.label_7.setText(_translate("MainWindow", "           Bluetooth", None))
        self.connectbutton.setText(_translate("MainWindow", "Connect", None))
        self.disconnectbutton.setText(_translate("MainWindow", "Disconnect", None))

from pyqtgraph import PlotWidget
import gui_maincomponents_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

