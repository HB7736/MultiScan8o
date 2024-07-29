from sys import path
from os.path import dirname, abspath, join as path_join
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def show_banner():
    terminal.execute_command(command=banner,
                            width=50,
                            height=15, fontsize="mini")

def subdomain_discovery(session):
    if session:
        print(f"[*] FFUF: Starting Subdomain Discovery ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Subdomain Discovery ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-subdomaindiscovery_({session.name})')+ ".csv"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f"ffuf -u '{session.Site.protocol}://FUZZ.{session.Site.site}' -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -ic -of csv -o '{logfile_name}' -t 20"
            terminal.execute_command(command=command,width=102,height=26,fontsize="mini")
            print(f"[*] FFUF: Finished Subdomain Discovery ({session.name})")
            session.write(f"[*] FFUF: Finished Subdomain Discovery ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occured while performing subdomain discovery:",str(e))
            session.write(f"[!] FFUF: Failed to Complete Subdomain Discovery ({session.name})")

def webcontent_discovery(session):
    if session:
        print(f"[*] FFUF: Starting Web Content Discovery ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Web Content Discovery ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_discovery_({session.name})')+ ".csv"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/common.txt -ignore-body -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command,width=102,height=26,fontsize="mini")
            print(f"[*] FFUF: Finished Web Content Discovery ({session.name})")
            session.write(f"[*] FFUF: Finished Web Content Discovery ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occured while performing web content discovery:",str(e))
            session.write(f"[!] FFUF: Failed to Complete Web Content Discovery ({session.name})")

def webcontent_wordpress_scan(session):
    if session:
        print(f"[*] FFUF: Starting Wordpress Scan ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Wordpress Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_wordpress_scan_({session.name})')+ ".csv"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/WebTechnologyPaths-Trickest-Wordlists/wordpress-all-levels.txt -ignore-body -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command,width=102,height=26,fontsize="mini")
            print(f"[*] FFUF: Finished Wordpress Scan ({session.name})")
            session.write(f"[*] FFUF: Finished Wordpress Scan ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occured while performing wordpress scan:",str(e))
            session.write(f"[!] FFUF: Failed to Complete Wordpress Scan ({session.name})")

def webcontent_joomla_scan(session):
    if session:
        print(f"[*] FFUF: Starting Joomla Scan ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Joomla Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_joomla_scan_({session.name})') + ".csv"
            logfile_name = logfile_name.replace("'", r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/WebTechnologyPaths-Trickest-Wordlists/joomla-all-levels.txt -ignore-body -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command, width=102, height=26, fontsize="mini")
            print(f"[*] FFUF: Finished Joomla Scan ({session.name})")
            session.write(f"[*] FFUF: Finished Joomla Scan ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occurred while performing joomla scan:", str(e))
            session.write(f"[!] FFUF: Failed to Complete Joomla Scan ({session.name})")

def webcontent_drupal_scan(session):
    if session:
        print(f"[*] FFUF: Starting Drupal Scan ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Drupal Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_drupal_scan_({session.name})') + ".csv"
            logfile_name = logfile_name.replace("'", r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/CMS/Drupal.txt -ignore-body -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command, width=102, height=26, fontsize="mini")
            print(f"[*] FFUF: Finished Drupal Scan ({session.name})")
            session.write(f"[*] FFUF: Finished Drupal Scan ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occurred while performing drupal scan:", str(e))
            session.write(f"[!] FFUF: Failed to Complete Drupal Scan ({session.name})")

def webcontent_magento_scan(session):
    if session:
        print(f"[*] FFUF: Starting Magento Scan ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Magento Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_magento_scan_({session.name})') + ".csv"
            logfile_name = logfile_name.replace("'", r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/WebTechnologyPaths-Trickest-Wordlists/magento.txt -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command, width=102, height=26, fontsize="mini")
            print(f"[*] FFUF: Finished Magento Scan ({session.name})")
            session.write(f"[*] FFUF: Finished Magento Scan ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occurred while performing magento scan:", str(e))
            session.write(f"[!] FFUF: Failed to Complete Magento Scan ({session.name})")

def webcontent_ghost_scan(session):
    if session:
        print(f"[*] FFUF: Starting Ghost Scan ({session.name})")
        try:
            session.write(f"[*] FFUF: Starting Ghost Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'FFUF-webcontent_ghost_scan_({session.name})') + ".csv"
            logfile_name = logfile_name.replace("'", r"\'")
            command = f"ffuf -u '{session.Site.protocol}://{session.Site.site}/FUZZ' -w /usr/share/seclists/Discovery/Web-Content/WebTechnologyPaths-Trickest-Wordlists/ghost-all-levels.txt -ic -of csv -o '{logfile_name}' -t 100"
            terminal.execute_command(command=command, width=102, height=26, fontsize="mini")
            print(f"[*] FFUF: Finished Ghost Scan ({session.name})")
            session.write(f"[*] FFUF: Finished Ghost Scan ({session.name})")
        except Exception as e:
            print("[!] FFUF: Exception Occurred while performing ghost scan:", str(e))
            session.write(f"[!] FFUF: Failed to Complete Ghost Scan ({session.name})")

banner = r'''
#!/bin/bash
a1="

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

________________________________________________
"
echo -n "$a1"
ffuf -V
exit 0
'''

if __name__=="__main__":
    show_banner()