"""
See app/README.rst for setup instructions
"""

import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# --- docedit import and configuration ---
from app import docedit

docedit.DOCDIR = 'app/docs/'
docedit.DOCURL = '/static/docs/'
# --- / ---


TEMPLATES = os.path.join(os.path.dirname(__file__), 'templates')

def render(tpl, values):
    return template.render(os.path.join(TEMPLATES, tpl), values)


class MainPage(webapp.RequestHandler):
    def get(self):
        values = {
            'applink': '/docedit',
            'applink_text':'DocEdit Version %s' % docedit.__version__,
        }
        self.response.out.write(render('main.html', values))
        # [ ] main.html contains link to action that is better to generate
        #     to avoid grepping when link changes

class DocEdit(webapp.RequestHandler):
    def get(self):
        """
        Args:
          page: name of the page resource
        """
        # [ ] add debug messages
        pagename = self.request.get('page')
        if not pagename:
            # show index page
            self.response.out.write('<h4>documentation sources on this server</h4>\n')
            # [ ] or choose remote one
            self.response.out.write('<ul>')
            for link in docedit.listfiles():
                self.response.out.write('<li><a href="%s">%s</a></li>' % (link, link))
                # [ ] backurl function is needed
            self.response.out.write('</ul>')
        elif pagename not in docedit.listfiles():
            # show error page 
            # [ ] link to the code where the error occured
            self.response.out.write('invalid page name: %s' % cgi.escape(pagename))
        else:
            # show editor page
            self.response.out.write('a sophisticated editor for %s' % cgi.escape(pagename))


urlmap = [
    ('/', MainPage),
    ('/docedit', DocEdit),
]

def main():
    app = webapp.WSGIApplication(urlmap, debug=True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
