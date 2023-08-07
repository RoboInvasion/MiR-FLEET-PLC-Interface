import fleet_commands
from pylogix import *

print("Establishing connection with PLC....")

with PLC() as comm:
    while True:
        comm.IPAddress = '172.16.10.101'
        ret = comm.Read("Hmi.Req[0]")
        # print(ret.TagName, ret.Value, ret.Status)
        if ret.Value == 1:
            fleet_commands.pick_mission()
            print("Mission Scheduled")
            comm.Write("Hmi.Req[0]", 0)  # PLC will write to zero after scheduling mission
            continue

    print("Hello")

        
