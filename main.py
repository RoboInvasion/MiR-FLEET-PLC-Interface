"""
Main program that reads a PLC tag and schedules a specific mission on the MiR FLEET. 
We are using (2) PLC tags to call initialize and acknowledge the request.

"""


import fleet_commands
from pylogix import *

print("Establishing connection with PLC....")

with PLC() as comm:
    while True:
        comm.IPAddress = '<PLC IP Adress>'
        pallet_ready = comm.Read("Hmi.Req[0]")
        robot_accept = comm.Read("Hmi.Req[1]")

        if pallet_ready.Value == 1 and robot_accept.Value == 0:
            fleet_commands.pick_mission()
            print("Mission Scheduled")
            comm.Write("Hmi.Req[1]", 1)
            continue
            

        
