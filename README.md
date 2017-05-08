# logrotate

![Build Status](https://travis-ci.org/nickhammond/ansible-logrotate.svg?branch=master)

Installs logrotate and provides an easy way to setup additional logrotate scripts by
specifying a list of directives.

## Requirements

None

## Role Variables

* **logrotate_conf_dir**: String defining the location of the directory containing the logrotate configuration files.

* **logrotate_scripts**: A list of logrotate scripts and the directives to use for the rotation.
    * name - The name of the script that goes into /etc/logrotate.d/
    * path - Path to point logrotate to for the log rotation
    * options - List of directives for logrotate, view the logrotate man page for specifics
    * scripts - Dict of scripts for logrotate (see Example below)
    
* **logrotate_replace_old_configurations**: Boolean defining whether to remove conflicting path configurations defined 
in configuration files not managed by this role.
<br><br>
E.g. if you define a configuration for managing `/var/log/kern.log`, you may find that this has done before in 
`/etc/logrotate.d/rsyslog` (along with configurations for a number of other log paths). Setting this variable to `true` 
in this case will remove the old configuration from `/var/log/kern.log`, whilst leaving the other configurations in 
`/var/log/rsyslog` unaltered.


## Dependencies

None

## Example Playbook

Setting up logrotate for additional Nginx logs, with postrotate script (assuming this role is located in `roles/logrotate`).

```
- role: logrotate
  logrotate_scripts:
    - name: nginx
      path: /var/log/nginx/*.log
      options:
        - weekly
        - size 25M
        - rotate 7
        - missingok
        - compress
        - delaycompress
        - copytruncate
      scripts:
        postrotate: "[ -s /run/nginx.pid ] && kill -USR1 `cat /run/nginx.pid`"
```

## License

[BSD](https://raw.githubusercontent.com/nickhammond/logrotate/master/LICENSE)

## Author Information

* [nickhammond](https://github.com/nickhammond) | [www](http://www.nickhammond.com) | [twitter](http://twitter.com/nickhammond)
* [bigjust](https://github.com/bigjust)
* [steenzout](https://github.com/steenzout)
* [jeancornic](https://github.com/jeancornic)
* [duhast](https://github.com/duhast)
* [kagux](https://github.com/kagux)
