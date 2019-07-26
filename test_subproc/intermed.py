import subprocess
import os


print("intermed: start", os.getpid())

print("intermed proc: start grandchild")
grand_child = subprocess.Popen(["python", "./grandchild.py"])
print("intermed proc: after grandchild")

from time import sleep
sleep(3)

print("intermed: end", os.getpid())
