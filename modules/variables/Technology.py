from re import findall

class Technology:
    def __init__(self):
        self.web_technologies = []  # List of web technologies used
        self.domains = []        # List of discovered domains
        self.firewall = "Not Checked"        # Discovered Firewall
        self.CMS = "Not Checked"               # CMS type (e.g., WordPress, Joomla)
        self.CMS_version = ""       # CMS version (e.g., 1.0.0, v2.0-13)
        self.CMS_Users = []         # List of CMS users
        self.emails = []            # List of discovered email addresses
        self.ip_addresses = []      # List of discovered IP addresses
        self.open_ports = {}        # Dictionary of IP addresses and their open ports
        self.dns_info = {}          # DNS information
        # self.whois_info = {}        # WHOIS information
        # self.scripts = []           # List of discovered scripts
        self.database_info = {}     # Database information
        # self.ssl_info = {}          # SSL certificate information

    def add_web_technology(self, technology):
        self.web_technologies.append(technology)

    def set_Firewall(self, firewall_name):
        if type(firewall_name)==str:
            self.firewall = firewall_name

    def add_domains(self, domains):
        if type(domains)!=str:
            domains = str(domains)
        domains = findall(r'(?<=[^.-])\b([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]+)(?=\b[^\w.-])',domains)
        for domain in domains:
            if not domain in self.domains:
                self.domains.append(domain)

    def set_CMS(self, cms_name):
        if type(cms_name)==str:
            self.CMS = cms_name
            self.cms_checked = True
    
    def set_CMS_version(self, cms_version):
        if type(cms_version)==str:
            self.CMS_version = cms_version

    def add_CMS_user(self, users):
        if type(users)==list:
            users = ",".join([user for user in users if type(user)==str and 0<len(user)<51])
        if type(users)==str:
            for user in [user for user in users.split(",") if user]:
                self.CMS_Users.append(user)

    def add_email(self, emails):
        if type(emails)==list:
            emails = " ".join([email for email in emails if type(email)==str])
        if type(emails)==str:
            emails = findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",emails)
            for email in emails:
                if not email in self.emails:
                    self.emails.append(email)

    def add_ip_address(self, ip_addresses):
        if not isinstance(ip_addresses, str):
            ip_addresses = str(ip_addresses)
        ip_addresses = findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ip_addresses)

        for ip in ip_addresses:
            ip_parts = ip.split(".")
            if len(ip_parts) == 4:  # Ensure we have exactly 4 parts
                valid = True
                if not any((0 <= int(part) <= 255 for part in ip_parts)):
                    continue
                if valid:
                    self.ip_addresses.append(ip)

    def add_open_port(self, ip_address, port):
        if ip_address not in self.open_ports:
            self.open_ports[ip_address] = []
        self.open_ports[ip_address].append(port)

    def set_dns_info(self, dns_info):
        self.dns_info = dns_info

    # def set_whois_info(self, whois_info):
    #     self.whois_info = whois_info

    # def add_script(self, script):
    #     self.scripts.append(script)

    def set_database_info(self, database_info):
        self.database_info = database_info

    # def set_ssl_info(self, ssl_info):
    #     self.ssl_info = ssl_info

    def __repr__(self):
        reprstr = ""
        reprstr += f"Identfied CMS: "+(f"{self.CMS} {self.CMS_version}\n" if self.CMS else "Not Detected\n")

        reprstr += f"Firewall: "+(f"{self.firewall}\n" if self.firewall else "Not Detected\n")

        if self.web_technologies:
            reprstr += f"Technology used = {self.web_technologies}\n"

        if self.domains:
            reprstr += "domains = "+(',\n          '.join(self.domains))+"\n\n"

        if self.CMS_Users:
            reprstr += f"CMS_Users = {', '.join(self.CMS_Users)}\n\n"

        if self.emails:
            reprstr += "emails = "+(',\n         '.join(self.emails))+"\n\n"

        if self.ip_addresses:
            reprstr += "ip_addresses = "+(',\n               '.join(self.ip_addresses))+"\n\n"

        if self.open_ports:
            IPs = list(self.open_ports.keys())
            if self.open_ports.get(IPs[0]):
                reprstr += f"open_ports = "+('\n             '.join([str(ip) for ip in self.open_ports.get(IPs[0])]))+"\n"
        
        if self.dns_info:
            reprstr += f"dns_info = {self.dns_info}"
        
        if self.database_info:
            reprstr +=f"database_info = {self.database_info}"
            
        return reprstr

if __name__=="__main__":
    # Example usage:
    tech = Technology()
    tech.add_web_technology('Apache')
    tech.add_domains('test.example.com')
    tech.set_CMS('WordPress')
    tech.add_CMS_user('admin')
    tech.add_email('admin@example.com')
    tech.add_ip_address('192.168.1.1')
    tech.add_open_port('192.168.1.1', 80)
    tech.set_dns_info({'A': '192.168.1.1', 'MX': 'mail.example.com'})
    # tech.set_whois_info({'registrar': 'Example Registrar', 'status': 'active'})
    # tech.add_script('jquery.js')
    tech.set_database_info({'type': 'MySQL', 'version': '5.7'})
    # tech.set_ssl_info({'issuer': 'LetsEncrypt', 'valid_from': '2024-01-01', 'valid_to': '2025-01-01'})
    print(tech)