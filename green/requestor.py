from typing import Any, Optional, Type

import requests
from requests.sessions import Session


class Requestor:
    def __init__(self, url: str, session: Optional[Type[Session]] = None):
        self.url = url
        self.session = session or requests.Session()

    def _http(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict[Any, Any] | str] = None,
        body: Optional[dict[Any, Any]] = None,
    ) -> dict:
        url = self.url + endpoint
        response = self.session.request(  # type: ignore[call-arg]
            url=url, method=method, params=params, json=body
        )
        if 299 >= response.status_code >= 200:
            return response.json()
        return {}

    def get(
        self,
        endpoint: str,
        params: Optional[dict[Any, Any] | str] = None,
    ):
        return self._http(method="GET", endpoint=endpoint, params=params)

    def post(
        self,
        endpoint: str,
        params: Optional[dict[Any, Any] | str] = None,
        body: Optional[dict[Any, Any]] = None,
    ):
        return self._http(method="POST", endpoint=endpoint, params=params, body=body)
