# Use ORACLE database 

## Install Oracle 18c instance
```shell
docker  volume create dboracle
docker run -d -p 11521:1521 -p 15500:5500 --name oracle -e ORACLE_PWD=oracle -v dboracle:/opt/oracle/oradata systemdevformations/oracle-tpcds
```
## Set up TPC-DS database 
```oracle
-- go to Toad
CREATE TABLESPACE TBS_PERM_TPCDS
    DATAFILE
    '/opt/oracle/oradata/XE/XEPDB1/users02.dbf' SIZE 2G AUTOEXTEND ON NEXT 100M MAXSIZE UNLIMITED
    LOGGING
    DEFAULT
    NO INMEMORY
    ONLINE
    EXTENT MANAGEMENT LOCAL AUTOALLOCATE
    BLOCKSIZE 8K
    SEGMENT SPACE MANAGEMENT AUTO
    FLASHBACK ON;
/
CREATE TEMPORARY TABLESPACE TBS_TEMP_TPCDS
    TEMPFILE
    '/opt/oracle/oradata/XE/XEPDB1/users03.dat' SIZE 200M AUTOEXTEND ON NEXT 100M MAXSIZE UNLIMITED
    TABLESPACE GROUP ''
    EXTENT MANAGEMENT LOCAL UNIFORM SIZE 1M
FLASHBACK ON;

    
    
    
```
