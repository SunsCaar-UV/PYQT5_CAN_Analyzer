from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import can
import time
import sys
import threading 
import logging
from Testgui import Ui_MainWindow
# from main import MainUI
class CanHandler(QObject):
    candata = pyqtSignal(list)
    cantxdata = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        # # self.ui.setupUi(self)
        
        self.bus_receive = can.Bus(interface='pcan', channel='PCAN_USBBUS1')
    
    def start_can_receive(self):
        self.listener = can.listener.BufferedReader()
        self.notifier = can.Notifier(self.bus_receive, [self.listener])
        while True:
             self.message_received = self.listener.get_message(1)
             if self.message_received is not None:
                self.data_to_emit = [self.message_received.arbitration_id, self.message_received.dlc, *self.message_received.data]  # Example data extraction
                print(self.data_to_emit)
                self.candata.emit(self.data_to_emit)  
                logging.info(str(self.message_received))  # Log received message
                print(str(self.message_received))
             else:
                print("passed")
                pass
    pyqtSlot(list)
    def start_can_send(self, transmit_data ):
        print("sending")
        self.can_messages = []
        try:
            arbitration_id = int(transmit_data[0])
            timestamp = time.time()
            dlc = int(transmit_data[1])
            data = [int(value) for value in transmit_data[2:]]  # Convert data to integers
            self.msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False, is_rx= False, timestamp= timestamp)
        except ValueError:
            print("Invalid data in row:", transmit_data)    
        
        self.bus_receive.send(self.msg)
        # self.i+=1
        print(f"Message sent on {self.bus_receive.channel_info}")
        logging.info(str(self.msg))  # Log transmitted message
        time.sleep(0.5)
    
    