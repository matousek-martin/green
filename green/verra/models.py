from typing import Any, Optional

from green.verra.endpoints import API_PATH


class Project:
    def __init__(self, verra: "Verra", data: dict[str, Any]):
        self._verra = verra
        self.program = data['program']
        self.resourceIdentifier = data['resourceIdentifier']
        self.resourceName = data['resourceName']
        self.proponent = data['proponent']
        self.operator = data['operator']
        self.designee = data['designee']
        self.protocolCategories = data['protocolCategories']
        self.protocolSubCategories = data['protocolSubCategories']
        self.protocols = data['protocols']
        self.resourceStatus = data['resourceStatus']
        self.country = data['country']
        self.estAnnualEmissionReductions = data['estAnnualEmissionReductions']
        self.region = data['region']
        self.projectRegistrationDate = data['projectRegistrationDate']
        self.version = data['version']
        self.compatibleProgramScenarioTypeName = data['compatibleProgramScenarioTypeName']
        self.inputTypes = data['inputTypes']
        self.programObjectives = data['programObjectives']
        self.creditingPeriodStartDate = data['creditingPeriodStartDate']
        self.creditingPeriodEndDate = data['creditingPeriodEndDate']
        self.createDate = data['createDate']

    def summary(self) -> list:
        return self._verra.get(
            url=API_PATH["project_summary"].format(project=self.resourceIdentifier)
        )


class Program:
    def __init__(self, verra: "Verra", name: str):
        self._verra = verra
        self.name = name

    def parameters(
        self, params: Optional[dict[str, str]]
    ) -> dict[str, Any]:
        params = {
            "program": self.name,
            "types": [
                "protocolCategory",
                "resourceStatus",
                "country",
                "region",
                "protocol",
                "creditingPeriodType",  # VCS
                "inputType",            # PWRP
                "programObjective",     # CA_OPR
            ],
            "inUseOnly": True,
        }
        return self._verra.get(url=API_PATH["parameters"], params=params)

    def projects(
        self,
        body: Optional[dict[str, str]] = None,
        params: Optional[dict[str, str]] = None,
    ) -> list[Project]:
        params = {
            "maxResults": 2**31 - 1,
            "$top": 2**31 - 1,
            "$count": True,
            "$skip": 0,
        }
        if body is None:
            body = {}
        body["program"] = self.name

        res = self._verra.post(url=API_PATH["search"], params=params, body=body)
        return [Project(self._verra, data) for data in res['value']]

    def summary(self) -> list:
        return self._verra.get(
            url=API_PATH["program_summary"].format(program=self.name)
        )
