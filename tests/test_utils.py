from .. import utils

import googlemaps
import wikipedia

script = utils.Process

# Process:
#   Parser :
#      - Une phrase formulée de manière "conventionnelle" doit renvoyer seulement le lieu recherché

def test_parser():
    output = script.parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    assert output == "d'OpenClassrooms"
   
#   Google_maps_API :
#      - En cas de demande valide à l'API, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrtouver le dictionnaire attendu

def test_google_maps_API_Success(monkeypatch):
    
    result = {'maps_api_call': 'Ok', 'coordinates': {'lat': 48.8751155, 'lng': 2.3489782}, 
              'address': '10 Cité Paradis, 75010 Paris, France'}

    def mockreturn(obj):
        return result

    monkeypatch.setattr(script, 'google_maps_API', mockreturn)
    assert script.google_maps_API("d'OpenClassrooms") == result


def test_google_maps_API_Fail(monkeypatch):
    
    result = {'maps_api_call': 'Failure'}
    
    def mockreturn(obj):
        return result

    monkeypatch.setattr(script, 'google_maps_API', mockreturn)
    assert script.google_maps_API("") == result


#   Wiki_API :
#      - En cas de demande valide, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrouver le dictionnaire attendu

def test_wikipedia_API_Success(monkeypatch):
    
    result = {'wiki_api_call': 'Ok', 'summary': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.', 
              'url': 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'}

    def mockreturn(obj):
        return result

    monkeypatch.setattr(script, 'wikipedia_API', mockreturn)
    assert script.wikipedia_API("Cité Paradis") == result


def test_wikipedia_API_Fail(monkeypatch):
    
    result = {'wiki_api_call': 'Failure'}

    def mockreturn(obj):
        return result

    monkeypatch.setattr(script, 'wikipedia_API', mockreturn)
    assert script.wikipedia_API("") == result