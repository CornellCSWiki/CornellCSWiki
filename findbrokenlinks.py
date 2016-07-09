#!/usr/bin/env python3

import argparse
import html.parser
import os
import urllib.parse

class FindLinkParser(html.parser.HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []
        self.wikilink = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs = dict(attrs)
            if 'href' in attrs:
                if attrs['href'] == '#':
                    if 'title' in attrs:
                        self.links.append(attrs['title'])
                    else:
                        self.wikilink = True
                elif attrs['href'].startswith(self.base_url):
                    self.links.append(attrs['href'])

    def handle_data(self, data):
        if self.wikilink:
            self.wikilink = False
            self.links.append(data)


def collect_pages(site_dir, base_url):
    pages = []

    for root, _, files in os.walk(site_dir):
        virroot = os.path.relpath(root, site_dir)
        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext.lower() in ('.htm', '.html'):
                pages.append((os.path.join(root, filename),
                              urllib.parse.urljoin(base_url, os.path.join(virroot, filename))))

    return pages


def main(site_dir, base_url):
    pages = collect_pages(site_dir, base_url)
    urls = [page[1] for page in pages]
    urls.append(base_url)

    for filename, _ in pages:
        parser = FindLinkParser(base_url)
        with open(filename) as f:
            parser.feed(f.read())

        for link in parser.links:
            if link not in urls:
                print(filename, '\t', link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find broken site/wikilinks.")
    parser.add_argument("site", help="the directory containing the generated site")
    parser.add_argument("--base_url", help="the base URL of the site", required=True)

    args = parser.parse_args()

    main(args.site, args.base_url)
