# FailSafe


![failsafe](https://user-images.githubusercontent.com/48811414/218199963-129425ad-32b7-4017-a920-cb0604b00522.png)

## Description
The "Failsafe" script is a simple but effective way to ensure that important files are protected while also being easily accessible to those who need them. The script uses the bcrypt library to securely store a hashed password, which is prompted for whenever the script is run and the time of the last successful password entry is recorded.

If the password is not entered for a set interval of time (Default 7 Days), the script automatically uploads the files to several popular cloud storage services (such as MEGA, MediaFire, and Google Drive). The upload process uses the requests library to handle the HTTP requests, and the mimetypes library to correctly determine the content type of the files being uploaded. The script also includes error handling to ensure that the upload process continues even if one of the services experiences issues.

With its simple but secure password protection and automatic uploads, the "Failsafe" script is an ideal solution for ensuring that important files are protected in the events of something happening.
