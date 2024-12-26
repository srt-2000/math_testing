import requests
from dataclasses import dataclass

@dataclass()
class Blog:
    name: str

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()