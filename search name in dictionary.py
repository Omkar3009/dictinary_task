#search by name

n=int(input())
l=list(map(str,input().split()))[:n]
dic={}
for i in range(n):
	dic[l[i]]=list(map(int,input().split()))
r=input()
if(r in dic.keys()):
	print(sum(dic[r]))
else:
	print("No such student")