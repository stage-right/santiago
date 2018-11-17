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
    if user_data:
        droplet['user_data'] = user_data
    if ssh_key_ids:
        droplet['ssh_keys'] = ssh_key_ids.split(",")
    return droplet

class DomainCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_domains(args))

class DropletCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_droplets(args))
    def do_create(self, args):
        droplet_args = args.split(" ")[:-1]
        print(santiago.new_droplet(make_droplet(*droplet_args), args.split(" ")[-1]))
    def do_delete(self, args):
        print(santiago.destroy_droplet(args.split(" ")[0], args.split(" ")[-1]))

class SantiagoCmd(Cmd):
    def do_quit(self, args):
        raise SystemExit
    def do_droplet(self, args):
        DropletCmd().onecmd(args)

if __name__ == '__main__':
    shell = SantiagoCmd()
    shell.prompt = '> '
    if len(argv) == 1:
        shell.cmdloop()
    else:
        shell.onecmd(" ".join(argv[1:]))
