'''Module for debian security advisories.'''

import feedparser


def fetch():
    '''Fetch security advisories feed.'''

    feed = feedparser.parse('https://www.debian.org/security/dsa')
    for entry in feed['entries']:
        print(f"Title: {entry['title']}")
        print(f"Link: {entry['link']}")
        print(f"Updated: {entry['updated']}")
        print()
