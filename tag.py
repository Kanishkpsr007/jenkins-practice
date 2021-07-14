import subprocess
a=subprocess.run(["git", "describe" ,"--tags", "--abbrev=0"])
print(a)
