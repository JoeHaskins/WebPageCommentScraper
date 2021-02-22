#
import bs4
import re
import requests
from datetime import datetime

urlsfilepath = input("Path for .txt of urls:")
with open(urlsfilepath) as file:
    lines = file.readlines()

    current_datetime = datetime.now()
    name = str(current_datetime).replace(':', '_')
    name = name.replace('.', '_')
    name = name + ".txt"

    f = open(name, "w+")

for line in lines:
    url = re.sub('\n', '', str(line))
    pagedata = requests.get(url)
    cleanpagedata = bs4.BeautifulSoup(pagedata.text, 'html.parser')

    stringpagedata = re.sub('\n', ' ', str(cleanpagedata))
    htmlcomments = re.findall(r'<!--(.+?)-->', stringpagedata)
    jscomments = re.findall(r'/\*(.+?)\*/', stringpagedata)
    singlejscomments = re.findall(r'\B//(.+?)\n', str(cleanpagedata))

    print(htmlcomments)
    print(jscomments)
    print(singlejscomments)

    f.write("--"+url+"\n\n")
    for i in htmlcomments:
        f.write(str(i)+"\n")
    for i in jscomments:
        f.write(str(i)+"\n")
    for i in singlejscomments:
        f.write(str(i)+"\n")
    f.write("\n\n\n")

f.close()

