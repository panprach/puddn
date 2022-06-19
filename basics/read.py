import urllib.request

url = "https://raw.githubusercontent.com/maxg203/Python-for-Beginners/master/shakespeare.txt"
f = urllib.request.urlopen(url)
for l in f:
    print(l)
f.close()