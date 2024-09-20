import yaml
import requests
import time
from collections import defaultdict
import argparse

class HealthChecker:
    def __init__(self, config_file):
        self.endpoints = self.load_config(config_file)
        self.domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def check_endpoint(self, endpoint):
        url = endpoint['url']
        method = endpoint.get('method', 'GET')
        headers = endpoint.get('headers', {})
        body = endpoint.get('body')

        try:
            start_time = time.time()
            response = requests.request(method, url, headers=headers, data=body, timeout=1)
            response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

            is_up = 200 <= response.status_code < 300 and response_time < 500
            status = "UP" if is_up else "DOWN"
            reason = ""
            if not is_up:
                if response_time >= 500:
                    reason = f"(response latency is not less than 500 ms)"
                else:
                    reason = f"(response code is not in range 200–299)"

            print(f"Endpoint with name {endpoint['name']} has HTTP response code {response.status_code} "
                  f"and response latency {response_time:.0f} ms => {status} {reason}")
            return is_up
        except requests.RequestException as e:
            print(f"Endpoint with name {endpoint['name']} is DOWN. Error: {str(e)}")
            return False

    def run_health_checks(self):
        for endpoint in self.endpoints:
            domain = endpoint['url'].split('/')[2]
            is_up = self.check_endpoint(endpoint)
            self.domain_stats[domain]['total'] += 1
            if is_up:
                self.domain_stats[domain]['up'] += 1

    def log_availability(self):
        for domain, stats in self.domain_stats.items():
            availability = round((stats['up'] / stats['total']) * 100)
            print(f"{domain} has {availability}% availability percentage")

    def run(self):
        try:
            cycle = 1
            while True:
                print(f"\nTest cycle #{cycle} begins at time = {(cycle-1)*15} seconds:")
                self.run_health_checks()
                print(f"\nTest cycle #{cycle} ends. The program logs to the console:")
                self.log_availability()
                cycle += 1
                time.sleep(15)
        except KeyboardInterrupt:
            print("\nProgram manually stopped by user. Exiting...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Endpoint Health Checker")
    parser.add_argument("config_file", help="Path to the YAML configuration file")
    args = parser.parse_args()

    checker = HealthChecker(args.config_file)
    checker.run()
