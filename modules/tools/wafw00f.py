from json import load, JSONDecodeError
from sys import path
from os.path import dirname, abspath, join as path_join, exists
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def show_banner():
    terminal.execute_command(command=banner,
                            width=68,
                            height=26, fontsize="mini")

def detect_firewall(session):
    if session:
        print(f"[*] WAFW00F: Starting Firewall Detection ({session.name})")
        try:
            session.write(f"[*] WAFW00F: Starting Firewall Detection ({session.name})")
            command = f"wafw00f {session.Site.domain} -f json -o WAFW00F.json"
            terminal.execute_command(command=command,width=68,height=26,fontsize="mini")
            print(f"[*] WAFW00F: Finished Firewall Detection ({session.name})")
            session.write(f"[*] WAFW00F: Finished Firewall Detection ({session.name})")
            analyse_results(session=session)
        except Exception as e:
            print("[!] WAFW00F: Exception Occured while performing firewall detection:",str(e))
            session.write(f"[!] WAFW00F: Failed to Complete Firewall Detection ({session.name})")

def analyse_results(session):
    try:
        json_file_path = path_join(session.session_dir, "WAFW00F.json")
        if not exists(json_file_path):
            print("[!] WAFW00F: Can't find Results file (WAFW00F.json)")
            session.write("[!] WAFW00F: Can't find Results file (WAFW00F.json)")
            return False
        with open(json_file_path, 'r') as file:
            results = load(file)
        
        # Set Firewall Info
        firewall = results[0].get('firewall', "") if results else ""
        session.Site.tech.set_Firewall(firewall if firewall!="None" else "")
        return True
    except JSONDecodeError:
        print("[!] WAFW00F: Failed to Analyse Results file (WAFW00F.json)")
        session.write("[!] WAFW00F: Failed to Analyse Results file (WAFW00F.json)")
        return False
    except Exception as e:
        print(f"[!] WAFW00F: Exception occured while analysing results:",str(e))
        return False

banner = r'''
#!/bin/bash
wafw00f -V
exit 0
'''

if __name__=="__main__":
    show_banner()