from json import load, JSONDecodeError
from sys import path
from os.path import dirname, abspath, join as path_join, exists
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def show_banner():
    terminal.execute_command(command=banner,
                            width=70,
                            height=28, fontsize="mini")

def deep_scan(session):
    if session:
        print(f"[*] CMSeeK: Starting Deep Scan ({session.name})")
        try:
            session.write(f"[*] CMSeeK: Starting Deep Scan ({session.name})")
            command = f"""
cmseek -u {session.Site.site} -v --random-agent --follow-redirect;
rm {session.session_dir}/reports.json;
mv {session.session_dir}/Result/{session.Site.domain}/cms.json {session.session_dir}/CMSeeK.json ;
rm -rf {session.session_dir}/Result;
"""
            terminal.execute_command(command=command,width=70,height=28,fontsize="mini")
            print(f"[*] CMSeeK: Finished Deep Scan ({session.name})")
            session.write(f"[*] CMSeeK: Finished Deep Scan ({session.name})")
            analyse_results(session=session)
        except Exception as e:
            print("[!] CMSeeK: Exception Occured while performing deep scan:",str(e))
            session.write(f"[!] CMSeeK: Failed to Complete Deep Scan ({session.name})")

def light_scan(session):
    if session:
        print(f"[*] CMSeeK: Starting Light Scan ({session.name})")
        try:
            session.write(f"[*] CMSeeK: Starting Light Scan ({session.name})")
            command = f"""
cmseek -u {session.Site.site} -v --random-agent --light-scan --follow-redirect;
rm {session.session_dir}/reports.json;
mv {session.session_dir}/Result/{session.Site.domain}/cms.json {session.session_dir}/CMSeeK.json ;
rm -rf {session.session_dir}/Result;
"""
            terminal.execute_command(command=command,width=70,height=28,fontsize="mini")
            print(f"[*] CMSeeK: Finished Light Scan ({session.name})")
            session.write(f"[*] CMSeeK: Finished Light Scan ({session.name})")
            analyse_results(session=session)
        except Exception as e:
            print("[!] CMSeeK: Exception Occured while performing light scan:",str(e))
            session.write(f"[!] CMSeeK: Failed to Complete Light Scan ({session.name})")

def analyse_results(session):
    try:
        json_file_path = path_join(session.session_dir, "CMSeeK.json")
        if not exists(json_file_path):
            print("[!] CMSeeK: Can't find Results file (CMSeeK.json)")
            session.write("[!] CMSeeK: Can't find Results file (CMSeeK.json)")
            return False
        with open(json_file_path, 'r') as file:
            results = load(file)
        # Set CMS Name
        keys = results.keys()
        # if "cms_name" in keys:
        session.Site.tech.set_CMS(results.get('cms_name',""))
        # else:
        #     session.Site.tech.set_CMS("")
        # Set CMS Version
        cms_v = [key for key in keys if len(key.split("_"))==2 and key.endswith("_version")]
        if cms_v:
            session.Site.tech.set_CMS_version(results.get(cms_v[0]))
        # Set CMS Users
        cms_u = [key for key in keys if key.endswith("_users")]
        if cms_u:
            session.Site.tech.add_CMS_user(results.get(cms_u[0]))
        # # Add subdomains
        # session.Site.tech.add_domains(results.get('hosts', []))
        # # Add IP addresses
        # session.Site.tech.add_ip_address(results.get('ips', []))
        return True
    except JSONDecodeError:
        print("[!] CMSeeK: Failed to Analyse Results file (CMSeeK.json)")
        session.write("[!] CMSeeK: Failed to Analyse Results file (CMSeeK.json)")
        return False
    except Exception as e:
        print(f"[!] CMSeeK: Exception occured while analysing results:",str(e))
        return False

banner = r'''
#!/bin/bash
a1="
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA
"
echo -n "$a1"
cmseek --version
exit 0
'''

if __name__=="__main__":
    show_banner()