import requests
import urllib.parse
import json
import hashlib
global api_url

# -------------------------------------------------
# SET API ENDPOINT FOR THE EVERGREEN SERVER
#
api_url = 'https://cool-cat.org/osrf-gateway-v1'
# -------------------------------------------------


def retrieve_auth_token(*params):
    """
    Returns an authentication token with the user's permissions

    :param params:
        barcode (str): User barcode
        password (str): User password
        type ['opac']:
    :return:
        authtoken (str)
    """

    post = urllib.parse.urlencode(
        {'service': 'open-ils.auth',
         'method': 'open-ils.auth.login'
         }
    )

    for param in params:
        post += f'&param={json.dumps(param)}'

    response = requests.post(api_url, data=post.encode())
    auth_response = response.json()
    authtoken = auth_response['payload'][0]['payload']['authtoken']

    return authtoken


def post(service, method, *params):
    """
    POST a command to an Evergreen API endpoint and receive a JSON response

    :param service:
        the name of the OpenSRF application (str) e.g. open-ils.auth
    :param method:
        the registered OpenSRF method to be called (str) e.g. open-ils.auth.login
    :param params:
        params are defined in the method declaration for each OpenSRF application; sent params must be ordered as they
        are in the method declaration
    :return:
        JSON payload for API service
    """

    post = urllib.parse.urlencode(
        {
            'service': service,
            'method': method
        }
    )

    for param in params:
        post += f'&param={json.dumps(param)}'

    response = requests.post(api_url, data=post.encode())

    return response.json()['payload']


def md5_hash(password):
    """
    Hashes a password with MD5 algorithm

    :param password:
        the user's password
    :return:
        hashed password
    """

    hashed_password = hashlib.md5(str(password).encode('utf-8')).hexdigest()

    return hashed_password
