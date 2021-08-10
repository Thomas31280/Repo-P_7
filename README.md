### PRESENTATION ET OBJECTIFS DE L'APPLICATION

GrandPy bot est une application web qui repose sur le framework Flask. Le programme s'articule autours d'une architecture MVT, et doit être hébergé
sur un serveur Heroku. Les parties dynamiques du template sont gérées par jQuery.AJAX ( en JS donc ), le template utilise le framework CSS Bootstrap4,
et les tests unitaires sont réalisés avec la librairie pytest. Enfin, les informations relatives à la géolocalisation aux informations sur le lieu
sont obtenues par l'utilisation des API Wikipedia et GoogleMaps.

L'application a pour objectif de proposer à l'utilisateur un service qui lui permet, pour un lieu donné, d'obtenir l'adresse de ce lieu, un point GPS,
une description et un lien vers une page web wikipedia qui lui permet d'en apprendre plus sur le lieu. L'interaction avec le programme se fait via une
chatbox, et l'utilisateur utilise le programme directement dans son browser. Aucun hitorique n'est conservé.

---

### PREREQUIS

Pour exécuter convenablement le programme, il faut préparer l'environnement pour que tout se passe correctement. Il faut donc :

* Cloner le repo GitHub du projet, ce qui est soit faisable en faisant un téléchargement manuel depuis GitHub, soit en utilisant **Git Bash** ( les
procédures de clonnage sont facilement trouvables sur google ).

* Initialiser un environnement virtuel ( avec **Virtual Env** par exemple ). Dans ce cas, il vous faudra créer votre environnement virtuel avec
**Python 3** dessus, puis l'activer. Selon que vous soyez sous Windows, MacOS ou Linux, les procédures changent légèrement. Là encore, elles sont très
facilement trouvables sur Google.

* Pour éxecuter le programme, il est enfin nécessaire d'installer les librairies requises. Pour cela, on peut tout simplement utiliser _PIP_ pour
installer toutes les librairies qui figurent dans le **requirements.txt**, via la commande _pip install * requirements.txt_. Cette commande est
à exécuter à la racine du projet, en ayant bien son environnement virtuel activé !!!

---

### EXECUTION DU PROGRAMME

Après avoir installé les librairies, il faudra se rendre dans le module **config.py** à la racine du projet, et entrer la valeur de votre clé d'API 
GoogleMaps pour la variable *MAPS_API_KEY =*  ( notez que le type de donnée doit être une string ). Ensuite, exécutez la commande python _views.py_ 
dans votre console à la racine du projet ( sous windows ). _Flask_ utilisera alors son serveur de développement intégré pour vous proposer une URL sur 
le port 5000 par défaut ( typiquement de type _http://127.0.0.1:5000/_ ). Vous pourrez alors accéder à l'interface utilisateur en suivant cette URL.

---

### EXECUTION DES TESTS

Si vous souhaitez lancer les tests, il vous faudra exécuter la commande _python -m pytest tests/_ à la racine du projet. En effet, si vous exécutez
simplement la commande "pytest", le module pytest vous renverra une erreur relative à l'importation des modules. La raison est que dans ce cas, pytest
n'ajoute pas le répertoire courant dans la variable d'environnement **PYTHONPATH** lui-même, ce qui conduit à des erreurs lors de l'importation de modules.
Tandis que si vous utilisez la commande _python -m pytest tests/_, Python ajoute le répertoire actuel dans le **PYTHONPATH**.