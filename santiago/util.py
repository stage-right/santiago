from cmd import Cmd
from sys import argv

import santiago

class DropletCmd(Cmd):
    def do_list(self, args):
        print(santiago.all_droplets(args))

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
