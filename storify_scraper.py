from bs4 import BeautifulSoup
import requests

# the file you saved locally from https://storify.com/your_user_name
filename = "my_storifys.html"
# change to your own Storify username
username = "your_user_name"

string1 = '/' + username + '/'
string2 = 'https://storify.com/' + username + '/followers'
string3 = 'https://storify.com/' + username + '/following'

html = open(filename)
bsObj = BeautifulSoup(html, "html.parser")
url_list = bsObj.find_all('a')

# using set() prevents duplicates
my_urls = set()

for link in url_list:
    try:
        h = link.get('href')
        if string1 in h and '/edit' not in h:
            my_urls.add(h)
    except:
        pass

# now you have a set of all your Storify URLs
# let's remove the two you won't use from the set
my_urls.remove(string2)
my_urls.remove(string3)

# access Storify's rawer HTML file for each Storify by adding '.html'
# download the file to your hard drive, current directory
def saveAsNewHTMLFile(url):
    file = url + '.html'
    split_list = file.split('/')
    # get filename to assign to saved file
    new_filename = split_list[-1]
    r = requests.get(file, allow_redirects=True)
    open(new_filename, 'wb').write(r.content)

# if you want the file as XML not HTML
def saveAsNewXMLFile(url):
    file = url + '.xml'
    split_list = file.split('/')
    # get filename to assign to saved file
    new_filename = split_list[-1]
    r = requests.get(file, allow_redirects=True)
    open(new_filename, 'wb').write(r.content)

# if you want the file as JSON not HTML
def saveAsNewJSONFile(url):
    pre = 'https://api.storify.com/v1/stories' + string1
    split_list = url.split('/')
    # construct the URL to get
    file = pre + split_list[-1]
    # get filename to assign to saved file
    new_filename = split_list[-1] + '.json'
    r = requests.get(file, allow_redirects=True)
    open(new_filename, 'wb').write(r.content)

# imma just run the HTML option below - you can change to
# saveAsNewXMLFile(url) or
# saveAsNewJSONFile(url)

# save all your Storifys
for url in my_urls:
    saveAsNewHTMLFile(url)
