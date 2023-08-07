import requests
import json

ip = '172.16.1.142'
host = 'http://' + ip + '/api/v2.0.0/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic RGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}


def get_missions():
    get_missions_local = requests.get(host + 'missions', headers=headers)
    print(get_missions_local.text)


def pick_mission():
    payload = {"mission_id": "64b7faba-263e-11ee-a80f-000129ad3d43", "robot_id": 0,
               "priority": 0,
               "high_priority": True}

    post_mission = requests.post(host + 'mission_scheduler', json=payload, headers=headers)
    print(post_mission)
    print(post_mission.status_code)


# "earliest_start_time": "2023-07-31T16:06:00.175Z",

def place_mission():
    payload = {"mission_id": "f052f827-b868-11ed-b178-000129ad3d43", "robot_id": 0,
               "priority": 0,
               "high_priority": True}

    post_mission = requests.post(host + 'mission_scheduler', json=payload, headers=headers)
    print(post_mission)
    print(post_mission.status_code)


if __name__ == "__main__":
    get_missions()
