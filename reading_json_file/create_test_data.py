import json
import os

roles = ["admin", "user", "blocked"]
users = []

for i in range(1,51):
    user = {
    #"email": f"user{i}@test.com",
    "email": f"{roles[i%3]}@test.com",
    "password":f"pass{i}",
    "role":roles[i%3]
}
    users.append(user)

os.makedirs("test_data", exist_ok=True)

with open ("test_data/users.json", "w") as f:
    json.dump(users, f, indent=2)


