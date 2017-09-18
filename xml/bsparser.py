
# delwin

from bs4 import BeautifulSoup

with open('index.html') as fp:
    soup = BeautifulSoup(fp,'xml')

soup =  BeautifulSoup('<html>data</html>','xml')

