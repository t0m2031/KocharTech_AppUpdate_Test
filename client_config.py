from pyupdater.client import ClientConfig

# client_config.py
def get_client_config():
    client_config = {
        'APP_NAME': 'KocharTechApp',
        'APP_VERSION': '1.0.0',
        'UPDATE_URLS': ['https://github.com/t0m2031/KocharTech_AppUpdate_Test/releases']
        # Add more configuration settings if needed
    }
    return client_config
