from pylogix import *

with PLC() as comm:
    while True:
        comm.IPAddress = '172.16.10.101'
        comm.ProcessorSlot = 0
        ret = comm.Read("Sys.AlwaysOn")
        print(ret.TagName, ret.Value, ret.Status)
   