
* To check all the disks that are attached to this machine

```bash
lsblk
```

* To check if any data is inside that volume

```bash
file -s /dev/xvdf
```

* Format the device (for linux systems, we want to format to `ext4`)

```bash
mkfs -t ext4 /dev/xvdf
```

* Create a mounting location by creating a new directory

```bash
mkdir data # you can choose whichever name you want, min is 'data'
```

* Mount the device to this location by 

```bash
sudo mount /dev/xvdf data/
```

* Change the permissions of your disk to, for example, everyone

```bash
sudo chmod 777 -R data # 777 means full access to everyone
```

* Write some new file inside your new storage

```bash
touch data/text.txt
echo "welcome to the aws course" > data/text.txt
```

* To unmount the device from the machine, type

```bash
sudo umount data
```

## Automount ebs volumes on boot

* make a backup of /etc/fstab file

```bash
cp /etc/fstab /etc/fstab.bak
```

* modify the file (with any text editor available in-place: vim or nano) by adding a new line to this file

```
/dev/xvdf   /home/ubuntu/data   ext4    defaults    0   0
```

* Save and close

* Run the command `sudo mount -a`

* If there is no error, then it's good. Reboot the machine to see the effect.