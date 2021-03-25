import time

from colorama import Fore, Style, init

from lib import __version__ as version

init(convert = True)

class Banner:
    r = Fore.RED
    y = Fore.YELLOW
    ny = Fore.YELLOW
    nw = Fore.WHITE
    g = Fore.GREEN
    e = Style.RESET_ALL


                                         
  

    def banner(self):
        print(self.ny + "  ____    _    ____  _____ ___ ___   " + self.e)
        print(self.ny + " / ___|  / \  |  _ \|  ___|_ _/ _ \  " + self.e)
        print(self.ny + "| |  _  / _ \ | |_) | |_   | | | | | " + self.e)
        print(self.ny + "| |_| |/ ___ \|  _ <|  _|  | | |_| | " + self.e)
        print(self.ny + " \____/_/   \_|_| \_|_|   |___\___/  " + self.e)
        print(self.g + "~/#" + self.e + " golf in spain" + self.g + " #\\~" + self.e)
        print(self.g + "~/#" + self.e + "titi @11titiprieto" + self.g + " #\\~" + self.e)
        
        print("\n")

    @classmethod
    def preamble(cls, url):
        print('URL: %s' % url)
        print('---------  Scan Started: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    @classmethod
    def postscript(cls):
        print('---------  Scan Finished: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    def version(self):
        return self.g + "~/#" + self.e + " Sitadel (" + version + ")\n"
