from cmd import Cmd
from sys import argv

class SantiagoCmd(Cmd):
    def do_hello(self, args):
        print "Hello world"

    def do_quit(self, args):
        print "goodbye cruel world"
        raise SystemExit

if __name__ == '__main__':
    shell = SantiagoCmd()
    shell.prompt = '> '
    if len(argv) == 1:
        shell.cmdloop()
    else:
        shell.onecmd(" ".join(argv[1:]))
