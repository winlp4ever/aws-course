# Install a simple web server on an ec2 machine

* 1st step: Run all the following commands:

```bash
sudo apt-get install apache2 -y
sudo systemctl status apache2
sudo chmod 777 -R /var/www/html
echo '<html><body>hello world!</body></html>' > /var/www/html/index.html 
cat /var/www/html/index.html 
```

* 2nd step: Configure security groups

    * Go to EC2 console, open `instances` window
    * Tick the machine that you want to change security groups settings
    * In the bottom panel, a lot of informations will appear, search for `security groups`
    * Click the security group name
    * You will be redirected to security groups windows, again clicking the security group _id_
    * Click `Change inbound rules`
    * Add new line: Choose http as protocol, `0.0.0.0/0` as source
    * Click save
    * Reopen the ipv4 address of your ec2 machine, this time the page wil be loaded

## Create a small python server

* Create a folder on your ec2 machine, named, for ex, `python-server`

```bash
mkdir python-server # create a folder
cd python-server # go to the new folder
```

* Create an `index.html` file with this content:

```html
<html>
<body>
    hello world!
</body>
</html>
```

You can do with `vim` or `nano` or a simple `echo` command like before (`echo '<html><body>sthg</body></html>' > index.html`)
* Create a python file named `server.py` with this content:

```python
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
```

* Run `python server.py`
* Go to address `<your-machine-ipv4>:8080` to see the result

> In case you want to copy files from your local machine to aws ec2 machine, you can use `scp`

> ```scp -i <your-key-pem-file>.pem -rp /path/to/python/folder ubuntu@<ipv4-or-dns-of-your-ec2-machine>:/home/ubuntu```