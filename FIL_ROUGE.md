# Projet fil-rouge

## Cahier des charges du fil-rouge
Le societe DataMine veut mettre dans une chaine CI/CD utilisant Jenkins son developpement 
de produit informatique qui est, pour le moment, une application Python Flask de type data mining utilisant la librairie Pandas de Python .
Vous devez completer le projet github existant, en precisant votre demarche pour porter ce projet dans la chaine ci/cd.   

**Etapes:**  
* Etudier le projet suivant   
  **https://github.com/app-generator/sample-flask-pandas-dataframe.git**  
  Faire un fork de toutes les branches dans votre repo perso github  
  etudiez le projet le fichier README.md, la partie setup.   
  Faire une clone de votre projet forke dans votre directory de travail sur votre laptop et 
  dans la vm google.
* Faire fonctionner, en ligne de commande,  le projet dans un shell, precisez les commandes necessaires pour realiser ca dans un fichier **flask_pandas.md**, l'application flask doit etre accessible par l'adresse publique gcp google et par le **port 31201**. Lire correctement le fichier README du projet pour trouver les commandes necessaires. Faire regulierement des git commit, push pour enregister votre projet
* dans le projet, ecrire un fichier **Dockerfile** pour conteneuriser cette application (pensez a faire git commit, push) 
* en dehors de jenkins, sur votre vm google, creez une image **flask-panda**. Mettre l'image dans le repository docker hub 
* en dehors de jenkins, sur votre vm google,  faire une docker run et verifier que l'application est disponible sur le port 31201.
* dans jenkins creez un job **flask-panda-jmeter**, creer un test plan pour verifier si l'application affiche des data.
* chainer les jobs jenkins pour faire un pipeline graphique
* mettre a jour le jenkins plugin de goland pour lancer des build depuis votre IDE goland
* mettre un webhook dans votre projet github, pour demarrer automatiquement votre ci/cd a chaque commit.
