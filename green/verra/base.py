from abc import ABC
from typing import Any, Optional
from urllib.parse import urlencode

from green.requestor import Requestor
from green.verra.endpoints import ENDPOINTS


class ProgramBase(ABC):
    def __init__(self):
        self.name = None
        self.section = None
        self.http = Requestor(url="https://registry.verra.org/uiapi")

    def get_search_parameters(
        self, types: Optional[list[str]] = None, in_use_only: bool = True
    ) -> dict[str, Any]:
        params = {
            "program": self.name,
            "types": types
            or [
                "protocolCategory",
                "resourceStatus",
                "country",
                "region",
                "protocol",
                "creditingPeriodType",  # VCS
                "inputType",  # PWRP
                "programObjective",  # CA_OPR
            ],
            "inUseOnly": in_use_only,
        }
        return self.http.get(endpoint=ENDPOINTS["parameters"], params=params)

    def search(
        self,
        body: Optional[dict[str, str]] = None,
        result_size: int = 2**31 - 1,
        count: bool = True,
        skip: Optional[int] = None,
        top: Optional[int] = None,
    ) -> dict:
        query_parameters = {
            "maxResults": result_size,
            "$count": count,
            "$skip": skip or 0,
            "$top": top or result_size,
        }
        params = urlencode(query_parameters, safe="$")
        if body is None:
            body = {}
        body["program"] = self.name
        return self.http.post(endpoint=ENDPOINTS["search"], params=params, body=body)

    def statistics(self) -> list:
        programmes = self.http.get(endpoint=ENDPOINTS["program"])
        for program in programmes:
            if program.get("code") == self.name:
                return program.get("statistics")
        return []


class VerifiedCarbonStandard(ProgramBase):
    def __init__(self):
        super().__init__()
        self.name = "VCS"


class PlasticWasteReductionProgram(ProgramBase):
    def __init__(self):
        super().__init__()
        self.name = "PWRP"


class ClimateCommunityBiodiversityStandards(ProgramBase):
    def __init__(self):
        super().__init__()
        self.name = "CCB"


class SustainableDevelopmentVerifiedImpactStandard(ProgramBase):
    def __init__(self):
        super().__init__()
        self.name = "SDVISTA"


class CaliforniaOffsetProjectRegistry(ProgramBase):
    def __init__(self):
        super().__init__()
        self.name = "CA_OPR"
