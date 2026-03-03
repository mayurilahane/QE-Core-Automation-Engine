'''
Task 3: The Test Data Grouper (List of Dictionaries)
The Scenario: You have a massive list of test results from your overnight Playwright execution. You want to group them by status so you can easily count the failures.
The Prompt: Write a function that takes a list of test result dictionaries and returns a new dictionary where the keys are the "status" and the values are a list of the "test_names".

Your Starting Data:

Python
test_results = [
    {"test_name": "test_login", "status": "passed"},
    {"test_name": "test_payment", "status": "failed"},
    {"test_name": "test_logout", "status": "passed"},
    {"test_name": "test_rbac_admin", "status": "failed"}
]

# Expected Output: 
# {
#   "passed": ["test_login", "test_logout"],
#   "failed": ["test_payment", "test_rbac_admin"]
# }

'''

test_results = [
    {"test_name": "test_login", "status": "passed"},
    {"test_name": "test_payment", "status": "failed"},
    {"test_name": "test_logout", "status": "passed"},
    {"test_name": "test_rbac_admin", "status": "failed"}
]

