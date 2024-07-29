from re import match, findall
from sys import path
from os.path import dirname, abspath
path.append(dirname(abspath(__file__)))
from Technology import Technology

class SiteInfo:
    def __init__(self):
        self.domain = None
        self.port = None
        self.protocol = None
        self.tech = Technology()

    def set_info(self,url):
        try:
            """
            Sets the domain from a given URL using regex.
            """
            if not type(url)==str:
                raise ValueError("Url must be a string")

            domains = match(r'https?://(?:www\.)?([^/]+)', url)
            if domains:
                self.site = domains.group(1)
                if ":" in self.site:
                    self.port = self.site.split(":")[1]
                self.domain = self.site.split(":")[0]
                self.protocol = findall(r"^[a-zA-Z]+",domains.group(0))[0]
            else:
                raise ValueError("Invalid URL format")
        except Exception as e:
            print("Exception Occured while setting domain:",str(e))
    
def site(url):
    new_site = SiteInfo()
    new_site.set_info(url=url)
    return new_site

# Example usage:
if __name__ == "__main__":
    site_info = SiteInfo()
    site_info.set_info("https://stackoverflow.com:443/questions")
    print(site_info.site)
    print(site_info.domain)
    print(site_info.port)
    print(site_info.protocol)

