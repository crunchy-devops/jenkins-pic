# Ecrire un Jenkinsfile

Avant d'écrire une seule ligne, comprenez pourquoi nous faisons cela.
Versionnage : Le fichier Jenkinsfile vit dans votre dépôt Git, à côté de votre code source.
Reproductibilité : N'importe qui peut relancer le build sans configuration manuelle dans l'interface graphique.
Transparence : Tout le processus de déploiement est visible et auditable.
Le choix professionnel : Nous utiliserons la syntaxe Declarative Pipeline (et non "Scripted"). 
C'est le standard moderne, plus lisible et doté de meilleures fonctionnalités de validation.

## L'Anatomie d'un Pipeline Parfait
Un Jenkinsfile professionnel ne se contente pas d'enchaîner des commandes shell. 
Il est structuré pour gérer l'imprévu. Voici le squelette type :
```jenkinsfile
pipeline {
    agent any // Ou un agent Docker spécifique
    options { 
        // Configuration globale (timeouts, logs...)
    }
    environment {
        // Variables globales
    }
    stages {
        // Le flux de travail principal
    }
    post {
        // Gestion des notifications et nettoyages
    }
}
```



