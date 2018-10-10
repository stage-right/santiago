BASE_URI = 'https://api.digitalocean.com/v2/'

def request(endpoint, headers={}, params={}, method="get"):
    return getattr(requests, method)(BASE_URI + endpoint, headers=headers, params=params)

def all_domains(api_key=None):
    return request("/domains/", {'Content-Type': 'application/json', 'Authorization': "Bearer %s" % api_key}).json()['domains']

def main():
    return "Hello World"
