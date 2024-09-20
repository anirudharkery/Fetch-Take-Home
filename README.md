# Fetch-Take-Home
# HTTP Endpoint Health Checker

This Python script checks the health of HTTP endpoints specified in a provided YAML configuration file.
Note: While we have used the given sample input file for testing, this script can perform health checks on any YAML file that follows the schema listed

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

1. Clone this repository or download the script files to your local machine.
   
2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script with the following command:
   ```
   python health_checker.py <path_to_yaml_file>
   ```
   Replace <path_to_yaml_file> with the path to your YAML configuration file. This can be either the provided sample file or your own custom file.

4. The script will start checking the endpoints every 15 seconds and display the results in the console.

5. To stop the script, press Ctrl+C.

## Output

The script will output the availability percentage for each domain after every check cycle. For example:

```
fetch.com has 67% availability percentage
www.fetchrewards.com has 100% availability percentage
```

## Notes

- The script considers an endpoint "UP" if it responds with a 2xx status code and the response time is less than 500 ms.
- Ensure you have a stable internet connection while running the script.
