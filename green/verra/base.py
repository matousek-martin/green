from typing import Any, Optional, Type
from urllib.parse import urlencode

import requests
from requests.sessions import Session

from green.verra.models import Program


class Verra:
    def __init__(
        self,
        url: str = "https://registry.verra.org/uiapi",
        session: Optional[Type[Session]] = None,
    ):
        self.url = url
        self.session = session or requests.Session()
        self.vcs = Program(self, "VCS")
        self.pwrp = Program(self, "PWRP")
        self.ccb = Program(self, "CCB")
        self.sdvista = Program(self, "SDVISTA")
        self.ca_opr = Program(self, "CA_OPR")

    def _http(
        self,
        method: str,
        url: str,
        params: Optional[dict[Any, Any] | str] = None,
        body: Optional[dict[Any, Any]] = None,
    ) -> dict | list:
        url = self.url + url
        response = self.session.request(  # type: ignore[call-arg]
            url=url, method=method, params=params, json=body
        )
        if 299 >= response.status_code >= 200:
            return response.json()
        return {}

    def get(
        self,
        url: str,
        params: Optional[dict[Any, Any] | str] = None,
    ):
        return self._http(method="GET", url=url, params=params)

    def post(
        self,
        url: str,
        params: Optional[dict[Any, Any] | str] = None,
        body: Optional[dict[Any, Any]] = None,
    ):
        if isinstance(params, dict):
            params = urlencode(params, safe="$")
        return self._http(method="POST", url=url, params=params, body=body)
