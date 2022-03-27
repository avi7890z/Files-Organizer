import os,shutil

# location to organize
loc = r"C:\Users\Personal\Downloads"

files = os.listdir(loc)
extentions = []

print("STEP 1 : Reading Files..")
for f in files:

	if os.path.isfile(os.path.join(loc,f)):
		if "." in f:
			file_extention = f.split(".")[-1]
			extentions.append(file_extention)


# get unique extention
unique_extention = set(extentions)
print(f"STEP 2 : Fetching unique Extentions : {unique_extention}")

# create folder for unique extentions in uppercase if doesn't exist
for ext in unique_extention:
	if os.path.isdir(os.path.join(loc,ext.upper())):
		pass
	else:
		# try:
		os.mkdir(os.path.join(loc,ext.upper()))
		# except:
		# 	pass

print(f"STEP 3 : Created folders for exentions")

# now lets more all the files to the created folders

for f in files:
	for ext in unique_extention:
		if f.endswith(ext):
			try:
				shutil.move(os.path.join(loc,f), os.path.join(loc,ext))
			except:
				print(f"-->{f} already Exists")

print(f"STEP 4 : Organized files into their folders.")
print("-- Mission Complete")