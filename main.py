import fleet_commands
from pylogix import *

print("Establishing connection with PLC....")

with PLC() as comm:
    while True:
        comm.IPAddress = <ip address of PLC>
        ret = comm.Read(<PLC Tag>)
        # print(ret.TagName, ret.Value, ret.Status)
        if ret.Value == 1:
            fleet_commands.pick_mission()
            print("Mission Scheduled")
            comm.Write(<PLC Tag>, 0)  
            continue
            

        
