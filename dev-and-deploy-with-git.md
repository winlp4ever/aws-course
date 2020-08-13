# How to develop and deploy on a remote machine (EC2)

The best way is via Git!!!

1. Go to your github page and create a repo

2. Register the remote repo with your local repo by typing: 

```bash
git remote add origin https://github.com/your-username/your-repo
```

3. Do the first commit and push
```bash
git add .
git commit -m 'first commit'
git push -u origin master
```

4. Connect to the EC2 machine

5. Clone the github repo you have created

```bash
git clone https://github.com/your-username/your-repo
cd your-repo
```

6. Now every time you make some changes to your code inside the local machine, you can commit and push it to github, 
and use `git pull origin master` to update your remote machine's code

That's how you can develop on your local machine and deploy on an EC2 machine (or a remote machine in general)