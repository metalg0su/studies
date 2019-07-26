import multiprocessing
import time


def run_proc2(conn, event: multiprocessing.Event):
    print("proc2 start")

    time.sleep(10)
    event.set()

    print("Conn: ", conn)

    print("proc2 end")


parent_conn, child_conn = multiprocessing.Pipe()
event = multiprocessing.Event()

proc2 = multiprocessing.Process(target=run_proc2, args=(child_conn, event))
print("Proc1 init proc2")
proc2.start()
print("Proc1 start proc2")

event.wait()
