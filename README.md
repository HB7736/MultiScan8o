# MultiScan8o

MultiScan8o is simple multi-scan tool tool for security analysis of websites using various other popular tools.

## Features

- **CMS Detection**: Identifies the CMS and runs relevant scans.
- **Port Scanning**: Uses Nmap to scan top or open ports.
- **Firewall Detection**: Detects web application firewalls with Wafw00f.
- **Subdomain and Email Enumeration**: Gathers subdomains and emails with theHarvester.
- **Web Content Discovery**: Discovers hidden web content using FFUF.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/hb7736/multiscan8o.git
    cd multiscan8o
    ```

2. **Install dependencies**:
    ```sh
    sudo apt update && sudo apt install -y python3 wafw00f theharvester cmseek wpscan joomscan nmap ffuf
    pip3 install -r requirements.txt
    ```

## Usage

Run the script:

```sh
python multiscan.py --wpscan-token <YOUR_WPSCAN_TOKEN> --url TARGET_URL
```

- `--wpscan-token`: WPScan token (optional).
- `--url`: Target URL.
