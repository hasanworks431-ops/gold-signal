import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class BaseProvider:

    def __init__(self):

        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET"]
        )

        adapter = HTTPAdapter(max_retries=retry)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, url, **kwargs):

        kwargs.setdefault("timeout", 10)

        response = self.session.get(url, **kwargs)

        response.raise_for_status()

        return response
