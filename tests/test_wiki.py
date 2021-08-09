from .. import utils

import wikipedia

script = utils.Process


#   Wiki_API :
#      - En cas de demande valide, on doit retrouver le dictionnaire attendu
#      - En cas de demande invalide, on doit retrouver le dictionnaire attendu

def test_wikipedia_API_Success(monkeypatch):

    expected_result = {'wiki_api_call': 'Ok',
                       'summary': 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.',
                       'url': 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'}

    summary = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris."
    page = "<WikipediaPage 'Cité Paradis'>"

    def mockreturn_summary(obj):
        return summary

    def mockreturn_page(obj):
        return page

    monkeypatch.setattr(wikipedia, 'summary', mockreturn_summary)
    monkeypatch.setattr(wikipedia, 'page', mockreturn_page)
    # REMARQUE : On a du créer la variable url_for_test, car il est IMPOSSIBLE de mocker ou de modifier
    # une variable locale. On a donc créé une structure conditionnelle dans le utils.py pour pouvoir
    # réaliser ce test.
    monkeypatch.setattr(utils, 'url_value_for_test',
                        'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis')

    assert script.wikipedia_API("10 Cité Paradis, 75010 Paris, France") == expected_result


def test_wikipedia_API_Fail(monkeypatch):

    expected_result = {'wiki_api_call': 'Failure'}

    summary = None
    page = None

    def mockreturn_summary(obj):
        return summary

    def mockreturn_page(obj):
        return page

    monkeypatch.setattr(wikipedia, 'summary', mockreturn_summary)
    monkeypatch.setattr(wikipedia, 'page', mockreturn_page)
    monkeypatch.setattr(utils, 'url_value_for_test', None)
    assert script.wikipedia_API("Recherche_Non_Valide_Pour_l'API") == expected_result
