import requests

def get_token(url: str, username: str, pw: str):
    r = requests.post(
        url=url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=f"client_id=ANDR&grant_type=password&username={username}&password={pw}")

    print(r.status_code)
    return r.json()["access_token"]

def znamky(url: str, token: str):
    r = requests.get(
        url=url,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            'Authorization': 'Bearer ' + token
        }
    )

    return r.json()['Subjects']