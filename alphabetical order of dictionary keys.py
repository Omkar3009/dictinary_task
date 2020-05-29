#alphabitical order


n=int(input())
l=list(map(str,input().split()))[:n]
dic={}
for i in range(n):
	dic[l[i]]=list(map(int,input().split()))
for i in sorted(dic.keys()):
	for j in range(len(dic[i])):
		print(dic[i][j],end=' ')
	print('')