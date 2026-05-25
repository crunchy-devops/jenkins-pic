# SonarQube

## reset admin password
# inside the postgresql container
``shell
psql -U bn_sonarqube -d bitnami_sonarqube
update users set crypted_password='100000$t2h8AtNs1AlCHuLobDjHQTn9XppwTIx88UjqUm4s8RsfTuXQHSd/fpFexAnewwPsO6jGFQUv/24DnO55hY6Xew==', salt='k9x9eN127/3e/hf38iNiKwVfaVk=', hash_method='PBKDF2', reset_password=TRUE, user_local=TRUE where login='admin';
```