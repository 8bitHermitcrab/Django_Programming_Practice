from urllib.parse import urlparse
from urllib.request import urlopen

# urlparse
result = urlparse("http://www.python.org:80/guido/python.html;philosphy?overall=3#n10")
# result

# urlopen(url, data=None, [timeout])
f = urlopen("http://www.example.com")
print(f.read(500).decode('utf-8'))