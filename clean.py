import os
import shutil

try:
	os.mkdir("removed")
except:
	pass

remove_str = [".log", ".fls", ".aux", ".fdb_latexmk", ".synctex.gz", ".nav", ".out", ".snm", ".toc"]

for root, dirs, paths in os.walk(os.getcwd()):
	# print(root)
	# print(dirs)
	# print(paths)
	# print("-----------")
	for path in paths:
            for string in remove_str:
                if path.endswith(string):
                    shutil.move(root + "/" + path, "removed/" + path)
