AUTHOR = 'K Dublin'
SITENAME = 'K Dublin Photography'
SITEURL = '' # 'https://kdublin.com'

PATH = 'content'

# Static Paths
STATIC_PATHS = ['static', 'static/images', 'static/css', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

SITEDESCRIPTION = 'Photography portfolio site for K Dublin'

# Make into Static Site with Secondary Blog
ARTICLE_PATHS = ['folio']
ARTICLE_URL = 'folio/{slug}.html'
ARTICLE_SAVE_AS = 'folio/{slug}.html'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = 'folio/category/{slug}.html'
CATEGORY_URL = 'folio/category/{slug}.html'
TAG_SAVE_AS = 'folio/tag/{slug}.html'
TAG_URL = 'folio/tag/{slug}.html'


DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme Settings
THEME = 'themes/photowall'



# Blogroll
LINKS = (('Writing', 'https://kevindublin.com/'),
         ('Living Room', 'https://www.thelivingroomsf.com/'),
        )

# Social widget
SOCIAL = (('instagram', 'https://www.instagram.com/kevdublin/'),
          ('twitter', 'https://www.twitter.com/parteverything'),
          ('email', 'mailto:k@kdublin.com'),)

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Turn off caching for local development
LOAD_CONTENT_CACHE = False
