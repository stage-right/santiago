BASE_URI = 'https://api.digitalocean.com/v2/'

def request(endpoint, params={}, method="get"):
    return getattr(requests, method)(BASE_URI + endpoint, params=params)

def main():
    return "Hello World"
