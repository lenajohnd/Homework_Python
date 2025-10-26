import requests


class YougileAPI:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Beaver {api_key}',
            'Content-Type': 'application/json'
        }

    def create_project(self, title: str, users: dict = None):
        response = requests.post(
            url=f"{self.base_url}/api-v2/projects",
            json={"title": title, "users": users or {}},
            headers=self.headers
        )
        return {
            "status_code": response.status_code,
            "response": response.json()
        }

    def get_project(self, project_id: str):
        response = requests.get(
            url=f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )
        return {
            "status_code": response.status_code,
            "response": response.json()
        }

    def update_project(self, project_id: str, title: str, users: dict = None):
        payload = {'title': title}
        if users:
            payload["users"] = users
        response = requests.put(
            url=f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
        return {
            "status_code": response.status_code,
            "response": response.json()
        }
