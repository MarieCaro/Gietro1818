# Gietro1818
Mise en ligne d'un site sur la débâcle du Giétro dans le cadre du stage obligatoire de M2 TNAH de l'Ecole des Chartes aux Archives de l'Etat du Valais.
Sous la direction de MM. Clérice et Dubois.

## Comment installer le site ?

L’ensemble de l’application créée est à cloner de Github.
`git clone « https://github.com/MarieCaro/Gietro1818.git »`

Installer les requirements
`pip install -r requirements.txt`

Pour lancer l’application, taper les commandes
```FLASK_APP=code.py```
```flask run```

## Comment installer le serveur d’image et le serveur de manifeste ?

Pour faire fonctionner l’API des images, il faut télécharger Cantaloupe et suivre les directives pour son installation. Vous trouverez les informations ici sur leur site: https://cantaloupe-project.github.io/

Il faut ensuite mettre les images qui sont dans le dossier « Images » à l’intérieur de dossier Cantaloupe.

Dans le terminal, déplacez-vous dans le dossier Cantaloupe.
Activer le serveur d’image avec la commande :
`java -Dcantaloupe.config=/path/to/cantaloupe.properties -Xmx2g -jar cantaloupe-x.x.x.war`

Dans un nouveau terminal déplacez-vous dans le dossier Gietro1818/app/manifest.
Activer le serveur de présentation avec la ligne de commande :
`python server.py`

Au vu du nombre d’images qui sera mise en ligne, j’ai fait une petite sélection qui sert d’exemple à ce que sera le site.
Pour voir une image pour une personne, rendez-vous sur la page de la notice d’Ignace Venetz
Pour ouvrir un document d’archive, la note de bas de page de la page « Course contre la montre »
