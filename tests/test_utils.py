from .. import utils
from .. import config

import googlemaps
import wikipedia

script = utils.Process
gmaps = utils.gmaps


# Process:
#   Parser :
#      - Une phrase formulée de manière "conventionnelle" doit renvoyer seulement le lieu recherché
#      - Vérifier qu'une phrase composée uniquement de mots contenus dans le Stop_Word ne renvoie rien
#      - Vérifier que les caractères majuscules n'ont pas d'incidence sur le traitement du stopword

def test_parser_classic():
    output = script.parser("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    assert output == "d'openclassrooms"

def test_parser_stop_word():
    output = script.parser("Je pense donc je suis !")
    assert output == ''

def test_parser_capital_letters():
    output = script.parser("SaLUt GRAndpY ! eSt-CE que Tu cONnaiS l'AdreSSe D'oPEnclASsRooMS ?")
    assert output == "d'openclassrooms"

#   Google_maps_API :
#      - En cas de demande valide à l'API, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrtouver le dictionnaire attendu

def test_google_maps_API_Success(monkeypatch):

    expected_result = {'maps_api_call': 'Ok', 'coordinates': {'lat': 48.8751155, 'lng': 2.3489782}, 
                       'address': '10 Cité Paradis, 75010 Paris, France'}
    
    api_result = [{'address_components': [{'long_name': '10', 'short_name': '10', 'types': ['street_number']}, 
                    {'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis', 'types': ['route']}, 
                    {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 
                     'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, 
                    {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, 
                    {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75010', 'short_name': '75010', 'types': ['postal_code']}], 
                     'formatted_address': '10 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8751155, 'lng': 2.3489782}, 'location_type': 'ROOFTOP', 
                     'viewport': {'northeast': {'lat': 48.8764644802915, 'lng': 2.350327180291502}, 'southwest': {'lat': 48.8737665197085, 'lng': 2.347629219708498}}}, 
                     'partial_match': True, 'place_id': 'ChIJLUzI3xRu5kcRX7qwoQiY5bM', 'plus_code': {'compound_code': 'V8GX+2H Paris, France', 'global_code': '8FW4V8GX+2H'}, 
                     'types': ['electronics_store', 'establishment', 'home_goods_store', 'point_of_interest', 'store']}]


    def mockreturn(obj):
        return api_result

    monkeypatch.setattr(gmaps, 'geocode', mockreturn)
    assert script.google_maps_API("d'openclassrooms") == expected_result



def test_google_maps_API_Fail(monkeypatch):

    expected_result = {"maps_api_call": 'Failure'}

    api_result = []


    def mockreturn(obj):
        return api_result

    monkeypatch.setattr(gmaps, 'geocode', mockreturn)
    assert script.google_maps_API("Adresse_non_valide_pour_l'api") == expected_result


#   Wiki_API :
#      - En cas de demande valide, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrouver le dictionnaire attendu

def test_wikipedia_API_Success(monkeypatch):
    
    expected_result = {'wiki_api_call': 'Ok', 'summary': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.', 
              'url': 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'}

    summary = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris."
    page = "<WikipediaPage 'Cité Paradis'>"
    url_to_the_page = 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'


    def mockreturn_summary(obj):
        return summary
    
    def mockreturn_page(obj):
        return page
    
    
    monkeypatch.setattr(wikipedia, 'summary', mockreturn_summary)
    monkeypatch.setattr(wikipedia, 'page', mockreturn_page)
    # REMARQUE : On a du créer la variable url_for_test, car il est IMPOSSIBLE de mocker ou de modifier
    # une variable locale. On a donc créé une structure conditionnelle dans le utils.py pour pouvoir
    # réaliser ce test.
    monkeypatch.setattr(utils, 'url_value_for_test', 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis')
    assert script.wikipedia_API("10 Cité Paradis, 75010 Paris, France") == expected_result


def test_wikipedia_API_Fail(monkeypatch):
    
    expected_result = {'wiki_api_call': 'Failure'}

    summary = None
    page = None
    url_to_the_page = None


    def mockreturn_summary(obj):
        return summary
    
    def mockreturn_page(obj):
        return page
    
    
    monkeypatch.setattr(wikipedia, 'summary', mockreturn_summary)
    monkeypatch.setattr(wikipedia, 'page', mockreturn_page)
    monkeypatch.setattr(utils, 'url_value_for_test', None)
    assert script.wikipedia_API("Recherche_Non_Valide_Pour_l'API") == expected_result