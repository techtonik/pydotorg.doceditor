"""
Online documentation editor and patch generator.

tracking issue: http://code.google.com/p/pydotorg/issues/detail?id=6
online editor used for Google Code: http://codemirror.net/

link to send Python documentation patches:
http://bugs.python.org/issue?@template=item&components=4
"""

#import webbrowser
#import webserver

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
  # -- command line framefork --
  # 
  # this framework allows to inspect available actions
  # and test them from command line
  #
  actions = [a for a in dir() if not a.startswith('_')]
  if actions:
    print "Available actions:"
    for a in actions:
      print "- %s" % a
      # [ ] print definition / prototype
