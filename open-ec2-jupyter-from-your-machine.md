## Make your jupyter notebook accessible

* Modify security groups of your EC2 Instance:

Search for `security groups` in the bottom info panel on ec2 console, click the group name -> click group id -> edit inbound rules -> add port 8000

* Go to your ec2 machine. Type `jupyter notebook --generate-config`

* Add these lines to the file:

conf = get_config()
conf.NotebookApp.ip = '0.0.0.0'
conf.NotebookApp.port = 8000 # this is up to you

* Now run `jupyter notebook`. Copy the token part in the url that shows up:

Normally, the url looks like this: `http://127.0.0.1:8000/?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`. Copy the sub string from `?token` to the end.

* Open `your-machine-public-ip:8000/<copy-paste-the-token-part-here>` (replace the port by the number you chose in config file), for example, the link will looks like this:

`33.15.79.128:8000/?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`