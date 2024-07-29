from xmltodict import parse as xml_parse
from json import dumps, loads, JSONDecodeError
from sys import path
from os.path import dirname, abspath, join as path_join, exists
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def show_banner():
    terminal.execute_command(command=banner,
                            width=82,
                            height=28, fontsize="mini")

def scan_top1000_ports(session):
    if session:
        print(f"[*] NMap: Starting Scan for Top 1000 Ports ({session.name})")
        try:
            session.write(f"[*] NMap: Starting Scan for Top 1000 Ports ({session.name})")
            logfile_name = path_join(session.session_dir, f'NMap-top1000_ports_scan_({session.name})')+".txt"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f'''{banner}
sleep 2 ;
clear ;
nmap --top-ports 1000 -sC -Pn -sV -v {session.Site.domain} -T5 -oX NMap.xml ;
'''
            terminal.execute_command(command=command,width=82,height=28,fontsize="mini", output_file=logfile_name)
            print(f"[*] NMap: Finished Scan for Top 1000 Ports ({session.name})")
            session.write(f"[*] NMap: Finished Scan for Top 1000 Ports ({session.name})")
            # analyse_results(session=session)
        except Exception as e:
            print("[!] NMap: Exception Occured while performing scan for top 1000 ports:",str(e))
            session.write(f"[!] NMap: Failed to Complete Scan for Top 1000 Ports ({session.name})")

def scan_open_ports(session):
    if session:
        print(f"[*] NMap: Starting Scan for Open Ports ({session.name})")
        try:
            session.write(f"[*] NMap: Starting Scan for Open Ports ({session.name})")
            logfile_name = path_join(session.session_dir, f'NMap-open_ports_scan_({session.name})')+".txt"
            logfile_name = logfile_name.replace("'",r"\'")
            command = f'''{banner}
sleep 2 ;
clear ;
nmap --open -p 1-65535 -sC -Pn -sV -v {session.Site.domain} -T5 -oX NMap.xml ;
'''
            print(command)
            terminal.execute_command(command=command,width=82,height=28,fontsize="mini", output_file=logfile_name)
            print(f"[*] NMap: Finished Scan for Open Ports ({session.name})")
            session.write(f"[*] NMap: Finished Scan for Open Ports ({session.name})")
            # analyse_results(session=session)
        except Exception as e:
            print("[!] NMap: Exception Occured while performing scan for open ports:",str(e))
            session.write(f"[!] NMap: Failed to Complete Scan for Top Open Ports ({session.name})")

# def analyse_results(session):
#     try:
#         xml_file_path = path_join(session.session_dir, "NMap.xml")
#         if not exists(xml_file_path):
#             print("[!] NMap: Can't find Results file (NMap.xml)")
#             session.write("[!] NMap: Can't find Results file (NMap.xml)")
#             return False
#         with open(xml_file_path, 'r') as file:
#             results = xml_parse(file.read())
#             results = dumps(results, indent=4)
#             results = loads(results)
#         # print(results)
#         host_info = results.get('nmaprun', {}).get('host', {})
#         ip = host_info.get("address",{}).get("@addr","")
#         ports = host_info.get('ports', {}).get('port', [])
#         if not ip or not ports:
#             return False
#         for port in ports:
#             if port.get('state', {}).get('@state')!="open":
#                 continue
#             port_info = {}
#             protocol = port.get('@protocol')
#             portid = port.get('@portid')
#             service = port.get('service', {})
#             service_name = service.get('@name')
#             # service_fp = service.get('@servicefp')
#             product = service.get('@product')
#             version = service.get('@version')

#             port_info["port"] = portid
#             port_info["protocol"] = protocol.lower() if protocol else ""
#             port_info["service"] = service_name.lower() if service_name else ""
#             # port_info["fingerprint"] = service_fp.lower() if service_fp else ""
#             port_info["product"] = product.lower() if product else ""
#             port_info["version"] = version.lower() if version else ""
#             session.Site.tech.add_open_port(ip,port_info)
            
#         return True
#     except JSONDecodeError:
#         print("[!] NMap: Failed to Analyse Results file (NMap.xml)")
#         session.write("[!] NMap: Failed to Analyse Results file (NMap.xml)")
#         return False
#     except Exception as e:
#         print(f"[!] NMap: Exception occured while analysing results:",str(e))
#         return False

banner = r'''
#!/bin/bash



a1="                                                                        
                                                                                
                               ##%###%%%%%%%##&##                               
                        #(#%&@@@@@@@@@@@@@@@@@@@@@@&#%(#                        
                   /#(#%@@@@@@@@@@@@@&&&&&@@@@@@@@@@@@&@@%##(                   
               ###%%@&@@&@&%%##%%%%%%###%##%%#%%#####&@@#@@@@@###               
           .###@@&@@@@&%%&&%%%&&%#%#######%&&&%%#%#%%&&&%#@@%@@@@%%##           
        #%&@@%@@@@%%%&&&&&&%%%&%%####******/%##%%&&%%%&&&&&&##@@%@@@@(%#        
     #%(@#@@#@&%%&&&&&&&&&%%&%%%%%%/**/***(**%#%%%%%%%&&&&&&&&&&(%@@&@@@&#%     
   %%(@@&@@#%&@@@@@@@@@@@@%%&&&%%%%(**(***(**%%%&&&&&%@@@@@@@@@@@@@%(%@&@@@#&*  
  %%%@%/%%%%%@@@@@@@@@@@@@@%&@@&&%%%&/*****(%%%&&&&&%&@@@@@@@@@@@@@%(&&&/(&@#&, 
   #(#%#&#&#&#%(%&@@@@@@@@@@%%&&&&%%%%%%%%%%%&%&&&&%&@@@@@@@@@&#%%%%&&&&##(#%   
            ###((&&&%(#%&@@@@@%&%&&&&&%%%%&&%%&&%%%@@@@@#%%#&#&(###(            
                  *%(%#&&&&(%#%&&%%%%%%&&%%&&%%%&####%&&&&##%(                  
                       ##(#&&&&&&&%########%#%&&&&&&&#((#                       
                            #(#%(#&&&&&&&&&&&&#(%#(%#                           


             .,,,,,,,,,,,,,,,,,,   ,,,,,,,,,,,,,,   ,,,,,,,,,,.                 
             ,/&&&&  *&&&&%#&&&#, ,,&&&&,/&&&&&&,,  ,&&&&&&&&&&,,               
              .,%%#%%  (%%  %%#%#,/%%%%  *,%%,*%%,,  ,#%#    *%%,               
              .,%%  %%((%%  %%*%%%%  %%   %%%%%%%%,, ,(%%%%%%%/,                
              ,,##   *####  ##   ((  ##  ##*    *##, ,(##,,,,                   
             ,,#####   ### #####   #########(  (####(#######,.                  
                                                                                                                                                                                       
"
echo -n "$a1"

'''

if __name__=="__main__":
    show_banner()