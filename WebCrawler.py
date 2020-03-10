import requests

### Functions ###

def status(status_code):
    if requests.status_codes != 200:
        print("The Website isn't available at the moment")
        return False


### Functions ###

status()