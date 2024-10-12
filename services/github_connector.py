# services/github_connector.py
import requests
import json

def load_form_config(config_url):
    """
    Loads form configuration from a provided GitHub URL.
    
    :param config_url: URL to the JSON configuration file
    :return: JSON data as a dictionary
    """
    try:
        response = requests.get(config_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching form configuration: {e}")
        return {}


