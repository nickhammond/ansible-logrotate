import os
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def get_logrotate_d_log_files():
    """
    return a list of log files managed by logrotate
    as defined in playbook.yml
    """
    playbook_path = 'playbook.yml'

    with open(playbook_path) as y:
        playbook_yml = yaml.safe_load(y)

    log_files = []
    for play in playbook_yml:
        for role in play['roles']:
            for script in role['vars']['logrotate_scripts']:
                log_files.append(script['name'])

    return log_files


def test_logrotate_conf(host):
    for log_file in get_logrotate_d_log_files():
        logrotate_d_path = '/etc/logrotate.d/' + log_file
        cmd = host.run('logrotate -d "%s"', logrotate_d_path)
        assert cmd.stderr.find('error') == -1
