import jenkins.model.*
import hudson.model.*
import hudson.tools.*
import hudson.plugins.toolenv.*
import hudson.model.JDK

def jenkins = Jenkins.getInstance()
def jdkConfig = jenkins.getDescriptorByType(hudson.model.JDK.DescriptorImpl.class)

// Configuration des versions à installer
def versions = [
        [name: "Corretto-11", version: "11.0.21.9.1"],
        [name: "Corretto-17", version: "17.0.9.8.1"]
]

def jdkList = []

versions.each { v ->
    // URL officielle AWS Corretto pour Linux x64 (.tar.gz)
    def downloadUrl = "https://corretto.aws/downloads/resources/${v.version}/amazon-corretto-${v.version}-linux-x64.tar.gz"

    // Définition de l'installateur par archive binaire
    def installer = new ZipExtractionInstaller(null, downloadUrl, "amazon-corretto-${v.version}-linux-x64")
    def installSource = new InstallSourceProperty([installer])

    // Association du JAVA_HOME
    def javaHome = "${jenkins.getRootDir().absolutePath}/tools/hudson.model.JDK/${v.name}/amazon-corretto-${v.version}-linux-x64"

    // Création de l'objet JDK
    def jdk = new JDK(v.name, javaHome, [installSource])
    jdkList << jdk
    println "SUCCESS: Configuration préparée pour ${v.name} avec JAVA_HOME=${javaHome}"
}

// Application de la configuration à Jenkins
jdkConfig.setInstallations(jdkList.toArray(new JDK[0]))
jenkins.save()

println "REMARQUE: Jenkins téléchargera les JDK lors de leur première utilisation dans un pipeline."