class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left  = left
		self.right = right

def createtree(asso):
	lis=[]
	for i in asso:
		lis.append(Tree(i))
#  for i in lis:
#    print i.cargo
	while len(lis)!=1:
		first=lis.pop()
		second=lis.pop()
		lis.append(Tree((first.cargo[0]+second.cargo[0],first.cargo[1]+second.cargo[1]),first,second))
		lis=sorted(lis,key=lambda x:x.cargo[1])
		lis.reverse()
	return lis.pop()

def encode(tree,i,code):
	while i!=tree.cargo[0]:
		if i in tree.cargo[0]:
			if i in tree.left.cargo[0]:
				code=code+str(1)
				tree=tree.left
			elif i in tree.right.cargo[0]:
				code=code+str(0)
				tree=tree.right
	return (i,code)
    
def decode(tree,code,cha):
	tree1=tree
	for i in code:
		if i=="1":
			tree=tree.left
		if i=="0":
			tree=tree.right
		if tree.right==None or tree.left==None:
			cha=cha+tree.cargo[0]
			tree=tree1
	return cha

def main():
	string=raw_input("enter the string")
	asso={}
	subtree=[]
	lis=[]
	cha=""
	for i in string:
		if i not in asso:
			asso[i]=0
		asso[i]+=1
	asso=sorted(asso.items(),key=lambda x:x[1])
	asso.reverse()
#  print asso
	tree=createtree(asso)
	print "\n Tree Root\n"
	print tree.cargo,"\n"
	for i in string:
		a=encode(tree,i,"")
		lis.append(a)
		cha=cha+a[1]
	print "\nCode for each character\n"
	print lis
	print"\n Huffman Code\n"
	print cha
	print "\n................Encoding Done.................\n"
	stdeco=raw_input("\nEnter the code that was assigned to each character in previous string to decode\n")
	print decode(tree,stdeco,"")
  
if __name__=="__main__":
	main()
