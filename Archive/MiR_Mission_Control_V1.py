import requests, json

ip = '172.16.1.173'
host = 'http://' + ip + '/api/v2.0.0/'

headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic RGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=='

def getMissions():
    get_missions = requests.get(host + 'missions', headers = headers)
    print(get_missions.text)

def postMission():
    mission_id = {"mission_id": "f052f827-b868-11ed-b178-000129ad3d43"}
    post_mission = requests.post(host + 'mission_queue', json = mission_id, headers = headers)
    print(post_mission)
    print(post_mission.status_code)
