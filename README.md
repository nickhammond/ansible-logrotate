# logrotate

[![Build Status](https://travis-ci.org/nickhammond/ansible-logrotate.svg?branch=master)](https://travis-ci.org/nickhammond/ansible-logrotate)

Installs logrotate and provides an easy way to setup additional logrotate scripts by
specifying a list of directives.

## Requirements

None

## Role Variables

**logrotate_scripts**: A list of logrotate scripts and the directives to use for the rotation.

* name - The name of the script that goes into /etc/logrotate.d/
* path - Path to point logrotate to for the log rotation
* options - List of directives for logrotate, view the logrotate man page for specifics
* scripts - Dict of scripts for logrotate (see Example below)

```
logrotate_scripts:
  - name: rails
    path: "/srv/current/log/*.log"
    options:
      - weekly
      - size 25M
      - missingok
      - compress
      - delaycompress
      - copytruncate
```

## Dependencies

None

## Example Playbook

Setting up logrotate for additional Nginx logs, with postrotate script.

```
- hosts: all
  vars:
    logrotate_scripts:
      - name: nginx-options
        path: /var/log/nginx/options.log
        options:
          - daily
          - weekly
          - size 25M
          - rotate 7
          - missingok
          - compress
          - delaycompress
          - copytruncate

      - name: nginx-scripts
        path: /var/log/nginx/scripts.log
        options:
          - daily
          - weekly
          - size 25M
        scripts:
          postrotate: "echo test"

  roles:
    - ansible-logrotate
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
