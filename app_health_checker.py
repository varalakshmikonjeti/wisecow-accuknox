import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://wisecow.local"  # using HTTPS now

def check_app_health():
    try:
        response = requests.get(URL, timeout=5, verify=False)  # verify=False ignores self-signed cert
        if response.status_code == 200:
            print(f"Application is UP ✅ (Status: {response.status_code})")
        else:
            print(f"Application is DOWN ⚠️ (Status: {response.status_code})")
    except requests.RequestException as e:
        print(f"Application is DOWN ⚠️ (Error: {e})")

if __name__ == "__main__":
    check_app_health()
