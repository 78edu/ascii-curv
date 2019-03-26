print("--------------------------------")
a=0	##Strings counter
b=0	##Symbols per string counter
maxh=100	##Max width (symbols)
maxv=70	##Max. vertical limit for math function
st=""	##String for cycle
c="█"	##Fill symbol
em=" "	##Empty space
pp=" "	##Temp variable with next symbol, " " for 1st iteration
curv=0	##Curve "equation"
strs=[]	##Strings array after precalc
####
##(a*(maxh/maxv)) - just straight lines
##((a/5)**3)*(maxh/maxv) - curves 1
##((a/2)**2)*(maxh/maxv/3) - curves 2
####


for a in range (0,int(maxv/2)): ##String iterations
	for b in range (0,maxh): ##Cycle for each symbol in string
	  
	    curv=((a/2)**2)*(maxh/maxv/2) ##Place curve here
	    curv2=((a/4)**3)*(maxh/maxv/3) 	 ##Double fun
	   
	    if (b==int(curv) or b==maxh-int(curv)-1 or b==int(curv2) or b==maxh-int(curv2)-1):
	      pp=c
	      #fill symbols for two curves	
	    else:
	      pp=em
	    st+=pp
	    #add result to string
	if curv>=maxh/2: ##limits strings generation by a critical point of curv (not curv2)
	         break
	    
	##print(st)##, " ",curv," ",a)
	strs.append(st)
	st=""
print("###precalc done","     strings:", len(strs))
for a in range (0, len(strs)):
	print(strs[a])
for a in range (0, len(strs)):
	print(strs[len(strs)-a-1])
for a in range (0, len(strs)):
	print(strs[a])
for a in range (0, len(strs)):
	print(strs[len(strs)-a-1])
