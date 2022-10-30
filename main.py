def rss_reader(url):
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse
    u = urlopen(url)
    doc = parse(u)
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        description = item.findtext('description')
        link = item.findtext('link')
        print(title, description, date, link, sep='\n')
        print()
#rss_reader('https://ru.wordpress.org/feed/')