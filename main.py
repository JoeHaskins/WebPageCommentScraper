#
import requests, bs4, re, time

lines = []
i=0

urlsfilepath = input("Path for .txt of urls:")
with open(urlsfilepath) as file:
    lines = file.readlines()

for line in lines:
    pagedata = requests.get(line)
    cleanpagedata = bs4.BeautifulSoup(pagedata.text, 'html.parser')

    stringpagedata = re.sub('\n', ' ', str(cleanpagedata))
    htmlcomments = re.findall(r'<!--(.+?)-->', stringpagedata)
    jscomments = re.findall(r'/\*(.+?)\*/', stringpagedata)

    print(htmlcomments)
    print(jscomments)