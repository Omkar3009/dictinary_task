#name of the max sum

n=int(input())
l=list(map(str,input().split()))[:n]
dic={}
for i in range(n):
	dic[l[i]]=list(map(int,input().split()))
print(max(list(dic.items()), key=lambda x: sum(x[1]))[0])