# 1. Import libraries
from pkg_resources import parse_version
import requests, json

URL_COVID_ITALIA_JSON = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"


def download_nuovi_positivi_ita_json():
    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA_JSON)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:
        responseJson = response.json()

        for record in responseJson:
            nuovi_positivi_inverso[record["data"][:10]] = record["nuovi_positivi"]

            # print(record["data"][:10] + " " + str(record["nuovi_positivi"]))

        nuovi_positivi = dict(reversed(list(nuovi_positivi_inverso.items())))

        # print(nuovi_positivi)
    return nuovi_positivi
