from modules import session
from modules.variables import Site, Config
from modules.tools import banner, wafw00f, theharvester, cmseek, wpscan, joomscan, nmap, ffuf
import argparse
import threading


def cms_scan(new_session):
    try:
        scans = []
        if new_session.Site.tech.CMS.lower() == "joomla":
            scans.append(threading.Thread(target=joomscan.enumerate, args=(new_session,)))
            scans.append(threading.Thread(target=ffuf.webcontent_joomla_scan, args=(new_session,)))
        elif new_session.Site.tech.CMS.lower() in ["wordpress", "wp"]:
            scans.append(threading.Thread(target=wpscan.full_scan, args=(new_session,)))
            scans.append(threading.Thread(target=ffuf.webcontent_wordpress_scan, args=(new_session,)))
        elif new_session.Site.tech.CMS.lower() in ["drupal", "dr"]:
            scans.append(threading.Thread(target=ffuf.webcontent_drupal_scan, args=(new_session,)))
        elif new_session.Site.tech.CMS.lower() in ["magento", "mg"]:
            scans.append(threading.Thread(target=ffuf.webcontent_magento_scan, args=(new_session,)))
        elif new_session.Site.tech.CMS.lower() in ["ghost", "gh"]:
            scans.append(threading.Thread(target=ffuf.webcontent_ghost_scan, args=(new_session,)))
        else:
            scans.append(threading.Thread(target=ffuf.webcontent_discovery, args=(new_session,)))
        _ = [scan.join() for scan in [scan for scan in scans if scan.start() or True]]
    except Exception as e:
        print("[!] Exception Occurred While Running CMS scans:", str(e))

def run_nmap(new_session):
    try:
        cms = new_session.Site.tech.CMS
        nmap.scan_top1000_ports(session=new_session) if cms and cms!="Not Checked" else nmap.scan_open_ports(session=new_session)
    except Exception as e:
        print("[!] Exception Occurred While Running Nmap scans:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Scanner")
    parser.add_argument("--wpscan-token", default=None, required=False, help="Set WPScan Token")
    parser.add_argument("-u","--url", default=None, required=False, help="URL to use for scan")
    args = parser.parse_args()
    if args.wpscan_token:
        token = args.wpscan_token
        if token.isalnum() and len(token) == 43:
            if not Config.save_token(name="WPScan", value=token):
                print("[!] Token Rejected By WPScan")
                return
        else:
            print(f"[!] WPScan Token {token} Invalid")
            return
    new_session = None
    url = args.url
    try:
        new_Site = Site.SiteInfo()
        if url:
            new_Site.set_info(url)
        else:
            new_Site.set_info(input("Enter Site URL: "))
        if new_Site.domain:
            try:
                new_session = session.Session(Site=new_Site)
                new_session.start()
                banner.use_Hacking_banner()
                scans = []

                # Creating wafw00f thread
                scans.append(threading.Thread(target=wafw00f.detect_firewall, args=(new_session,)))
                # Creating theHarvester thread
                scans.append(threading.Thread(target=theharvester.domain_full_scan, args=(new_session,)))
                # Creating cmseek thread
                scans.append(threading.Thread(target=cmseek.deep_scan, args=(new_session,)))
                # Starting all threads and waiting till finish
                _ = [scan.join() for scan in [scan for scan in scans if scan.start() or True]]

                post_scans = []
                # Creating CMS-specific scans thread
                post_scans.append(threading.Thread(target=cms_scan, args=(new_session,)))
                # Creating nmap scans thread
                post_scans.append(threading.Thread(target=run_nmap, args=(new_session,)))
                # Starting all threads and waiting till finish
                _ = [scan.join() for scan in [scan for scan in post_scans if scan.start() or True]]

            except Exception as e:
                print("[!] Exception Occurred:", str(e))
            new_session.write(str(new_session.Site.tech))
        else:
            print("[!] Domain Not Set.............")
    except KeyboardInterrupt:
        print("[!] Process Interrupted By User")
    except Exception as e:
        print("[!] Exception Occurred:", str(e))
    finally:
        new_session.end() if new_session else None

if __name__ == "__main__":
    main()
