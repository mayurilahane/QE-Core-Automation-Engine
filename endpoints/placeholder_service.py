from core.api_client import APIClient

class PlaceholderService:
    def __init__(self):
        self.api = APIClient("https://jsonplaceholder.typicode.com")

    def get_user(self, user_id):
        res = self.api.get(f"/users/{user_id}")
        return res

        
