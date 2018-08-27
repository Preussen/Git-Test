import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import serial
import minimalmodbus
import binascii
import time
import sys
import csv
from struct import unpack, pack
import array

def _checkSlaveaddress(slaveaddress):
  SLAVEADDRESS_MAX = 255
  SLAVEADDRESS_MIN = 0
  minimalmodbus._checkInt(slaveaddress, SLAVEADDRESS_MIN, SLAVEADDRESS_MAX, description='slaveaddress')