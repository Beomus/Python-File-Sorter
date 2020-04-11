import os


extensions = {
		"HTML": ["html5", "html", "htm", "xhtml"],
		"IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg",
							 "heif", "psd"],
		"VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng",
							 "qt", "mpg", "mpeg", "3gp"],
		"DOCUMENTS": ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods",
									"odt", "pwi", "xsn", "xps", "dotx", "docm", "dox",
									"rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt",
									"pptx", "pdf"],
		"ARCHIVES": ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z",
								 "dmg", "rar", "xar", "zip"],
		"AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
							"msv", "ogg", "oga", "raw", "vox", "wav", "wma"],
		"SCRIPTS": ["txt", "in", "out"],
		"APP": ["exe"],
}

# create a list of all files in the current directory excluding this file
files = [i for i in os.listdir() if os.path.isfile(i) and i != os.path.basename(__file__)]

# make all the folders according to the extensions
for key in extensions:
	if not os.path.exists(key):
		os.makedirs(key)

# moving the files to their designated folders according to their extensions
for file in files:
	for key in extensions:
		if file.split(".")[-1] in extensions[key]:
			os.rename(file, key + "/" + file)

# adding all newly-created folders to a list
folders = [i for i in os.listdir() if not os.path.isfile(i)]

# loop through all folder in the list
for folder in folders:
	# check for any empty folder
	if len(os.listdir(folder)) == 0:
		# remove it accordingly
		os.rmdir(folder)

print("Done!")
