#
import bs4
import re
import requests
import argparse
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description='Process a list of urls and scrape comments.')
parser.add_argument('file_path', help='Provide file path of .txt with list of urls to check',
                    nargs='?', default='0')
args = parser.parse_args()
print(args)

if args.file_path != '0':

    try:
        with open(args.file_path) as file:
            lines = file.readlines()

            current_datetime = datetime.now()
            name = str(current_datetime).replace(':', '_')
            name = name.replace('.', '_')
            name = name + ".txt"

            f = open(name, "w+")

        for line in lines:
            url = re.sub('\n', '', str(line))
            pagedata = requests.get(url)
            if pagedata.status_code == 200:
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
            else:
                print("An error occurred with URL: "+url+" HTTP Status Code: "+str(pagedata.status_code))

        f.close()
    except:
        print("Bad file path")
        sys.exit()


else:
    print(FileNotFoundError)
