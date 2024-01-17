from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
import can
import time
import sys
import threading 
import logging
from Testgui import Ui_MainWindow
from can_handler import CanHandler
class MainUI(QMainWindow):
   
    i =0
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # loadUi("D:\PyQT\Test\Testgui.ui", self)
        self.tablewidget()
        self.can_handler = CanHandler()  # Create CanHandler instance
        self.ui.actionconnect.triggered.connect(self.dummy_thread)
        # self.actiondisconnect.triggered.connect(self.disconnecthandler)
        self.ui.transmit.clicked.connect(self.getcellvalue)
        self.can_handler.candata.connect(self.update_receivetable)
        self.can_handler.cantxdata.connect(self.can_handler.start_can_send)
        self.ui.start_log.clicked.connect(self.logging)
        self.ui.stop_log.clicked.connect(self.logging)
        self.filename_edit = self.findChild(QTextEdit, "logfilename")
         
        self.log_file = None
        
    def dummy_thread(self):
        threading.Thread(target=lambda: self.can_handler.start_can_receive()).start()
        threading.Thread(target=lambda: self.can_handler.start_can_send()).start()

    def tablewidget(self):
        self.ui.transmittable.setColumnCount(10)
        self.ui.transmittable.setRowCount(1)
        self.ui.transmittable.setHorizontalHeaderLabels(('ID','DLC','Data1','Data2','Data3','Data4','Data5','Data6','Data7','Data8'))
        self.ui.receivetable.setColumnCount(10)
        self.ui.receivetable.setRowCount(50)
        self.ui.receivetable.setHorizontalHeaderLabels(('ID','DLC','Data1','Data2','Data3','Data4','Data5','Data6','Data7','Data8'))
    
    @pyqtSlot(list)
    def update_receivetable(self, data_to_emit):
        print("updating")
        # for row in range(self.ui.transmittable.rowCount()):    
        for col in range(self.ui.receivetable.columnCount()):
            self.ui.receivetable.setItem(0,col,QTableWidgetItem(str(data_to_emit[col])))
    
   
    def getcellvalue(self):
        self.transmit_data = []
        for col in range(self.ui.transmittable.columnCount()):
            self.item = self.ui.transmittable.item(0, col)
            if self.item is not None:
                cell_value = self.item.text() 
                self.transmit_data.append(cell_value)
            else:
                self.transmit_data.append("0")
            
                
        self.can_handler.cantxdata.emit(self.transmit_data)
        # print(self.transmit_data)
        
    def logging(self):
        if self.log_file is None:
            filename = self.filename_edit.toPlainText()
            if filename:
                self.log_file = open(filename, "w")
                logging.basicConfig(filename=filename, level=logging.INFO)
                print("Logging started to file:", filename)
            else:
                print("Please enter a filename.")
        else:
            self.log_file.close()
            self.log_file = None
            logging.shutdown()
            print("Logging stopped.")    
    
    

# class available_configs():
#     def __init__(self):
        # self.bus_send = can.Bus(interface='pcan', channel='PCAN_USBBUS1')
        # available_channels = can.interface.detect_available_configs('pcan')
#         print(available_channels)
#         for element in available_channels:
#             # for key, value in element.items():
#             if element['channel'] == 'PCAN_USBBUS1':
#                 print("Connected")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
