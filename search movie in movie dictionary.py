movies={2004:['anji','vasham','arya','mass'],2005:['Bhadra','atadu','chatrapati'],2006:['Don','Happy days','aata']}
c=input()
for i in movies:
	if(c in movies[i]):
		print(c,i)