# coding=utf-8
import termcolor
import sys

defaultEncoding = sys.getdefaultencoding()
termcolor.cprint(defaultEncoding)
termcolor.cprint(u"🔥 🗄️ Dropping something here: {}".format(u"SOME_NAME"), u"cyan")
