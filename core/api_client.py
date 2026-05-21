import requests
class APIClient:
    def __init__(self, baseurl):
        self.base_url = baseurl        
    
    def get(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}")
        return response
