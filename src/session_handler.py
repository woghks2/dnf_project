import requests
from requests.adapters import HTTPAdapter

class SessionHandler:
    def __init__(self, headers=None, pool_connections=50, pool_maxsize=100):
        self.session = requests.Session()
        adapter = HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize)
        self.session.mount('https://', adapter)
        if headers:
            self.session.headers.update(headers)

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)

    def close(self):
        self.session.close()

# headers = {
    # 'Keep-Alive': 'timeout=5, max=1000'
    # 'Connection': 'close'
# }
