from requests_html import HTMLSession
 
keyword = input("keyword: ")
url = "https://www.google.com/search?q=site+html+liste+mail+gratuit&rlz=1C1CHBF_frFR897FR897&oq=site+html+liste+mail+gratuit&aqs=chrome..69i57.3214j0j7&sourceid=chrome&ie=UTF-8"
session = HTMLSession()
r = session.get(url)
 
listlink = list(set(r.html.absolute_links))
print(listlink)