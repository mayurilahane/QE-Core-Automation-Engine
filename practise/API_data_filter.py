'''
Task: The API Data Filter
You have just made a GET request to a /users endpoint, and the response gives you a list of user dictionaries.

Your goal is to write a Python function that takes this list and returns a new list containing only the names of the users whose status is "active".

Here is your starting data:

Python
users_response = [
    {"name": "Alice", "status": "active"},
    {"name": "Bob", "status": "inactive"},
    {"name": "Charlie", "status": "active"},
    {"name": "Diana", "status": "pending"}
]

The expected output should be: ['Alice', 'Charlie']
'''

users_response = [
    {"name": "Alice", "status": "active"},
    {"name": "Bob", "status": "inactive"},
    {"name": "Charlie", "status": "active"},
    {"name": "Diana", "status": "pending"}
]

def api_data_filter(users_response):
    active_users = []
    for user in users_response:
        if user["status"] == "active":
            active_users.append(user["name"])    
    return active_users



if __name__ == "__main__":
    api_data = api_data_filter(users_response)
    print(api_data)