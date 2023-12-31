import requests


# Obtener las netwoks
def get_all_networks(api_key, org_id):
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"
    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    params = {

    "perPage": 1300
    }

    response = requests.get(url, headers=headers, params= params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de redes: Código de estado {response.status_code}")
        return None


# Obtener vlan 
def get_vlans_of_network(api_key, network_id):
    url = f"https://api.meraki.com/api/v1/networks/{network_id}/appliance/vlans"
    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de VLAN: Código de estado {response.status_code}")
        return None
    

# Obtener equipos en netwoks

def get_device_of_networks(api_key, networks_id):

    url = f"https://api.meraki.com/api/v1/networks/{networks_id}/devices"

    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de DEVICE: Código de estado {response.status_code}")
        return None
    

def get_vlans_dns_networks(api_key, networks_id):

    url = f"https://api.meraki.com/api/v1/networks/{networks_id}/appliance/vlans"

    headers = {
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }
    response = requests.request('GET', url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la solicitud de vlans: Código de estado {response.status_code}")
        return None