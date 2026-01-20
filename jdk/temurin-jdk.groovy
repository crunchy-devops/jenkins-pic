#!/usr/bin/env groovy
import hudson.model.JDK
import hudson.tools.InstallSourceProperty
import io.jenkins.plugins.adoptopenjdk.AdoptOpenJDKInstaller
import jenkins.model.Jenkins

final versions = [
        'jdk8' : 'jdk8u452-b09',
        'jdk11': 'jdk-11.0.27+6',
        'jdk17': 'jdk-17.0.15+6',
        'jdk21': 'jdk-21.0.7+6',
]

Jenkins.instance.getDescriptor(hudson.model.JDK).with {
    installations = versions.collect {
        new JDK(it.key, '', [
                new InstallSourceProperty([
                        new AdoptOpenJDKInstaller(it.value)
                ])
        ])
    } as JDK[]

}