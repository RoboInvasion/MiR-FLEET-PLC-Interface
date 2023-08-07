import fleet_commands
from pylogix import *

print("Establishing connection with PLC....")

with PLC() as comm:
    while True:
        comm.IPAddress = '172.16.10.101'
        pallet_ready = comm.Read("Hmi.Req[0]")
        robot_accept = comm.Read("Hmi.Req[1]")

        if pallet_ready.Value == 1 and robot_accept.Value == 0:
            fleet_commands.pick_mission()
            print("Mission Scheduled")
            comm.Write("Hmi.Req[1]", 1)
            continue




        

