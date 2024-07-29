from sys import path
from os.path import dirname, abspath
path.append(dirname(abspath(__file__)))
from others.filesystem import create_file, use_file, create_directory, path_join, getcwd, chdir
from datetime import datetime
from tools import theharvester, cmseek

def timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Session:
    def __init__(self, Site):
        self.name = Site.domain
        self.session_dir = path_join(getcwd(), self.name)
        self.session_info_file = None
        self.session_started = False
        self.Site = Site
    
    def start(self):
        create_directory(self.session_dir)
        chdir(self.session_dir)
        log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_file_name = f"session-{log_timestamp}.txt"
        self.session_info_file = session_file_name
        with open(self.session_info_file, 'w') as file:
            file.write(f"[*] Session started at {timestamp()}\n")
        self.session_started = True
        print(f"[*] Session started for {self.name}")

    def write(self, text):
        if not self.session_started:
            raise Exception("Session has not been started.")
        try:
            with open(self.session_info_file, 'a') as file:
                file.write(f"{text}\n")
            print("[*] Updated session log.")
        except Exception as e:
            print("[!] Failed to update session log.")

    def end(self):
        if not self.session_started:
            raise Exception("Session has not been started.")
        with open(self.session_info_file, 'a') as file:
            file.write(f"[*] Session ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.session_started = False
        print(f"[*] Session ended for {self.name}")

# Example usage:
if __name__ == "__main__":
    from variables.Site import SiteInfo
    Site = SiteInfo()
    Site.set_info("https://www.dypiu.ac.in/")
    session = Session(Site=Site)
    session.start()
    cmseek.light_scan(session=session)
    session.end()