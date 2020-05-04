import os, sys, requests, threading


#1
print(os.getpid())

#2
print(os.getloadavg())

print(sys.platform)

if(sys.platform=="linux"):
  print("load average is",os.getloadavg())





 
  
#3
print(os.cpu_count())
load1, load5, load15 = os.getloadavg() 
   
print("Load average over the last 1 minute:", load1) 
print("Load average over the last 5 minute:", load5) 
print("Load average over the last 15 minute:", load15) 

if (os.cpu_count()-abs(load5)<1):
  exit()

#4
arr = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/", "http://akrepnalan.com/ceng2034"]

def link(string):

  x = requests.get(string)
  y = x.status_code

  if (200<y<300):
    print("The url is valid:"+string)

  else:
    print("The url is invalid:"+string)

link(arr[0])
link(arr[1])
link(arr[2])
link(arr[3])

th = threading.Thread(target=link,args=("http://bilgisayar.mu.edu.tr/"),)
