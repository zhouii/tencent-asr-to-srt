import re
import sys

with open(sys.argv[1],'r',encoding='utf8') as f:
	content=f.read()
	
lines=content.splitlines()
i=1
with open('subtitle.srt','w',encoding='utf8') as f:
	for line in lines:
		res=re.findall('\[(\d*?):(\d*?)\.(\d*?),(\d*?):(\d*?)\.(\d*?)\]\s*([\s\S]*)$',line)[0]
		f.write('%s\n%s:%s:%s,%s --> %s:%s:%s,%s\n%s\n\n'%(i,int(res[0])//60,int(res[0])%60,res[1],res[2],int(res[3])//60,int(res[3])%60,res[4],res[5],res[6]))
		i+=1
