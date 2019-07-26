import subprocess
import os
import time

print("main: start", os.getpid())

print("main proc: start intermed")
intermed_proc = subprocess.Popen(["python", "./intermed.py"])
print("main proc: after intermed")
print("- code: ", intermed_proc.returncode)
# print("- code, stdin, out, err" , intermed_proc.returncode, intermed_proc.stdin, intermed_proc.stdout, intermed_proc.stderr)

print("before wait")
intermed_proc.wait()
print("after wait- immed?")

time.sleep(5)
print("main proc: before close streams - ")
# print("- code, stdin, out, err" , intermed_proc.returncode, intermed_proc.stdin, intermed_proc.stdout, intermed_proc.stderr)
print("- code: ", intermed_proc.returncode)
# if intermed_proc.stdout:
#     intermed_proc.stdout.close()
# print("- code, stdin, out, err" , intermed_proc.returncode, intermed_proc.stdin, intermed_proc.stdout, intermed_proc.stderr)
# if intermed_proc.stderr:
#     intermed_proc.stderr.close()
# print("- code, stdin, out, err" , intermed_proc.returncode, intermed_proc.stdin, intermed_proc.stdout, intermed_proc.stderr)
# try:  # Flushing a BufferedWriter may raise an error
#     if intermed_proc.stdin:
#         intermed_proc.stdin.close()
# except:
#     pass

print("main proc: before wait - ")
print("- code, stdin, out, err" , intermed_proc.returncode, intermed_proc.stdin, intermed_proc.stdout, intermed_proc.stderr)
intermed_proc.wait()
print("main proc: before sigterm - ", intermed_proc.returncode)
time.sleep(5)
intermed_proc.terminate()  # 얘를 써도 자식이 살아남음 ㅡㅓㅡ
intermed_proc.wait()
print("main proc: intermed terminated!!")
print("main proc: intermed proc ret code is ", intermed_proc.returncode)
time.sleep(5)

print("main: end ", os.getpid())
