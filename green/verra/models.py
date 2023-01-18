from typing import Any, Optional

from green.verra.endpoints import API_PATH


class Project:
    def __init__(self, verra: "Verra", data: dict[str, Any]):
        self._verra = verra
        self.resourceIdentifier = None
        for attr, val in data.items():
            setattr(self, attr, val)

    def summary(self) -> list:
        return self._verra.get(
            url=API_PATH["project_summary"].format(project=self.resourceIdentifier)
        )


class Program:
    def __init__(self, verra: "Verra", name: str):
        self._verra = verra
        self.name = name

    def parameters(self, types: Optional[list[str]]) -> dict[str, Any]:
        params = {
            "program": self.name,
            "types": types
            or [
                "protocolCategory",
                "resourceStatus",
                "country",
                "region",
                "protocol",
                "creditingPeriodType",
                "inputType",
                "programObjective",
            ],
            "inUseOnly": True,
        }
        return self._verra.get(url=API_PATH["parameters"], params=params)

    def projects(
        self,
        body: Optional[dict[str, str]] = None,
        params: Optional[dict[str, Any]] = None,
    ) -> list[Project]:
        if params is None:
            params = {
                "maxResults": 2**31 - 1,
                "$top": 2**31 - 1,
                "$count": True,
                "$skip": 0,
            }
        if body is None:
            body = {"program": self.name}

        res = self._verra.post(url=API_PATH["search"], params=params, body=body)
        return [Project(self._verra, data) for data in res["value"]]

    def summary(self) -> list:
        return self._verra.get(
            url=API_PATH["program_summary"].format(program=self.name)
        )
