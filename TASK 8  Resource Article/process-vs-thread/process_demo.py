from multiprocessing import Process
import os, time

def worker(name):
    print(f"Process {name} started (PID: {os.getpid()})")
    time.sleep(2)
    print(f"Process {name} finished")

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # important for Windows
    processes = []
    for i in range(3):
        p = Process(target=worker, args=(f"P{i+1}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed")
