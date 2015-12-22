#!/usr/bin/python
import os
import sys


def print_zone(zone_name, master_ip):
    return """
zone "{}" {{
  type slave;
  file "/var/cache/bind/db.{}";
  masters {{ {}; }};
}};

""".format(zone_name, zone_name, master_ip)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("usage: {} command-to-run args".format(sys.argv[0]))

    zone_names = os.environ['ZONE_NAMES'].split()
    master_ip = os.environ['MASTER_IP']

    with open('/etc/bind/named.conf.local', 'w') as conf_fh:
        for zone_name in zone_names:
            conf_fh.write(print_zone(zone_name, master_ip))

    os.execvp(sys.argv[1], sys.argv[1:])
