from PyQt5 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("di.ui")  # type: <class 'PyQt4.QtGui.QWidget'>
QtCore.QObject.connect(window.butQuit, QtCore.SIGNAL("clicked()"),
                       QtGui.qApp.quit)
window.show()
sys.exit(app.exec_())