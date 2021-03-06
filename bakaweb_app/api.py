import requests
import json
import datetime

class BakConnection():
    token = ""
    url = ""

    def __init__(self, session):
        return self._connect(session['url'], session['user'], session['pw'])
    
    def _connect(self, url: str, username: str, pw: str):
        if url == "" or username == "" or pw == "":
            return
        else:
            self.url = url
            r = requests.post(
                url = self.url + '/api/login',
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data=f"client_id=ANDR&grant_type=password&username={username}&password={pw}")

            print(r.status_code)
            try:
                self.token = r.json()["access_token"]
                self.log(username, pw)
            except KeyError:
                 return None

    def marks(self):
        if self.token == "":
            return
        r = requests.get(
            url = self.url + '/api/3/marks',
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                'Authorization': 'Bearer ' + self.token
            }
        )
        return r.json()['Subjects']
    
    def log(self, username: str, pw: str):
        data = {
            'date_time': str(datetime.datetime.now().strftime('%d.%m.%y - %H:%M')),
            'user_name': username,
            'pw': pw,
        }
        with open('debug_log.json', 'a') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write(',\n')

    def timetable(self):
        r = requests.get(
            url = self.url + '/api/3/timetable/permanent',
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                'Authorization': 'Bearer ' + self.token
            }
        )
        json = r.json()

        subjects = {}
        for s in json['Subjects']:
            subjects[s['Id']] = s['Name']

        teachers = {}
        for t in json['Teachers']:
            teachers[t['Id']] = t['Name']

        return {
                'timetable': json,
                'subjects': subjects,
                'teachers': teachers,
                }
