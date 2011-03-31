"""
Online documentation editor and patch generator.

tracking issue: http://code.google.com/p/pydotorg/issues/detail?id=6
online editor used for Google Code: http://codemirror.net/

link to send Python documentation patches:
http://bugs.python.org/issue?@template=item&components=4
"""

#import webbrowser
#import webserver

"""
implementation requirements and details:
 1. docs are available from static dir and served directly
 2. script needs access to this dir to list all files (DOCDIR)
 3. script requires DOCURL config, because expicit static path
    is better than implicit
"""

# --- config ---
# docdir is path with files
# docurl is the URL to fetch these files
DOCDIR = 'docs/'
DOCURL = '/static/'
# --- /config ---


# [ ] insert auto-updated consecutive revision (ok to be project wide)
__version__ = '0.1'


import os
def listfiles():
  # . GET output links for files available for editing
  # [ ] throw up strategy if dir is not found / error occured
  paths = []
  for root, dirs, files in os.walk(DOCDIR):
    for name in files:
      paths.append(root + name)
  return [DOCURL + p for p in paths]


def edit(filename=None):
  # . GET
  #  . if filename is not available - show list of files
  #  . if available - show edit form, load file from URL
  # . POST
  #  . check params (invalid filename, wrong data)
  #  . calculate diff
  #  . show diff for copy/paste

  pass


if __name__ == '__main__':
  # --== command line framefork ==--
  # 
  # this framework allows to inspect available actions
  # and test them from command line
  #

  # -- get actions list
  import inspect
  # no module name - can't use getmembers()
  #print inspect.getmembers(module, inspect.isfunction)
  actions = [locals()[a] for a in dir() if not a.startswith('__')]
  actions = [a for a in actions if inspect.isfunction(a)]

  # -- process commands
  import sys
  if len(sys.argv) == 1:
    # - no args - print available actions
    if actions:
      print sys.argv[0] + ' <action> [params]\n'
      # [ ] params processing
      print "Available actions:"
      for a in actions:
        print "- %s()" % a.__name__
        # [ ] print definition (prototype)
  else:
    # - action is specified - execute it
    action = sys.argv[1]
    if not action in [a.__name__ for a in actions]:
      sys.exit("Error: no such action '%s'" % action)
    print "Executing action '%s'" % action
    print locals()[action]()

