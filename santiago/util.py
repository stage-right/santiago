from cmd import Cmd
from sys import argv

import santiago

def make_droplet(name, size, image, region,
                ssh_key_ids=None, virtio=True, private_networking=False,
                backups_enabled=False, user_data=None, ipv6=False):
    droplet = {
        'name': str(name),
        'size': str(size),
        'image': str(image),
        'region': str(region),
        'virtio': str(virtio).lower(),
        'ipv6': str(ipv6).lower(),
        'private_networking': str(private_networking).lower(),
        'backups': str(backups_enabled).lower(),
    }

    if user_data: droplet['user_data'] = user_data
    if ssh_key_ids: droplet['ssh_keys'] = ssh_key_ids.split(",")

    return droplet

def make_domain(name, ip):
    return {"name": name, "ip_address": ip}

def make_record(record_type, data, name=None, priority=None, port=None, weight=None):
    record = {'data': data, 'type': record_type}

    if name: record['name'] = name
    if priority: record['priority'] = priority
    if port: record['port'] = port
    if weight: record['weight'] = weight

    return record

class DomainRecordCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_domain_records(*args.split(" ")))
    def do_create(self, args):
        record_args = args.split(" ")[1:-1]
        print(santiago.new_domain_record(args.split(" ")[0], make_record(*record_args), args.split(" ")[-1]))
    def do_delete(self, args):
        print(santiago.destroy_domain_record(*args.split(" ")))

class DomainCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_domains(args))
    def do_create(self, args):
        domain_args = args.split(" ")[:-1]
        print(santiago.new_domain(make_domain(*domain_args), args.split(" ")[-1]))
    def do_record(self, args):
        DomainRecordCmd().onecmd(args)

class DropletCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_droplets(args))
    def do_create(self, args):
        droplet_args = args.split(" ")[:-1]
        print(santiago.new_droplet(make_droplet(*droplet_args), args.split(" ")[-1]))
    def do_delete(self, args):
        print(santiago.destroy_droplet(*args.split(" ")))

class SantiagoCmd(Cmd):
    def do_quit(self, args):
        raise SystemExit
    def do_droplet(self, args):
        DropletCmd().onecmd(args)
    def do_domain(self, args):
        DomainCmd().onecmd(args)

def main(args=None):
    shell = SantiagoCmd()
    shell.prompt = '> '
    if len(argv) == 1:
        shell.cmdloop()
    else:
        shell.onecmd(" ".join(argv[1:]))

if __name__ == '__main__':
    main()
