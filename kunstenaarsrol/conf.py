# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Kunstenaars Rol"
copyright = "2023-2024, Stichting Kunstenaars Rol"
author = "Stichting Kunstenaars Rol"


html_baseurl = "https://kunstenaarsrol.com/"
html_title = "Kunstenaars Rol"
timezone = "Europe/Amsterdam"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_favicon",
    # "sphinxcontrib.youtube",
    # "sphinxcontrib.bibtex",
    "sphinx.ext.autosectionlabel",
    "sphinxext.opengraph",
]

myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence", "substitution"]

ogp_site_url = html_baseurl

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "nl"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_show_sourcelink = False

favicons = ["images/palet-cropped_small.png"]
# -- Font-Awesome Options -----------------------------------------------------

# # Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
fontawesome_included = True
fontawesome_link_cdn = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
)

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


def setup(app):
    app.add_css_file("custom.css")


html_sidebars = {
    # "index": ["search-field.html", "aboutme.html"],
    # "about": ["search-field.html", "aboutme.html"],
    "posts": ["search-field.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "verhalen": ["search-field.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "verhalen/[!tag]**": [
        "search-field.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/archives.html",
    ],
    "posts/[!tag]**": [
        "search-field.html",
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/archives.html",
    ],
    # "posts/tag": ["search-field.html", "ablog/tagcloud.html", "ablog/archives.html"],
    # "posts/tag/**": ["search-field.html", "ablog/tagcloud.html", "ablog/archives.html"],
    # "posts/[!tag]**": [
    #     "search-field.html",
    #     "ablog/postcard.html",
    #     "ablog/recentposts.html",
    #     "ablog/archives.html",
    # ],
}


html_theme_options = {
    # If you want to configure Twitter or Github social media buttons to show up to the right of your nav bar,
    # you can use the "github_url" and "twitter_url" options:
    # "github_url": "https://github.com/adriaanrol/",
    # "gitlab_url": "https://gitlab.com/AdriaanRol/",
    # "twitter_url": "https://www.twitter.com/adriaanrol/",
    "show_prev_next": False,
    # You can also change the text that is in the search bar before people click on it by setting the
    # "search_bar_text"
    "search_bar_text": "Zoeken",
    "footer_start": ["copyright"],
    "footer_end": ["contact"],
    # # By default your site will have a search bar in the nav bar, but when we include the about.html,
    # # this gets removed to so you can add one to the top "navbar" instead
    # "search_bar_position": "navbar",
    # "navbar_center": [],
}

# html_theme_options["analytics"] = {
#     "google_analytics_id": "G-J6GBVEHM1P",
# }

# <script defer data-domain="kunstenaarsrol.nl" src="https://plausible.io/js/script.js"></script>


html_theme_options["analytics"] = {
    # The domain you'd like to use for this analytics instance
    "plausible_analytics_domain": "kunstenaarsrol.nl",
    # The analytics script that is served by Plausible
    "plausible_analytics_url": "https://plausible.io/js/script.js",
}

# -- Ablog configuration ---------------------------------------------------
ablog_builder = "dirhtml"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = "https://kunstenaarsrol.com/"

# A path relative to the configuration directory for posts archive pages.
blog_path = "verhalen"

# The "title" for the posts, used in active pages.  Default is ``'Blog'``.
BLOG_TITLE = {"en": "Artists Rol", "nl": "Kunstenaars Rol"}

blog_default_language = "nl"

blog_languages = {"nl": ("Nederlands", None)}

# The path that you store your content in, this will be used for the browsing path
# on your published website
# e.g. blog_post_pattern = "blog/*/*"
blog_post_pattern = "posts/*/*"

# blog_feed_fulltext: Choose to display full text in blog feeds.
blog_feed_fulltext = True

# post_redirect_refresh: Number of seconds (default is 5) that a redirect page waits before refreshing the page
# to redirect to the post.
post_redirect_refresh = 1

# post_auto_image: Index of the image that will be displayed in the excerpt of the post. Default is 0, meaning no
# image. Setting this to 1 will include the first image
post_auto_image = 1

# post_auto_excerpt: Number of paragraphs (default is 1) that will be displayed as an excerpt from the post. Setting
# this 0 will result in displaying no post excerpt in archive pages.
post_auto_excerpt = 1


# Make sure the target is unique
autosectionlabel_prefix_document = True

html_show_sourcelink = False
