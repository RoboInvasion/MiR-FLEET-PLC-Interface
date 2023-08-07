import requests
import json

ip = <IP Address of FLEET Server>
host = 'http://' + ip + '/api/v2.0.0/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic RGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='}


def get_missions():
    get_missions_local = requests.get(host + 'missions', headers=headers)
    print(get_missions_local.text)


def pick_mission():
    payload = {"mission_id": <guid>, "robot_id": 0,
               "priority": 0,
               "high_priority": True}

    post_mission = requests.post(host + 'mission_scheduler', json=payload, headers=headers)
    print(post_mission)
    print(post_mission.status_code)


def place_mission():
    payload = {"mission_id": <guid>, "robot_id": 0,
               "priority": 0,
               "high_priority": True}

    post_mission = requests.post(host + 'mission_scheduler', json=payload, headers=headers)
    print(post_mission)
    print(post_mission.status_code)


if __name__ == "__main__":
    get_missions()
