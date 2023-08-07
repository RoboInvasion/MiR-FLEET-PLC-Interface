"""
Main program that reads a PLC tag and schedules a specified mission on the MiR FLEET.

"""


import fleet_commands
from pylogix import *

print("Establishing connection with PLC....")

with PLC() as comm:
    while True:
        comm.IPAddress = <ip address of PLC>
        ret = comm.Read(Hmi.Req[0])
        # print(ret.TagName, ret.Value, ret.Status)
        if ret.Value == 1:
            fleet_commands.pick_mission()
            print("Mission Scheduled")
            comm.Write(Hmi.Req[0], 0)  
            continue
            

        
