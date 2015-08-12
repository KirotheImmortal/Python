def searchFile(Path, a) :
	with open(Path,'r') as file :
		for line in file :
			if a in line :
				print(line)
				break
			else :
				print("Searching..")
	print("<Name Not Found>")


	
def splitNames(Path) :
	first = []
	last = []
	c =  1
	temp = ''
	with open(Path, 'r') as file :
		for line in file :
			for l in line :
				l = l.replace('\n', ' ')
				if(l!=' ')  and (c == 1):
					temp += l 
					
				elif(l != ' ' ) and ( c == 2) :
					temp += l
					
				elif( l == ' ') and (c == 1) :
					first.append(temp)
					c = 2
					temp = None
					temp = ''
					
				elif(l == ' ')  and (c == 2):
					last.append(temp) 
					c = 1
					temp = None
					temp = ''
					
	last.append(temp)
	print(first)
	print(last)


a = r"C:\Users\quinton.baudoin\Desktop\classNames.txt"



splitNames(a)
