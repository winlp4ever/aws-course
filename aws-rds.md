# RDS

## Database services of AWS

Hot topics: RDS - DynamoDB - ElastiCache - Amazon Redshift

## To remember

* RDS runs on virtual machines (you cannot ssh to your rds instances)
* You cannot log in to these operating systems however
* Patching of the RDS Operating System and DB is Amazon's responsibility
* RDS is not serverless
* except Aurora serverless

__What is serverless?__
Serverless is the native architecture of the cloud that enables you to shift more of your operational responsibilities to AWS, increasing your agility and innovation. Serverless allows you to build and run applications and services without thinking about servers. It eliminates infrastructure management tasks such as server or cluster provisioning, patching, operating system maintenance, and capacity provisioning. You can build them for nearly any type of application or backend service, and everything required to run and scale your application with high availability is handled for you.

## Back-ups

* Automated Backups
* Manual Snapshots

__Automated Backups__ are enabled by default. the bakup data is stored in S3 and you get free storage space equal to the size of the database.

__DB Snapshots__ are done manually (ie the are user initiated.) They are stored even after you delete the original RDS instance, unlike automated backups.

__Attention!:__ Whenever you restore either an Automatic Backup or a manual Snapshot, the restored version of the database will be a new RDS instance with a new DNS endpoint.

__Encryption At Rest:__ Encryption at rest is supported for MySQL, Oracle, SQL Server, PostgreSQL, MariaDB & Aurora. Encryption is done using the AWS KMS service. Once your RDS instance is encrypted, the data stored at rest in the underlying storage is encrypted, as are its automated backups, read replicas, and snapshots.

__Multi-AZ:__ Your db is replicated across different AZs. Every written operations will be auto synchronized to the stand by db. In the event of an AZ failure, RDS will auto failover to the standby so that db operations can resume quickly without administrative intervention. Available for:
* SQL Server
* Oracle
* MySQL Server
* PostgreSQL
* MariaDB

__Multi-AZ__ is for Disaster Recovery, while __Read Replicas__ is for Performance Improvement.

__Read Replicas:__ Db is replicated and asynchronously updated between different AZs so that different EC2s may link to different Dbs to allow a better performance. (Attention - only your primary database can be written into, other (replica) dbs are read-only (why the name _Read Replica_), so actually this is only useful for read-heavy databases.) Things to know:
* Each read replica will have its own DNS end point.
* You can have read replicas that have multi-AZ.
* You can create read replicas of Multi-AZ source databases.
* Read replicas can be promoted to be their own databases. This breaks the replication.
* You can have a read replica in a second region.

## Lab

_ Create a database 

_ Access the database via command: `psql --username admin --password --hostname <db-dns-endpoint> --port=<db-port>`

_ Play with the database