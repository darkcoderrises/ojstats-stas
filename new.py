#urllib,urllib2,bs4
import os
os.system("export no_proxy=\" localhost, 127.0.0.1, iiit.ac.in, .iiit.ac.in, iiit.net, .iiit.net, 172.16.0.0/12, 192.168.0.0/16, 10.0.0.0/8,10.4.3.208, 10.4.3.68\"")
os.system("export NO_PROXY=\"localhost, 127.0.0.1, iiit.ac.in, .iiit.ac.in, iiit.net, .iiit.net, 172.16.0.0/12, 192.168.0.0/16, 10.0.0.0/8,10.4.3.208, 10.4.3.68\"")

link = "https://login.iiit.ac.in/cas/login?service=http%3A%2F10.4.3.68"
link1 = "http://10.4.3.68/OJstats"

import urllib, urllib2, cookielib
username = raw_input("Username: ")
import getpass
import bs4
password = getpass.getpass('Password:')

tocheckp=raw_input("Problem to check: ")
tocheckm=raw_input("Marks to check: ")
anss=[]
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open(link, login_data)
resp1 = opener.open(link)
resp=opener.open("http://10.4.3.68/OJstats")
opener1=opener

soup = bs4.BeautifulSoup(resp.read())
#print soup
trs = soup.find_all("tr")
for tr in trs:
    for atrs in tr.attrs:
        if atrs == "style":
            if tr.attrs['style']=="display:none;":
                am = tr.attrs['id'][4:13]
                res=opener1.open(link1+"/?roll="+am)
                soup1 = bs4.BeautifulSoup(res.read())
                tds = soup1.findAll("tr",{"class":"nacc"})
                tds1 = soup1.findAll("tr",{"class":"acc"})
                tds=tds+tds1
                i=0
                for td in tds:
                    i=i+1
                    if(i<5):
                        continue
                    t=td.contents
                    if t[1].string==tocheckp and t[4].string==tocheckm:
                        flag=0
                        for item in anss:
                            if item == am:
                                flag=1
                        if flag==0:
                            anss.append(am)
for item in anss:
    print item
