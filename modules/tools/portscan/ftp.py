from ftplib import FTP, error_perm
import socket

class FTPchecker:
    def __init__(self, host, port=21, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.default_credentials = [
            ("admin", "admin"),
            ("admin", "password"),
            ("root", "root"),
            ("root", "admin"),
            ("user", "user"),
            ("anonymous", "anonymous"),
            ("anonymous", ""),
            ("ftp", "ftp"),
            ("test", "test"),
            ("guest", "guest")
        ]
        self.ftp = FTP()

    def connect(self):
        try:
            self.ftp.connect(self.host, self.port, self.timeout)
            print(f"Connected to {self.host}:{self.port}")
            return True
        except (socket.error, socket.gaierror):
            print(f"Failed to connect to {self.host}:{self.port}")
            return False

    def check_anonymous_login(self):
        try:
            self.ftp.login()
            print("Anonymous login allowed")
            return True
        except error_perm:
            print("Anonymous login not allowed")
            return False

    def check_default_credentials(self):
        for username, password in self.default_credentials:
            results = []
            try:
                self.ftp.login(username, password)
                print(f"Login successful with credentials: {username}/{password}")
                results.append(f"{username}:{password}")
            except error_perm:
                print(f"Login failed with credentials: {username}/{password}")
            except:
                print(f"Timeout with credentials: {username}/{password}")
        return results

    def check_ftp_bounce(self):
        try:
            self.ftp.sendcmd('PORT 127,0,0,1,0,21')
            print("FTP Bounce attack possible")
            return True
        except error_perm:
            print("FTP Bounce attack not possible")
            return False

    def check_plain_text_auth(self):
        # In this basic check, we will see if we can log in and if so, the server supports plain text authentication
        try:
            self.ftp.login('test', 'test')
            print("Server supports plain text authentication (logged in with plain text credentials)")
            return True
        except error_perm:
            print("Server does not support plain text authentication with provided credentials")
            return False

    def close(self):
        self.ftp.quit()


def check_all(host,port):
    results = {}
    try:
        ftp = FTPchecker(host=host,port=port)
        if ftp.connect():
            if ftp.check_anonymous_login():
                results["anonymous_login"] = "supported"
            # default_creds = ftp.check_default_credentials()
            # if default_creds:
            #     results["default_credentials"] = "supported"
            #     results["credentials"] = default_creds
            if ftp.check_ftp_bounce():
                results["ftp_bounce"] = "supported"
            if ftp.check_plain_text_auth():
                results["plain_auth"] = "supported"
        else:
            results["Error"] = "Failed to Connect FTP port"
    except:
        ftp.close()
    return results

# Usage
if __name__ == "__main__":
    host = "ftp.example.com"  # Replace with the target FTP server
    checker = FTPchecker(host)

    if checker.connect():
        checker.check_anonymous_login()
        checker.check_default_credentials()
        checker.check_ftp_bounce()
        checker.check_plain_text_auth()
        checker.close()
