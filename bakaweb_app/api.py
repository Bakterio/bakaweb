import requests

class BakConnection():
    token = ""
    url = ""

    def __init__(self, str: token):
        token = self.token
    
    def __init__(self, url: str, username: str, pw: str):
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