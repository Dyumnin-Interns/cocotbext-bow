import cocotb
from cocotb_bus.drivers import BusDriver
from cocotb.triggers import RisingEdge, FallingEdge, ReadOnly, Timer, ReadWrite, Lock


class BOWTxDriver(BusDriver):
    _signals = ['d', 'fec', 'aux', 'clk']
    _optional_signals = ['clk_']

    def __init__(self, dut, prefix, cfg):
        pass

    def write(address, data):
        '''
        usage
        bow.write(0x01234,b'hello world')
        '''
        pass

    def read(address, length):
        pass


class BOWConfig():
    def __init__(self):
        pass
