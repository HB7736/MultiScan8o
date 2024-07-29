from sys import path
from os.path import dirname, abspath, join as path_join, exists
path.append(dirname(dirname(abspath(__file__))))
from window import terminal
from variables import Config


def show_banner():
    terminal.execute_command(command=banner,
                            width=63,
                            height=28, fontsize="mini")

def full_scan(session):
    if session:
        print(f"[*] WPScan: Starting Full Scan ({session.name})")
        try:
            token = Config.get_token("WPScan")
            session.write(f"[*] WPScan: Starting Full Scan ({session.name})")
            command = f'''
wpscan --banner --version ;
echo "[*] WPScan: Performing Scan For {session.Site.protocol}://{session.Site.site}" ;
echo "[*] WPScan: Output Format is JSON, will be saved as WPScan.json"
echo "{'[*] WPScan: Using API token '+token if token else '[!] WPScan: API Token not set, vulnerability scan not available! to set token, use --wpscan-token <token>'}"
echo "{'[*] WPScan: Performing full vulnerablity scan' if token else '[!] WPScan: Performing Partial Scan (Backups & Plugins Discovery, Users Enumeration and bruteforce)'}"
echo "[*] WPScan: This scan will run in background, and show results when completed"
touch WPScan.json
wpscan --url {session.Site.protocol}://{session.Site.site} -e u1-100 --password-attack wp-login -P {path_join(dirname(dirname(abspath(__file__))),'wordlists/common-india-100.txt')} -f json --rua -o WPScan.json ;
cat WPScan.json ;
'''
            terminal.execute_command(command=command,width=78,height=28,fontsize="mini")
            print(f"[*] WPScan: Finished Full Scan ({session.name})")
            session.write(f"[*] WPScan: Finished Full Scan ({session.name})")
        except Exception as e:
            print("[!] WPScan: Exception Occured while performing full scan:",str(e))
            session.write(f"[!] WPScan: Failed to Complete Full Scan ({session.name})")

banner = r'''
#!/bin/bash
wpscan --banner --version
exit 0
'''

if __name__=="__main__":
    show_banner()