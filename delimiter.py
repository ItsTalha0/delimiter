import os 

#current directory path

cwd=os.getcwd()

# Check for modified folder if not found create one 

if os.path.isdir(cwd+'/modified') == False:
	try:
		os.mkdir(cwd+'/modified')
	except:
		print("permission denied")

# get list of all the files in the folder

fileList=os.listdir()

# file handling logic

for f in fileList:
	if f[-4:]=='.csv':
		with open(f,'r') as fp:
			the_text=list(fp.read())

		for i in range(len(the_text)):
			if the_text[i] == '|':
				the_text[i]=','
		string=''.join(str(e) for e in the_text)
		print(string)

		with open(cwd+'/modified/'+f,'w') as newFile:
			newFile.write(string)


		
		
			
			

