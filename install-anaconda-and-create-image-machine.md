# Install Anaconda and create your own ec2 machine image

* Install anaconda on ec2 ubuntu machine:
```python
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
chmod +x Anaconda3-2020.02-Linux-x86_64.sh
./Anaconda3-2020.02-Linux-x86_64.sh
```

* Keep pushing enter to skip through the whole terms & agreements parts
* enter 'yes' for the other yes/no questions popping up in the installation process
* once done, type `conda`  to see if the command is recognized. If not, run
```bash
export PATH=$PATH:/home/ubuntu/anaconda3/bin
```
and now the `conda` command should work

* Go to ec2 instances dashboard, tick the machine that you've installed anaconda3 inside, then choose __Actions__ => __Image__ => __Create Image__.

* A window should pop-up that asks you for the name, the description and how much storage for your machine. Enter all the information and click __Create Image__

* Your image is now being created. To check the status, click __AMIs__ in the left panel

* If the status is _available_, then tick the image and click launch

* You don't need anymore to specify what ami (because it's your own ami), but you have to reconfigure all the other steps the same like before

* Once done and launched, the new machine will be paired with all the packages and data like the old one.