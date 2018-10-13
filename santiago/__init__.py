import requests

BASE_URI = 'https://api.digitalocean.com/v2/'

def request(endpoint, headers={}, params={}, method="get"):
    return getattr(requests, method)(BASE_URI + endpoint, headers=headers, params=params)

def headers(api_key=None):
    return {'Content-Type': 'application/json', 'Authorization': "Bearer %s" % api_key}

def all_domains(api_key=None):
    return request("/domains/", headers(api_key)).json()['domains']

def all_droplets(api_key=None):
    return request("/droplets/", headers(api_key)).json()['droplets']

def new_droplet(droplet, api_key=None):
    return request("/droplets/", headers(api_key), droplet, "post").json()['droplet']

def all_ssh_keys(api_key=None):
    return request("/account/keys", headers(api_key)).json()['ssh_keys']

def main():
    return "Hello World"
