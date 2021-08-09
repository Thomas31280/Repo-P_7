from .. import utils

script = utils.Process

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
