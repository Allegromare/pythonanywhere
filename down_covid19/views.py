from django.shortcuts import render
from . import downloadDataCovid

# Create your views here.


def index(request):
    nuovi_positivi = downloadDataCovid.download_nuovi_positivi_ita_json()
    return render(
        request, "down_covid19/index.html", {"nuovi_positivi": nuovi_positivi}
    )
