# Backend API

## Table of Contents
* [API for Frontend](#API-for-Frontend)
    * [Homepage](#Homepage)
    * [Plan & Update](#Plan-amp-Update)
* [Interface for Backend Planner](#Interface-for-Backend-Planner)

## API for Frontend
Postman collection for testing (i.e. requests filled with parameters already): https://www.getpostman.com/collections/201ddb2dfa1383f654a1

`Remote` ones are the deployed APIs hosted on Heroku already; while `local` ones are what you call if you run the backend locally.

### Homepage
* Remote: `https://yum-travel-planner.herokuapp.com/`
* Local: `http://0.0.0.0:5000/`
* Method: GET
* No parameters.
* Return: Homepage html (dummy json for now)

### Plan & Update
* Remote: `https://yum-travel-planner.herokuapp.com/plan`
* Local: `http://0.0.0.0:5000/plan`
* Method: POST
* Parameters: (passed in body as form data)

| Parameter Name | Type  | Default | Note |
| -------- | --------  | - | -|
| departure_date | str  | (required) | e.g. 2021-04-20
| return_date | str  | (required) | e.g. 2021-04-23
| city | str  | (required) | e.g. Taipei
| price_level  | int | 2 | 0 to 4; 0=free|
| outdoor | float |  0.5 | 0.0 to 1.0
| compactness | float | 0.5 | 0.0 to 1.0
| start_time | str | 0930 | "0930" for 09:30
| back_time | str | 2100 | "2100" for 21:00
| place_ids | str | None | e.g. A5; ordered list*; all selected place ids
| schedule | str | None | e.g. R3; ordered list*; the ids in the current schedule

*To send an ordered list of values, fill the keys multiple times with values in order, such as `['schedule':'R6', 'schedule':'A3']`.

If no `place_ids` nor `schedule` is sent, it makes a new plan. Otherwise, it updates the given `schedule` with the given `place_ids`.

* Return: A dictionary

| Key | Value | Value type |
| -------- | -------- | -------- |
| status   | Success | str     |
| places  | a list of `place`s | list(dict) |
| schedule  | a list of `id`s | list(str) |

See the format of a `place` [here](https://developers.google.com/maps/documentation/places/web-service/search#PlaceSearchResults).

An additional parameter added to each `place` is `id` (in `str`), which is in the format "one uppercase alphabet + a number", where the alphabet is one of `A`ttractions, `R`estaurants. For example, `R924`, `A1302`, and `H78`.

Note that `places` contains more places than `schedule`, because `places` also includes the places that are not selected.

You may separate the schedule into days by the `H`omestays in the `schedule`.

Example return values:
```
{
    "status": "Success",
    "message": "Make a new plan from 2021-04-20 to 2021-04-21 in Taipei",
    "places": [
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "108台灣台北市萬華區武昌街二段72號2樓",
            "geometry": {
                "location": {
                    "lat": 25.044807,
                    "lng": 121.506211
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0461913799,
                        "lng": 121.5075708299
                    },
                    "southwest": {
                        "lat": 25.0434917201,
                        "lng": 121.5048711701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R924",
            "name": "TGI FRIDAYS 星期五美式餐廳 西門餐廳",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/100262368738163148167\">jpanne young</a>"
                    ],
                    "photo_reference": "ATtYBwIFIZYyBswUwriouyB3heeVRDGEd6GskIktd7bVN_7cfM0qlmNf9cLSoVzmOq7BcXeeD7TPMj5-w6VG1CdKLOhdkvca5fec6WBlgyFycvIDXptT6qmJ5QKK_qtJKorMtXFxZXIvEzCbOzzt_BqiW7hQi9xk6f5u2mVpIiAHC_9m9Y4n",
                    "width": 4032
                }
            ],
            "place_id": "ChIJ7U64LwmpQjQRf-tzrAv4f24",
            "plus_code": {
                "compound_code": "2GV4+WF 萬華區 台北市",
                "global_code": "7QQ32GV4+WF"
            },
            "price_level": null,
            "rating": 4.1,
            "reference": "ChIJ7U64LwmpQjQRf-tzrAv4f24",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 2078
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "100台灣台北市中正區襄陽路2號",
            "geometry": {
                "location": {
                    "lat": 25.042754,
                    "lng": 121.515034
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0444865,
                        "lng": 121.5177498
                    },
                    "southwest": {
                        "lat": 25.0401749,
                        "lng": 121.5127818
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
            "id": "A772",
            "name": "國立臺灣博物館",
            "opening_hours": {
                "open_now": false
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2048,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/101298519871740394352\">Atthawut</a>"
                    ],
                    "photo_reference": "ATtYBwJwnO1X9yb9F9lheBblHHC5DBbC4ex7nrJqmuLUgmKlMolSKlcbcwWxLXEwMyQXJikRlnemsrUmnB24GKKxLFRHmUJVQ3dT4D6UysamZrmK5-uL3Re5S3lfWD8NvhwyJs6AjrKPm9DqjT3RLRVUvREeWHIy8YPgX727Y9Kln16I0-Ma",
                    "width": 1536
                }
            ],
            "place_id": "ChIJcRV3WHOpQjQRFpgzTpxZWgo",
            "plus_code": {
                "compound_code": "2GV8+42 中正區 台北市",
                "global_code": "7QQ32GV8+42"
            },
            "rating": 4.4,
            "reference": "ChIJcRV3WHOpQjQRFpgzTpxZWgo",
            "types": [
                "museum",
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 6477
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "115台灣台北市南港區研究院路三段68巷2號號",
            "geometry": {
                "location": {
                    "lat": 25.0348987,
                    "lng": 121.6142317
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0362562799,
                        "lng": 121.6156182299
                    },
                    "southwest": {
                        "lat": 25.0335566201,
                        "lng": 121.6129185701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R248",
            "name": "家常熱炒",
            "opening_hours": {
                "open_now": false
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3008,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/107510193673899060195\">Andrew Sun</a>"
                    ],
                    "photo_reference": "ATtYBwJ1kcyozwKI2u4EGkP8c6DNQptIl-TP_soNXUZEBZ-Muvwm6YFeiivKxgZk80NtddS_dsXTHSm053VWoYpcmJi2jyWMHScEVxF_Y5kPuSyqQDMPcvPBqwn0cAqN9xXjpEYOXvP5ZDh8gxrlbne3KI_-QOG605m3LGYtXutbJLG4uC7E",
                    "width": 4016
                }
            ],
            "place_id": "ChIJ5aTUYjirQjQRMBRfn_7ah24",
            "plus_code": {
                "compound_code": "2JM7+XM 南港區 台北市",
                "global_code": "7QQ32JM7+XM"
            },
            "price_level": null,
            "rating": 4.0,
            "reference": "ChIJ5aTUYjirQjQRMBRfn_7ah24",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 60
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "10841台灣台北市萬華區開封街二段63號1樓",
            "geometry": {
                "location": {
                    "lat": 25.0471039,
                    "lng": 121.5052681
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0484537299,
                        "lng": 121.5066179299
                    },
                    "southwest": {
                        "lat": 25.0457540701,
                        "lng": 121.5039182701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H784",
            "name": "天實商旅 ARTINN",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 1773,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/104732410753287993427\">簡吟玲</a>"
                    ],
                    "photo_reference": "ATtYBwKscmt6l3a5M7n774m4sIkqrZWd11uYGuAXyJzIOIwaSH2kdNNmS9yM8xxTLVgNgOlchnO4aUIxay5_s-pQFxNluYMxKI-VsTlG_X9sGIRd-YeuV-TXp05y2Mm0APYFN1CGm7xetZH2O732OBZB8dLjVKMyOcd6DrhNo0ddPCNi8x-o",
                    "width": 2364
                }
            ],
            "place_id": "ChIJsWHQCcqpQjQRQKaKJ5ehyoE",
            "plus_code": {
                "compound_code": "2GW4+R4 萬華區 台北市",
                "global_code": "7QQ32GW4+R4"
            },
            "rating": 3.1,
            "reference": "ChIJsWHQCcqpQjQRQKaKJ5ehyoE",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 290
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "110台灣台北市信義區松壽路12號4樓",
            "geometry": {
                "location": {
                    "lat": 25.03531,
                    "lng": 121.5660665
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0366598299,
                        "lng": 121.5674163299
                    },
                    "southwest": {
                        "lat": 25.0339601701,
                        "lng": 121.5647166701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R651",
            "name": "Moomin café 嚕嚕米主題餐廳",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 1388,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/115822701374314137099\">玥玥陳</a>"
                    ],
                    "photo_reference": "ATtYBwI9QglONap5Wq0FY3QwRfQkGoEowm01TV31743J8cQPjRRU-HdT9MQl7gU9-NrU4bAMg7B1CM7aKVTw_GJVhhATQnb6DyDGfMGKgLfxPru9AVhic0dCXdO0-Ycvb1NlzeAxSCCHf6hO3wQxvZIi_pw0py67mAY4YP1YVvwI1y5P07iX",
                    "width": 2048
                }
            ],
            "place_id": "ChIJgQPGedCrQjQR1gRW6SCy9Mw",
            "plus_code": {
                "compound_code": "2HP8+4C 信義區 台北市",
                "global_code": "7QQ32HP8+4C"
            },
            "price_level": 2.0,
            "rating": 4.4,
            "reference": "ChIJgQPGedCrQjQR1gRW6SCy9Mw",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 1407
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "103台灣台北市大同區",
            "geometry": {
                "location": {
                    "lat": 25.0569669,
                    "lng": 121.5078537
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0583167299,
                        "lng": 121.5092035299
                    },
                    "southwest": {
                        "lat": 25.0556170701,
                        "lng": 121.5065038701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "id": "A1302",
            "name": "唐山帆船造景",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2092,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/113538313045642352133\">Nomad YC</a>"
                    ],
                    "photo_reference": "ATtYBwKu1PXfO-rzukrdERaKH99hvpULCNshWvxNQci9ya1YqDQMJ1yij77KgXpE6r21WrMrvKVFg9g72d8U1fT-HVKME1XoEsTGogihNpw7UASZ-YDbm-DRfd0qxVq6Lbr4ANjDpwo2rzHlbTyNKW7tYTYd8jCIOHw2oNfGv6HhryFJQN1N",
                    "width": 3138
                }
            ],
            "place_id": "ChIJ9axumBapQjQRkLZyAZ2Ic1s",
            "plus_code": {
                "compound_code": "3G45+Q4 大同區 台北市",
                "global_code": "7QQ33G45+Q4"
            },
            "rating": 4.0,
            "reference": "ChIJ9axumBapQjQRkLZyAZ2Ic1s",
            "types": [
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 39
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "10491台灣台北市中山區新生北路二段68巷11-1號",
            "geometry": {
                "location": {
                    "lat": 25.056497,
                    "lng": 121.526841
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0579027799,
                        "lng": 121.5281928799
                    },
                    "southwest": {
                        "lat": 25.0552031201,
                        "lng": 121.5254932201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R492",
            "name": "玉琢精緻料理(預約制)台北美食 台北餐廳 中山區美食 台北精緻料理 台北油封鴨 台北中菜西吃",
            "opening_hours": {
                "open_now": false
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 4032,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/105796562277258798124\">A Google User</a>"
                    ],
                    "photo_reference": "ATtYBwKdzPVCy9_J0RciUdwfHFh8A4qosXad491dTdSFvocVyBK_4_bBE5p_QgmKUcoU_1lF0NvoeHl0-tEC8SoKmzp6I4YtHDZa7CFlPhEWPt2rpqGbGYsafC38iH6ck8Zu-521yDFOxKasefonWaF5yd939PmHff2OrBK5Z_YfbmX3C3Ws",
                    "width": 3024
                }
            ],
            "place_id": "ChIJtR8mJfapQjQR9t6JbJuOfng",
            "plus_code": {
                "compound_code": "3G4G+HP 中山區 台北市",
                "global_code": "7QQ33G4G+HP"
            },
            "price_level": null,
            "rating": 4.8,
            "reference": "ChIJtR8mJfapQjQR9t6JbJuOfng",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 46
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "108台灣台北市萬華區成都路10號",
            "geometry": {
                "location": {
                    "lat": 25.0420139,
                    "lng": 121.5068592
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0433517799,
                        "lng": 121.50809755
                    },
                    "southwest": {
                        "lat": 25.0406521201,
                        "lng": 121.50521295
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "id": "A1036",
            "name": "西門紅樓",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3120,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/113417895596279955279\">Nathalie Wu</a>"
                    ],
                    "photo_reference": "ATtYBwLOLlyAfZl4lIOfxidlbclchh6c-gMeFW_d6FVAS50V2bVZz7A8Amkfgwbg7OHbbah-gpnde7e9uiHnABQWKTL2DbNPai4Z38ANqe9MnMIsZwSylTBfeGsxHzkjUgEpARo9ql70C3JtkxMIh8YaqNeVLQin4NlnOcNau8a9_-Ep1asJ",
                    "width": 4208
                }
            ],
            "place_id": "ChIJi-yspAmpQjQRxcHc_lwnNHw",
            "plus_code": {
                "compound_code": "2GR4+RP 萬華區 台北市",
                "global_code": "7QQ32GR4+RP"
            },
            "rating": 4.2,
            "reference": "ChIJi-yspAmpQjQRxcHc_lwnNHw",
            "types": [
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 13328
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "108台灣台北市萬華區水源路199號",
            "geometry": {
                "location": {
                    "lat": 25.0221886,
                    "lng": 121.505779
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0231500299,
                        "lng": 121.5074411299
                    },
                    "southwest": {
                        "lat": 25.0204503701,
                        "lng": 121.5047414701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "id": "A1450",
            "name": "青年公園花鐘",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2250,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/100315628490112199127\">陳鶴文</a>"
                    ],
                    "photo_reference": "ATtYBwK59jbvCQkiU27aCJGjYF73-k3T5TpHGAp9VDIgo6Vn2o5DMOP9iX2AGijsjEL7EcueAV98rEJsvjVN1iU2YeRG-LUavSSr1_xsYvSr9f_SNlFanGNym2IdN8gxtOz7kwh2_os9ldnFm5slHFFsY4K7DYIN217_IKEsNrUn1SBZ7fv4",
                    "width": 4000
                }
            ],
            "place_id": "ChIJhSAzBrmpQjQR2wcuMKsg8cs",
            "plus_code": {
                "compound_code": "2GC4+V8 萬華區 台北市",
                "global_code": "7QQ32GC4+V8"
            },
            "rating": 4.3,
            "reference": "ChIJhSAzBrmpQjQR2wcuMKsg8cs",
            "types": [
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 103
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "105台灣台北市松山區饒河街221巷5號",
            "geometry": {
                "location": {
                    "lat": 25.0514224,
                    "lng": 121.5765095
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0527543799,
                        "lng": 121.5779126299
                    },
                    "southwest": {
                        "lat": 25.0500547201,
                        "lng": 121.5752129701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "id": "A364",
            "name": "饒河疏散門",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/100970506321156730713\">賴鼎富</a>"
                    ],
                    "photo_reference": "ATtYBwLun9Ib5zn3REluz6Rz3W6KSJ3KDxbWCub-5e3RYlHIcMYLmEoQNaI0YeTFJg0HrUbKgn6uHLlALyx966tkcDk7g0AyWA5Oze2wVZTQ-6joTreaL3dAIRE0ETGt-wocr4zGWcO7uRfXvgmZqCYlCvMxnClH6hsNV3kYzJWnBJll4Wvz",
                    "width": 4032
                }
            ],
            "place_id": "ChIJE3HAjJurQjQRuIsFiJj4ywA",
            "plus_code": {
                "compound_code": "3H2G+HJ 松山區 台北市",
                "global_code": "7QQ33H2G+HJ"
            },
            "rating": 4.0,
            "reference": "ChIJE3HAjJurQjQRuIsFiJj4ywA",
            "types": [
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 288
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "111台灣台北市士林區延平北路九段",
            "geometry": {
                "location": {
                    "lat": 25.1098485,
                    "lng": 121.4660588
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.1111983299,
                        "lng": 121.4674086299
                    },
                    "southwest": {
                        "lat": 25.1084986701,
                        "lng": 121.4647089701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png",
            "id": "A1209",
            "name": "社子島 島頭公園",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3456,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/103173756567963670186\">lehac Chen</a>"
                    ],
                    "photo_reference": "ATtYBwJSJjcXCkXQjHUtoYqCtQsO_Uhvl2-T1GeQEtytc9yhaXtzJ_9euYB4gP6R41hD8U4Wy0zjErzjPobURaZmyuHE4B4DvWHZxYJwjhW8dRZ5qjLXPkYXiNeZ1ltTmuO1Y91zOY79puqwc-EZem-x6jDCfO1RApPzVwGxAyFPPgSrsW8k",
                    "width": 4608
                }
            ],
            "place_id": "ChIJV69K-0CvQjQRAjNwXdEg8no",
            "plus_code": {
                "compound_code": "4F58+WC 士林區 台北市",
                "global_code": "7QQ34F58+WC"
            },
            "rating": 4.3,
            "reference": "ChIJV69K-0CvQjQRAjNwXdEg8no",
            "types": [
                "park",
                "tourist_attraction",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 2113
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "103台灣台北市大同區迪化街二段",
            "geometry": {
                "location": {
                    "lat": 25.0569163,
                    "lng": 121.5098405
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0582699799,
                        "lng": 121.5112261299
                    },
                    "southwest": {
                        "lat": 25.0555703201,
                        "lng": 121.5085264701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
            "id": "A1240",
            "name": "迪化老街--文化、商圈",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3792,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/112270222637970102617\">傅彥棠</a>"
                    ],
                    "photo_reference": "ATtYBwJL-hREE2jVyPagRz-yMUqKqccetF9OgtsQXX3hXFdLjrPPDKYZU9uKSgWzfLwfoGeXnKLunNXkqVmbbaq_9ELvrwTYZr4b-cXrHff4dqNeK4UuCVJ5vN0grZ5Js8CSKkHvaT4jh-HDzRwA7lXunNgMe_5DqoE8vIYWO8yDCAKBVED9",
                    "width": 5056
                }
            ],
            "place_id": "ChIJZXKGOBSpQjQRHko-EIytJMU",
            "plus_code": {
                "compound_code": "3G45+QW 大同區 台北市",
                "global_code": "7QQ33G45+QW"
            },
            "rating": 4.4,
            "reference": "ChIJZXKGOBSpQjQRHko-EIytJMU",
            "types": [
                "tourist_attraction",
                "grocery_or_supermarket",
                "food",
                "point_of_interest",
                "store",
                "establishment"
            ],
            "user_ratings_total": 112
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "Taipei Area, No. 83, No. 10漢口街二段 Wanhua Dist, 台北市台灣",
            "geometry": {
                "location": {
                    "lat": 25.045741,
                    "lng": 121.505741
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0471762299,
                        "lng": 121.5071119799
                    },
                    "southwest": {
                        "lat": 25.0444765701,
                        "lng": 121.5044123201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H827",
            "name": "Thetop Inn",
            "opening_hours": null,
            "permanently_closed": null,
            "photos": null,
            "place_id": "ChIJcf3O1Q6pQjQRRLgT5tG-CNs",
            "plus_code": {
                "compound_code": "2GW4+77 萬華區 台北市",
                "global_code": "7QQ32GW4+77"
            },
            "rating": 0.0,
            "reference": "ChIJcf3O1Q6pQjQRRLgT5tG-CNs",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 0
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "103台灣台北市大同區歸綏街182號",
            "geometry": {
                "location": {
                    "lat": 25.058066,
                    "lng": 121.512221
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0594690299,
                        "lng": 121.5135690799
                    },
                    "southwest": {
                        "lat": 25.0567693701,
                        "lng": 121.5108694201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H225",
            "name": "建山大旅社",
            "opening_hours": {
                "open_now": false
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3744,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/112526634484835537774\">建山大旅社</a>"
                    ],
                    "photo_reference": "ATtYBwInpOH7qASNSIkBT9JH9PEqX_bLhNe_j2utkFtFWrNeDnH7TRS1CX5FCNE6NRDQ99hxLX3lThV9A26oKXXt13J4viTf37vm1C9xlJW7IoOnSIDyDuCTXLOHu73CeF8qOBJgWVPzxZRD3KDUgsqeLfG3q0g3FRH5tEpXiB-M8x78pGwY",
                    "width": 5616
                }
            ],
            "place_id": "ChIJK9EFERWpQjQRTtdMuKkP-w4",
            "plus_code": {
                "compound_code": "3G56+6V 大同區 台北市",
                "global_code": "7QQ33G56+6V"
            },
            "rating": 4.3,
            "reference": "ChIJK9EFERWpQjQRTtdMuKkP-w4",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 160
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "1F, No, Taipei Area, No. 2忠孝東路三段217巷8弄大安區台北市台灣 104",
            "geometry": {
                "location": {
                    "lat": 25.0437249,
                    "lng": 121.5398737
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0451169299,
                        "lng": 121.5412226299
                    },
                    "southwest": {
                        "lat": 25.0424172701,
                        "lng": 121.5385229701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H146",
            "name": "Park 1st floor",
            "opening_hours": null,
            "permanently_closed": null,
            "photos": null,
            "place_id": "ChIJLTKqzNmrQjQR-rH9bMAL9zI",
            "plus_code": {
                "compound_code": "2GVQ+FW 大安區 台北市",
                "global_code": "7QQ32GVQ+FW"
            },
            "rating": 0.0,
            "reference": "ChIJLTKqzNmrQjQR-rH9bMAL9zI",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 0
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "No. 6, Lane 73, Chenggong Road Taipei Taipei Area, 台灣 241",
            "geometry": {
                "location": {
                    "lat": 25.051698,
                    "lng": 121.4892158
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0530017799,
                        "lng": 121.4905366799
                    },
                    "southwest": {
                        "lat": 25.0503021201,
                        "lng": 121.4878370201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H854",
            "name": "Love Hotel",
            "opening_hours": null,
            "permanently_closed": null,
            "photos": null,
            "place_id": "ChIJ65gFpv2oQjQRde4NlFFV8JM",
            "plus_code": {
                "compound_code": "3F2Q+MM 三重區 新北市",
                "global_code": "7QQ33F2Q+MM"
            },
            "rating": 5.0,
            "reference": "ChIJ65gFpv2oQjQRde4NlFFV8JM",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 2
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "100台灣台北市中正區延平南路9號",
            "geometry": {
                "location": {
                    "lat": 25.046323,
                    "lng": 121.5109236
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0476845799,
                        "lng": 121.5122208799
                    },
                    "southwest": {
                        "lat": 25.0449849201,
                        "lng": 121.5095212201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
            "id": "H917",
            "name": "力歐時尚旅館",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2048,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/106523129407354270436\">力歐時尚旅館 .</a>"
                    ],
                    "photo_reference": "ATtYBwLdff0pmL2x4y9Lw7lPNlzZv4JkHkS4my2rQOvjA080rLF1cpp7nEsJKQa6QpdPYPvdgHQFDPWwqZABgwQ1HiHfQP6SiQLXsdiUU_-iXcZDeckVayFEQ9I7HNI2HjW-NhRu_vhJA77zMn0tyYFfQFj0a6w13cwjRbVcPkruEKc84DZ2",
                    "width": 1370
                }
            ],
            "place_id": "ChIJSem5UAypQjQRBI9I-PqUb7Q",
            "plus_code": {
                "compound_code": "2GW6+G9 中正區 台北市",
                "global_code": "7QQ32GW6+G9"
            },
            "rating": 3.4,
            "reference": "ChIJSem5UAypQjQRBI9I-PqUb7Q",
            "types": [
                "lodging",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 268
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "110台灣台北市信義區松仁路28號6樓",
            "geometry": {
                "location": {
                    "lat": 25.039633,
                    "lng": 121.5678702
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0409828299,
                        "lng": 121.5692200299
                    },
                    "southwest": {
                        "lat": 25.0382831701,
                        "lng": 121.5665203701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R656",
            "name": "勞瑞斯牛肋排餐廳",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2736,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/105420929197092603369\">Pakerver Wong</a>"
                    ],
                    "photo_reference": "ATtYBwKeZ1PeK_9rNhwmGUAIiyapNS-3OcJvNjr5skoEPIKMMvd3gW1pEJfA2a9vZpKrmShuU67Bs_Gi2KLi3F0TGno2oYp_Nx2wGZy1K6hKqRCFb2UcjwUCBQDPgsOb63XR-eHzmZFxC3AnKulHgIk_DhKw4XK8c7H8Ju0RoEOhjdVA2SsD",
                    "width": 3648
                }
            ],
            "place_id": "ChIJjwfWf7CrQjQR8HEILkaBigk",
            "plus_code": {
                "compound_code": "2HQ9+V4 信義區 台北市",
                "global_code": "7QQ32HQ9+V4"
            },
            "price_level": 4.0,
            "rating": 4.3,
            "reference": "ChIJjwfWf7CrQjQR8HEILkaBigk",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 1824
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "100台灣台北市中正區館前路12號6樓",
            "geometry": {
                "location": {
                    "lat": 25.0456618,
                    "lng": 121.5147282
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0470095799,
                        "lng": 121.5162172799
                    },
                    "southwest": {
                        "lat": 25.0443099201,
                        "lng": 121.5135176201
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R771",
            "name": "欣葉日本料理-館前店",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2268,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/113704358283946906395\">陳啟展</a>"
                    ],
                    "photo_reference": "ATtYBwLsyoZ33lUAlm0pqfumgfr7xLCMV-XRreT2VYPbgrWINtMwCV_sxRKyi6uMGPkttLpONPwPVU8TS2LwdpeQ5EoSMIM7GpLdjxIB3QKFlLgh_64CyrqFbn6UmKJNhHlKXqqmyOLjwnfSO22l17ys9-BSHWo-rD9W6vNYo5bxCzxAYLY3",
                    "width": 4032
                }
            ],
            "place_id": "ChIJRXL_JXOpQjQRowS1Pdt1jVE",
            "plus_code": {
                "compound_code": "2GW7+7V 中正區 台北市",
                "global_code": "7QQ32GW7+7V"
            },
            "price_level": 3.0,
            "rating": 4.2,
            "reference": "ChIJRXL_JXOpQjQRowS1Pdt1jVE",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 4725
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "241台灣新北市三重區捷運路22巷14號",
            "geometry": {
                "location": {
                    "lat": 25.0551134,
                    "lng": 121.4848036
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0564729299,
                        "lng": 121.4861208299
                    },
                    "southwest": {
                        "lat": 25.0537732701,
                        "lng": 121.4834211701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R879",
            "name": "My Chef",
            "opening_hours": {
                "open_now": false
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 3024,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/116587227252376167995\">鄭文照</a>"
                    ],
                    "photo_reference": "ATtYBwJa7FtRL_Wz17cW6J2vzlQohaJM4ZgAT-tS2I4rKKxua54vM-wjMr4xSn30Qt_6tR7fMCV9G_ZWbLkwGZJysBfDiQR6__Tkn88WJVPdFd3-PaDo5_ZUWr0yK5ZzPwhSoO73NISd5QbkP-NWasUxmjcX_125uJKE-iNtGlh--KpzE6HD",
                    "width": 4032
                }
            ],
            "place_id": "ChIJ5wnAT_uoQjQREzR59ocmBTc",
            "plus_code": {
                "compound_code": "3F4M+2W 三重區 新北市",
                "global_code": "7QQ33F4M+2W"
            },
            "price_level": null,
            "rating": 4.8,
            "reference": "ChIJ5wnAT_uoQjQREzR59ocmBTc",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 12
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "114台灣台北市內湖區成功路三段162號7樓",
            "geometry": {
                "location": {
                    "lat": 25.080453,
                    "lng": 121.59016
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0818028299,
                        "lng": 121.5915098299
                    },
                    "southwest": {
                        "lat": 25.0791031701,
                        "lng": 121.5888101701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R89",
            "name": "蔬食鳳陪",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 2160,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/116246634742472223225\">A Google User</a>"
                    ],
                    "photo_reference": "ATtYBwJ8sCXQ3xwcxUyF3OzOXMiGQcovxgqW9-pKdG4kQKQ60jcdg6Fbp6yEBYTncOoLmS4sUQIqZxk8SB3856_VGqbWeh4osrrOMZy9URtQhK_XdUtYYkV42cum34LwibT-1RM9jT5pej2I8xbpItL1GfhkRqIUrckurvferl2sc61LWomq",
                    "width": 2880
                }
            ],
            "place_id": "ChIJH1M2u_KsQjQRYB0rjZReYrw",
            "plus_code": {
                "compound_code": "3HJR+53 內湖區 台北市",
                "global_code": "7QQ33HJR+53"
            },
            "price_level": null,
            "rating": 4.8,
            "reference": "ChIJH1M2u_KsQjQRYB0rjZReYrw",
            "types": [
                "lodging",
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 19
        },
        {
            "business_status": "OPERATIONAL",
            "formatted_address": "10462台灣台北市中山區樂群三路299號6樓",
            "geometry": {
                "location": {
                    "lat": 25.0827753,
                    "lng": 121.5591814
                },
                "viewport": {
                    "northeast": {
                        "lat": 25.0841251299,
                        "lng": 121.5605312299
                    },
                    "southwest": {
                        "lat": 25.0814254701,
                        "lng": 121.5578315701
                    }
                }
            },
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
            "id": "R464",
            "name": "Taïrroir",
            "opening_hours": {
                "open_now": true
            },
            "permanently_closed": null,
            "photos": [
                {
                    "height": 720,
                    "html_attributions": [
                        "<a href=\"https://maps.google.com/maps/contrib/107483383739091573879\">Ming Hong Lin</a>"
                    ],
                    "photo_reference": "ATtYBwIiXm5s5WX5uhXJJtMlUYLHrIOm5lLW0_1iv4WilhiyWOWLx74gM7P223PSkvpK72jNqYpHrPbXG7iSr3Da8JxJeWoAvo7w5ttzeMZ2hCZv22Ik0EMzMpyP42_XzPV41ixu5VkfCUcmM-5EKdnTxDPOu1oRHKowU_ujBxJ6WJ8Nt2dn",
                    "width": 960
                }
            ],
            "place_id": "ChIJIduw3BKsQjQR3Gkz01ZqB8s",
            "plus_code": {
                "compound_code": "3HM5+4M 中山區 台北市",
                "global_code": "7QQ33HM5+4M"
            },
            "price_level": null,
            "rating": 4.2,
            "reference": "ChIJIduw3BKsQjQR3Gkz01ZqB8s",
            "types": [
                "restaurant",
                "food",
                "point_of_interest",
                "establishment"
            ],
            "user_ratings_total": 1048
        }
    ],
    "schedule": [
        "R924",
        "A772",
        "R248",
        "H784",
        "R651",
        "A1302",
        "R492"
    ]
}
```

## Interface for Backend Planner
Input:
| Name | Type |
|-|-|
| n_days | int
| price_level | int; {0, 1, 2, 3, 4}
| outdoor | float; [0.0, 1.0]
| compactness | float; [0.0, 1.0]
| start_time | str
| back_time | str 
| place_ids | None or list(str); a list of `id`s
| schedule | None or list(str); a list of `id`s

If None is given for place_ids and schedule, the planner should generate a new plan. Otherwise, it may update the current plan.

Output:
tuple: (places, schedule)

* `places` is a list of `place` (the same as the format in the json file)
* `schedule` is a list of `id`s


You may refer the example return values above or the postman example for the format.
