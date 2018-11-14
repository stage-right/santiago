from cmd import Cmd
from sys import argv

import santiago

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
