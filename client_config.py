from pyupdater.client import ClientConfig

def get_client_config():
    client_config = ClientConfig()
    client_config.APP_NAME = "MyApp"
    client_config.APP_VERSION = "1.0.0"
    client_config.UPDATE_URLS = ["http://example.com/updates/"]
    return client_config
