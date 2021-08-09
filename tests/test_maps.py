from .. import utils
from .. import config

script = utils.Process
gmaps = utils.gmaps

#   Google_maps_API :
#      - En cas de demande valide à l'API, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrtouver le dictionnaire attendu


def test_google_maps_API_Success(monkeypatch):

    expected_result = {'maps_api_call': 'Ok',
                       'coordinates': {'lat': 48.8751155, 'lng': 2.3489782},
                       'address': '10 Cité Paradis, 75010 Paris, France'}

    def mockreturn(obj):
        return config.MOCK_MAPS_RESULT

    monkeypatch.setattr(gmaps, 'geocode', mockreturn)
    assert script.google_maps_API("d'openclassrooms") == expected_result


def test_google_maps_API_Fail(monkeypatch):

    expected_result = {"maps_api_call": 'Failure'}

    api_result = []

    def mockreturn(obj):
        return api_result

    monkeypatch.setattr(gmaps, 'geocode', mockreturn)
    assert script.google_maps_API("Adresse_non_valide") == expected_result
