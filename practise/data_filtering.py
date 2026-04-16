# Imagine you scraped a list of user IDs from a web page, but some of the data came back corrupted with None values or empty strings.

user_ids = ["user_001", None, "user_002", "", "user_003", "   "]
user_list = []
for user in user_ids:
    if user:
        if user.strip() != "":
            user_list.append(user)
print(user_list)

# user_list = [user for user in user_ids if user and user.strip()]
