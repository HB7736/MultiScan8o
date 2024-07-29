from sys import path
from os.path import dirname, abspath, join as path_join
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def show_banner():
    terminal.execute_command(command=banner,
                            width=68,
                            height=26, fontsize="mini")

def enumerate(session):
    if session:
        print(f"[*] JoomScan: Starting Enumeration ({session.name})")
        try:
            session.write(f"[*] JoomScan: Starting Enumeration ({session.name})")
            logfile_name = path_join(session.session_dir, f'JoomScan-enumeration_({session.name})')+".txt"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f"joomscan --url {session.Site.protocol}://{session.Site.site} --random-agent -ec"
            terminal.execute_command(command=command,width=68,height=26,fontsize="mini", output_file=logfile_name)
            print(f"[*] JoomScan: Finished Enumeration ({session.name})")
            session.write(f"[*] JoomScan: Finished Enumeration ({session.name})")
        except Exception as e:
            print("[!] JoomScan: Exception Occured while performing enumeration:",str(e))
            session.write(f"[!] JoomScan: Failed to Complete Enumeration ({session.name})")

banner = r'''
#!/bin/bash
joomscan --version
exit 0
'''

if __name__=="__main__":
    show_banner()