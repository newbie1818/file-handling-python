import os
import json


with open ("test_data/users.json", "r") as f:
    content = json.load(f)
    print(content)

    for item in content:
        if item["role"] == "admin" or item["role"]== "user":
            print(f'User:{item["email"]}, Role:{item["role"]}, Login Attempt:OK')
        elif item["role"] == "blocked":
            print(f'User:{item["email"]}, Role:{item["role"]}, Login Attempt:Skipped')




