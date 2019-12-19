# Gietro1818
Mise en ligne d'un site sur la débâcle du Giétro par les Archives de l'Etat du Valais.


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

#Pour réaliser ce site

Le CSS est réalisé à partir de Bootstrap: https://getbootstrap.com/

La frise chronologique a été adapté de : https://github.com/CodyHouse/horizontal-timeline

La visionneuse d'image est Mirador:https://projectmirador.org/

Le serveur d'image utilisé est Cantaloupe: https://cantaloupe-project.github.io/

