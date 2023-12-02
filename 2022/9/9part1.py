visited={
	'0':{0:0}
}
with open('9/input.txt','r') as f:
	xh=0
	yh=0
	xt=0
	yt=0
	for row in f:
		row=row.replace('\n','').split()
		for i in range(int(row[1])):
			if (row[0]=='R'):
				xh+=1
			elif(row[0]=='L'):
				xh-=1
			elif(row[0]=='U'):
				yh-=1
			else:
				yh+=1
			
			print(yh,xh,yt,xt)
			direct=0
			if(xh-xt>1):
				xt+=1
				direct=1
			elif(xh-xt<-1):
				xt-=1
				direct=1
			elif(yh-yt>1):
				yt+=1
				direct=2
			elif(yh-yt<-1):
				yt-=1
				direct=2
			
			if(xt!=xh and yt!=yh):
				if(direct==1):
					yt=yh
				elif(direct==2):
					xt=xh
			
			if yt not in visited.keys():
				visited[yt]={}
			visited[yt][xt]=1
som=0
for dict in visited.keys():
	som+=sum(visited[dict].values())
print(som)