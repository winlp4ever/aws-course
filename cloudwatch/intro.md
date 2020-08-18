# How to install and run
To install on an ubuntu machine, download the `deb package`

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a start # use stop to stop
# or you can use
sudo service amazon-cloudwatch-agent start # but this won't display the errors in case the service failed to start
```

The name of the configuration file must be
```
/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

An example of configuration file

```
{
	"agent": {
		"metrics_collection_interval": 60,
		"run_as_user": "cwagent",
		"credentials_path":"/home/cwagent/.aws/credentials"
	},
	"logs": {
		"logs_collected": {
			"files": {
				"collect_list": [
					{
						"file_path": "/var/log/syslog",
						"log_group_name": "foundeo-web",
						"log_stream_name": "{hostname}/syslog",
						"timestamp_format" :"%b %d %H:%M:%S"
					}
                                ]
                        }
               }
       }
}
```


