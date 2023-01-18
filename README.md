# Green

Green is a python package that provides simple access to carbon registries.

```
from green import Verra

verra = Verra()
projects = verra.vcs.projects()

projects[0].summary()
```

```

{
    "resourceIdentifier": "4086",
    "resourceName": "Suihuang Adjusted Water Management in Rice Cultivation",
    "description": "The project changing from continuously flooded to intermittent flooded condition during rice cultivation is conducted in Suicheng District and Huanglo Town within Suixi County, Zhanjiang City, Guangdong Province of China, with a total acreage of 6,545 ha for double-cropping rice. Without the implementation of this project, the continuously flooded method would be continued, so the scenario that rice was cultivated by continuously flooded method is the baseline scenario. Since the organic matter in rice soil under flooded condition can emit a large amount of methane (CH4) because of anaerobic decomposition, the intermittent flooded method is more beneficial to water conservation, production increase and methane emission reduction than the continuously flooded.\r\nThis project solved the problems of excessive water used during rice cultivation which results in not only large amount of methane (CH4) emissions but also low rice productivity by replacing the continuously flooded method with intermittent flooded method, which shortens the period of anaerobic decomposition of soil organic matter. In this case, the CH4 emission can be declined by an average of 48%1 . Hence, with the proposed project activity, an estimated amount of GHG emission reduction 9.15 tCO2e/ha for double-cropping rice is expected. Annual average estimation of GHG emission reductions from the project activity is 59,906 tCO2e/year, and the total GHG emission reductions are 599,060 tCO2e during the fixed 10 years crediting period.\r\nThis project aims to:\r\n- Sequester greenhouse gas and mitigate climate changes;\r\n- Increase the rice productivity resulting in higher living standard of local farmers;\r\n- Increase the number of local individuals who have relevant skills due to diversified educational opportunities from trainings;\r\n- Provide more job opportunities, especially women workers.",
    "location": {"latitude": 21.301452, "longitude": 110.184911},
    "inPublicCommentPeriod": True,
    "lastPublicCommentPeriod": None,
    "attributes": [
        {"code": "PROJECT_ID", "values": [{"type": "string", "value": "4086"}]},
        {
            "code": "STATE_PROVINCE",
            "values": [{"type": "string", "value": "Guangdong Province"}],
        },
    ],
    "participationSummaries": [
        {
            "programCode": "VCS",
            "attributes": [
                {
                    "code": "PROPONENT_NAME",
                    "values": [
                        {
                            "type": "string",
                            "value": "Xuwen Xinpenggang Building Materials Co., Ltd.",
                        },
                        {"type": "string", "value": "Guangdong Province, China"},
                    ],
                },
                {
                    "code": "PROJECT_STATUS",
                    "values": [{"type": "string", "value": "Under validation"}],
                },
                {
                    "code": "EST_ANNUAL_EMISSION_REDCT",
                    "values": [{"type": "string", "value": "59906"}],
                },
                {
                    "code": "PRIMARY_PROJECT_CATEGORY_NAME",
                    "values": [
                        {
                            "type": "string",
                            "value": "Agriculture Forestry and Other Land Use",
                        }
                    ],
                },
                {
                    "code": "PROJECT_SUBCATERGORY_NAMES",
                    "values": [{"type": "string", "value": "ALM"}],
                },
                {
                    "code": "PROTOCOL_NAME",
                    "values": [{"type": "string", "value": "AMS-III.AU"}],
                },
                {
                    "code": "PROJECT_ACREAGE",
                    "values": [{"type": "string", "value": "6545 Hectares"}],
                },
                {
                    "code": "VALIDATOR_NAME",
                    "values": [
                        {
                            "type": "string",
                            "value": "Shenzhen CTI International Certification Co., Ltd (CTI)",
                        }
                    ],
                },
                {
                    "code": "CREDIT_PERIOD_INFO",
                    "values": [
                        {"type": "string", "value": "1st, 02/03/2020 - 01/03/2030"}
                    ],
                },
            ],
        }
    ],
    "documentGroups": [
        {
            "code": "VCS_PIPELINE_DOCUMENTS",
            "description": "VCS Pipeline Documents",
            "documents": [
                {
                    "uri": "https://registry.verra.org/mymodule/ProjectDoc/Project_ViewFile.asp?FileID=82576&IDKEY=0lksjoiuwqowrnoiuomnckjashoufifmln902309ksdflku098w113872304",
                    "documentType": "Draft Project Description",
                    "documentName": "PROJ_DESC_DRAFT_4086_11JAN2023.pdf",
                    "uploadDate": "2023-01-12T06:54:02.97Z",
                },
                {
                    "uri": "https://registry.verra.org/mymodule/ProjectDoc/Project_ViewFile.asp?FileID=82574&IDKEY=j98klasmf8jflkasf8098afnasfkj98f0a9sfsakjflsakjf8d8113869546",
                    "documentType": "Listing Representation",
                    "documentName": "LIST_REP_4086_28DEC2022.pdf",
                    "uploadDate": "2023-01-12T06:51:29.86Z",
                },
            ],
        },
        {
            "code": "VCS_REGISTRATION_DOCUMENTS",
            "description": "VCS Registration Documents",
            "documents": [],
        },
        {
            "code": "VCS_ISSUANCE_DOCUMENTS",
            "description": "VCS Issuance Documents",
            "documents": [],
        },
        {
            "code": "VCS_OTHER_DOCUMENTS",
            "description": "VCS Other Documents",
            "documents": [
                {
                    "uri": "https://registry.verra.org/mymodule/ProjectDoc/Project_ViewFile.asp?FileID=82573&IDKEY=0903q4jsafkasjfu90amnmasdfkaidflnmdf9348r09dmfasdfa113868167",
                    "documentType": "Communications Agreement",
                    "documentName": "COMMS_AGREE_4086_28DEC2022.pdf",
                    "uploadDate": "2023-01-12T06:50:44.89Z",
                },
                {
                    "uri": "https://registry.verra.org/mymodule/ProjectDoc/Project_ViewFile.asp?FileID=82577&IDKEY=u097809fdslkjf09rndasfufd098asodfjlkduf09nm23mrn87j113873683",
                    "documentType": "KML File",
                    "documentName": "KML_4086.kml",
                    "uploadDate": "2023-01-12T06:54:53.477Z",
                },
            ],
        },
    ],
    "childResources": [],
}
```