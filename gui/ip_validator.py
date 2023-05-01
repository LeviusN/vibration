import logging
# import json
# from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
# from wsdiscovery import QName
from scapy.all import ARP, Ether, srp

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

LOG = logging.getLogger()


class IP4ValidatorBasic(QRegExpValidator):
    validationChanged = QtCore.pyqtSignal(QtGui.QValidator.State)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRegExp(QRegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]|)\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]|)$"))
        self.parent = parent

    def validate(self, text, pos):
        result = super().validate(text, pos)
        if result[0] == self.Acceptable:
            octets = list(map(str, text.split('.')))
            if len(octets) > 4:
                self.validationChanged.emit(0)
                result = 0, text, pos
        else:
            self.validationChanged.emit(0)
            return 0, text, pos
            # result = 0, text, pos
        self.validationChanged.emit(2)
        return result


# class OnvifDiscoverer():
#     def __init__(self):
#         pass
#
#     def discover(self):
#         try:
#             wsd = WSDiscovery()
#             wsd.start()
#             services = wsd.searchServices()
#             adrs = []
#             for service in services:
#                 adrs.append(service.getXAddrs()[0])
#             wsd.stop()
#             return adrs
#         except Exception as e:
#             LOG.error(e)
#             raise

class Discoverer():
    def __init__(self):
        pass

    def discover(self):
        arp = ARP(pdst='192.168.0.249')
        ether = Ether(dst='ff:ff:ff:ff:ff:ff')
        packet = ether/arp

        # send and receive packets
        result = srp(packet, timeout=3, verbose=0)[0]

        # parse response and print IP and MAC addresses
        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        return devices
