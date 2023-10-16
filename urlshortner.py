import pyshorteners
url=input('Enter the URL u want to short:')

def shortenurl(url):
    a=pyshorteners.Shortener()
    print(a.tinyurl.short(url))

shortenurl(url)