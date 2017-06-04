# Simple network speed test
# using `requests` and Google.com
import time
import requests

def connect_to_google():
    requests.get("http://www.google.com")

start_time = time.time()
connect_to_google()
end_time = time.time()
difference = end_time - start_time

print("It took", difference, "seconds")
