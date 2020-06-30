import requests
import bs4

def get_frequency_alphabet():
    htmlfile=requests.get('http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html').text
    soup=bs4.BeautifulSoup(htmlfile,'lxml')
    tables = soup.find_all('table')
    cnt=0
    letters=[]
    for my_table in tables:
        cnt += 1
        rows = my_table.find_all('tr', recursive=False)                  # <-- HERE
        for row in rows:
            cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
            l=cells[0].string
            if len(l)==1: letters.append(l)
    return ''.join(map(str.lower, letters))  
