from PyQt5 import QtCore, QtWidgets, QtGui
import sys

def send_notification(icon, name, text):
    app = QtWidgets.QApplication(sys.argv)
    screen = QtWidgets.QDesktopWidget().screeGeometry()

