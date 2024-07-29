from sys import path
from os.path import dirname, abspath
path.append(dirname(abspath(__file__)))
from ftp import check_all as ftp_check
from ssh import check_all as ssh_check

port_checkers = {"ftp":ftp_check,"ssh":ssh_check}

def check(session):
    port_infos = session.Site.tech.open_ports
    if port_infos:
        for ip_address in port_infos.keys():
            for port_info in port_infos.get(ip_address,[]):
                checker = port_checkers.get(port_info.get("service","None"))
                if checker:
                    results = checker(ip_address,int(port_info.get("port")))
                    for test,result in results.items():
                        print(f"{test} = {str(result)}\n")
                        session.write(f"{test} = {str(result)}\n")
