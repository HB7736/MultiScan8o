from json import load, JSONDecodeError
from sys import path
from os.path import dirname, abspath, join as path_join, exists
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

sources=["anubis",
        "bevigil",
        "binaryedge",
        "bing",
        "bingapi",
        "bufferoverun",
        "censys",
        "certspotter",
        "criminalip",
        "crtsh",
        "dnsdumpster",
        "duckduckgo",
        "fullhunt",
        "github-code",
        "hackertarget",
        "hunter",
        "hunterhow",
        "intelx",
        "netlas",
        "onyphe",
        "otx",
        "pentesttools",
        "projectdiscovery",
        "rapiddns",
        "rocketreach",
        "securityTrails",
        "sitedossier",
        "subdomaincenter",
        "subdomainfinderc99",
        "threatminer",
        "tomba",
        "urlscan",
        "virustotal",
        "yahoo",
        "zoomeye"
        ]


def show_banner():
    terminal.execute_command(command=banner,
                            width=80,
                            height=28, fontsize="mini")

def domain_full_scan(session):
    if session:
        print(f"[*] theHarvester: Starting Full Scan ({session.name})")
        try:
            session.write(f"[*] theHarvester: Starting Full Scan ({session.name})")
            logfile_name = path_join(session.session_dir, f'theHarvester-fullscan_({session.name})')+".txt"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f"theHarvester -d {session.Site.domain} -b {','.join(sources)} -f theHarvester"
            terminal.execute_command(command=command,width=80,height=28,fontsize="mini", output_file=logfile_name)
            print(f"[*] theHarvester: Finished Full Scan ({session.name})")
            session.write(f"[*] theHarvester: Finished Full Scan ({session.name})")
            print("[*] theHarvester: Analysing Results of Full Scan")
            session.write("[*] theHarvester: Analysing Results of Full Scan")
            analyse_results(session=session)
        except Exception as e:
            print("[!] theHarvester: Exception Occured while performing full scan:",str(e))
            session.write(f"[!] theHarvester: Failed to Complete Full Scan ({session.name})")

def analyse_results(session):
    try:
        json_file_path = path_join(session.session_dir, "theHarvester.json")
        if not exists(json_file_path):
            print("[!] theHarvester: Can't find Results file (theHarvester.json)")
            session.write("[!] theHarvester: Can't find Results file (theHarvester.json)")
            return False
        with open(json_file_path, 'r') as file:
            results = load(file)
        # Add emails
        session.Site.tech.add_email(results.get('emails', []))
        # Add subdomains
        session.Site.tech.add_domains(results.get('hosts', []))
        # Add IP addresses
        session.Site.tech.add_ip_address(results.get('ips', []))
        return True
    except JSONDecodeError:
        print("[!] theHarvester: Failed to Analyse Results file (theHarvester.json)")
        session.write("[!] theHarvester: Failed to Analyse Results file (theHarvester.json)")
        return False
    except Exception as e:
        print(f"[!] theHarvester: Exception occured while analysing results:",str(e))
        return False

banner = r'''
#!/bin/bash
theHarvester
exit 0
'''

if __name__=="__main__":
    show_banner()