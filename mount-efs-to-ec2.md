# 

* Assign all efs mount target ids to one security group

* Allow NFS connection on that security group by going to EC2 Security Groups, choose the one assigned to all efs mount targets, and modify the inbound rules by inserting a new NFS rule

* Once done, proceed to the mounting guide available on aws efs window