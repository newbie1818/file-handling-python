import os
# Avatar Upload Simulation
# Context: the project has a user avatar upload feature.
# After the upload, the test verifies that the file was saved correctly.

UPLOADS_DIR = "uploads"
def simulate_upload(username, filename, content):
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    folder = os.path.join(UPLOADS_DIR, username)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    with open (path, "w") as f:
        f.write(content)

def verify_upload(username, filename):
    path = os.path.join(UPLOADS_DIR, username, filename)

    if not os.path.exists(path):
        print("Error: folder does not exist")
        return False

    if not os.path.getsize(path):
        print("Error: File is empty")
        return False

    if not filename.endswith(".png") and not filename.endswith(".jpg"):
        print("Error: file must be .png or .jpg")
        return False

    return True
simulate_upload("newbie", "avatar.png", "fake image content")
result = verify_upload(username="newbie", filename="avatar.png")
print(result)