import requests

BASE_URI = 'https://api.digitalocean.com/v2/'

def request(endpoint, headers={}, params={}, method="get"):
    return getattr(requests, method)(BASE_URI + endpoint, headers=headers, params=params)

def headers(api_key=None):
    return {'Content-Type': 'application/json', 'Authorization': "Bearer %s" % api_key}

# domains
def all_domains(api_key=None):
    return request("/domains/", headers(api_key)).json()['domains']

def new_domain(domain, api_key=None):
    return request("/domains/", headers(api_key), domain, "post").json()['domain']

# subdomains
def all_domain_records(domain_id, api_key=None):
    return request('/domains/%s/records/' % domain_id, headers(api_key)).json()['domain_records']

def domain_record_id(domain_id, record_name, api_key=None):
    for record in all_domain_records(domain_id, api_key):
        if record['name'] == record_name:
            return record['id']

def new_domain_record(domain_id, record, api_key=None):
    return request('/domains/%s/records/' % domain_id, headers(api_key), record, "post").json()['domain_record']

def destroy_domain_record(domain_id, record_id, api_key=None):
    return request('/domains/%s/records/%s' % (domain_id, record_id), headers(api_key), {}, method='delete')

# droplets
def all_droplets(api_key=None):
    return request("/droplets/", headers(api_key)).json()['droplets']

def new_droplet(droplet, api_key=None):
    return request("/droplets/", headers(api_key), droplet, "post").json()['droplet']

def destroy_droplet(droplet_id, api_key=None):
    return request("/droplets/%s" % droplet_id, headers(api_key), {}, "delete")

# ssh keys
def all_ssh_keys(api_key=None):
    return request("/account/keys/", headers(api_key)).json()['ssh_keys']

def new_ssh_key(key, api_key=None):
    return request("/account/keys/", headers(api_key), key, "post").json()['ssh_key']

def destroy_ssh_key(key_id, api_key=None):
    return request("account/keys/%s" % key_id, headers(api_key), {}, "delete")
