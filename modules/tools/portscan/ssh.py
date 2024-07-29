from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException, SSHException
import socket

class SSHchecker:
    def __init__(self, host, port=22, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.default_credentials = [
            ("admin", "admin"),
            ("admin", "password"),
            ("root", "root"),
            ("root", "admin"),
            ("user", "user"),
            ("test", "test"),
            ("guest", "guest")
        ]

    def connect(self):
        try:
            self.client.connect(self.host, port=self.port, timeout=self.timeout)
            print(f"Connected to {self.host}:{self.port}")
            return True
        except (socket.error, socket.gaierror) as e:
            print(f"Failed to connect to {self.host}:{self.port} - {e}")
            return False
        except Exception as e:
            print("Exception Occured while connecting FTP:",str(e))

    def check_default_credentials(self):
        results = []
        for username, password in self.default_credentials:
            try:
                self.client.connect(self.host, port=self.port, username=username, password=password, timeout=self.timeout)
                print(f"Login successful with default credentials: {username}/{password}")
                results.append(f"{username}:{password}")
            except AuthenticationException:
                print(f"Login failed with default credentials: {username}/{password}")
            except SSHException as e:
                print(f"SSH error with credentials {username}/{password} - {e}")
            except Exception as e:
                print(f"Error with credentials {username}/{password} - {e}")
        return results

    def check_weak_encryption(self):
        try:
            transport = self.client.get_transport()
            if transport is None:
                print("Failed to get transport")
                return False
            weak_algorithms = [
                'arcfour', 'arcfour128', 'arcfour256',
                'aes128-cbc', '3des-cbc', 'blowfish-cbc'
            ]
            server_algorithms = transport.get_security_options().ciphers
            for algo in weak_algorithms:
                if algo in server_algorithms:
                    print(f"Weak encryption algorithm supported: {algo}")
                    return True
            print("No weak encryption algorithms supported")
            return False
        except SSHException as e:
            print(f"SSH error during encryption check - {e}")
            return False

    def close(self):
        self.client.close()

def check_all(host,port):
    results = {}
    try:
        ssh = SSHchecker(host=host,port=port)
        if ssh.connect():
            default_creds = ssh.check_default_credentials()
            if default_creds:
                results["default_credentials"] = "supported"
                results["credentials"] = default_creds
        else:
            results["Error"] = "Failed to Connect SSH port"
    except Exception as e:
        print("Exception:",str(e))
    finally:
        ssh.close()
    return results

# Usage
if __name__ == "__main__":
    host = "ssh.example.com"  # Replace with the target SSH server
    checker = SSHchecker(host)

    if checker.connect():
        checker.check_default_credentials()
        checker.check_weak_encryption()
        checker.close()
