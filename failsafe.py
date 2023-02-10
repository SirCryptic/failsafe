import time
import bcrypt
import mimetypes
import requests
import ssl

# Developer: SirCryptic (NullSecurityTeam)
# Info: failsafe [BETA]
# 15DB1A86C9C57A5153DA1E215FEF5C6414F3BF546E386C028D28012111FFD593
# Fuck The System Before It Fucks You!

hashed_password = bcrypt.hashpw("secret".encode(), bcrypt.gensalt()) # replace `secret` with your hashed bcrypt password
interval = 7 # Number of days between password prompts
last_access = time.time() # Record the time of the last successful password entry

services = {
    "mega": {"url": "https://mega.nz/login", "username": "user", "password": "pass"},
    "mediafire": {"url": "https://www.mediafire.com/login", "username": "user", "password": "pass"},
    "googledrive": {"url": "https://drive.google.com/", "username": "user", "password": "pass"}
    # Add more cloud storage services here
}
files = [
    "file1.jpg",  # Change this to the path of your file
    "file2.pdf",  # Change this to the path of your file
    "file3.txt",  # Change this to the path of your file
    "file4.mp3",  # Change this to the path of your file
    "file5.mp4",  # Change this to the path of your file
    "file6.docx", # Change this to the path of your file
    # Add more files here, i think you get the gist.
]
while True:
    user_input = input("Enter password: ")
    if bcrypt.checkpw(user_input.encode(), hashed_password):
        print("Access granted")
        last_access = time.time() # Update the time of the last successful password entry
    else:
        print("Access denied")
    if time.time() - last_access > interval * 24 * 60 * 60: # If The user dont input the password then files will be published slowly over the interval
        for service in services.values():
            try:
                session = requests.Session()
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"} # Feel free to change the user-agent to what you wish
                data = {"username": service["username"], "password": service["password"]}
                session.post(service["url"], data=data, headers=headers, verify=True)
                for file in files:
                    with open(file, "rb") as f:
                        content_type, encoding = mimetypes.guess_type(file)
                        files = {"file": (file, f, content_type)}
                        response = session.post(f"{service['url']}/upload", files=files, headers=headers, verify=True)
                        if response.status_code == 200:
                            print(f"Uploaded {file} to {service['url']}")
                        else:
                            print(f"Failed to upload {file} to {service['url']}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to upload files: {e}")
        last_access = time.time()
    time.sleep(60) # Wait for a minute before checking the password again
