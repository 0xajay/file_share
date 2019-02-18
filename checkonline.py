import time,pycurl,sys,StringIO
from urlparse import urlparse
from time import time as dest
import multiprocessing

pool = multiprocessing.Pool(processes=4)


def tor(link,name):
    print "checking site: " + link
    try:
        link = link.encode('utf-8')
        result = StringIO.StringIO()
        milestone = dest()
        term = pycurl.Curl()
        term.setopt(term.URL,link)
        term.setopt(term.PROXY,'127.0.0.1')
        term.setopt(term.PROXYPORT,9050)
        term.setopt(term.PROXYTYPE,term.PROXYTYPE_SOCKS5_HOSTNAME)
        term.setopt(term.FOLLOWLOCATION,1)
        term.setopt(term.WRITEFUNCTION,result.write)
        term.perform()
        print "[+] ONLINE [+]"
        with open("onine-"+name+".txt","a") as g:
            g.write(str(link)+"\n")

    except:
        print "[+] OFFLINE [+]"
        with open("offline-"+name+".txt","a") as h:
            h.write(str(link)+"\n")

def fileparse(name):
    print "parsing " + name
    with open(name+".txt","r") as f:
        info = f.readlines()
    for k in info:
        k = k.replace("\n","")
        t1 = multiprocessing.Process(target=tor, args=(k,name))
        t1.start()
        t1.join()



if __name__ == "__main__":
    names = ["blogs","books","pages","chans","chats","forum","hacking","service","socialnetwork","wiki","press","searchengines"]
    for i in names:
        fileparse("forum")
        break
    print "finished"
