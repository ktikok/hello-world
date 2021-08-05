# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:46:29 2021

@author: pcname
https://medium.com/analytics-vidhya/how-to-build-your-first-desktop-application-in-python-7568c7d74311

"""

import sys
from time import strftime, gmtime
import threading
from time import sleep

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal

class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])

    def updater(self, curr_time):
        self.updated.emit(curr_time)
        
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
    
    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(0.1)
            
            
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./MathFormula2.qml')
#'''
back_end = Backend()

engine.rootObjects()[0].setProperty('backend', back_end)

back_end.bootUp()
#'''
sys.exit(app.exec())