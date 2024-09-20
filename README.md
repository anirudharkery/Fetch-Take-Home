# Fetch-Take-Home
# HTTP Endpoint Health Checker

This Python script checks the health of HTTP endpoints specified in a provided YAML configuration file.

## Prerequisites

- Python 3.6 or higher

## Setup

1. Ensure Python 3.6+ is installed on your system.

2. Open a terminal or command prompt.

3. Install the required packages:
   ```
   pip install pyyaml requests
   ```

## Running the Script

1. Place the `health_checker.py` script and the provided YAML file in the same directory.

2. Run the script with the following command:
   ```
   python health_checker.py endpoints_config.yaml
   ```

3. The script will start checking the endpoints every 15 seconds and display the results in the console.

4. To stop the script, press Ctrl+C.

## Output

The script will output the availability percentage for each domain after every check cycle. For example:

```
fetch.com has 67% availability percentage
www.fetchrewards.com has 100% availability percentage
```

## Notes

- The script considers an endpoint "UP" if it responds with a 2xx status code and the response time is less than 500 ms.
- Ensure you have a stable internet connection while running the script.
