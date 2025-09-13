from threading import Thread
import time, threading, random

def download_file(file_id):
    # Print thread name and its unique thread ID (TID)
    print(f"Thread {file_id} started (TID: {threading.get_ident()})")
    # Simulate variable download time
    duration = random.randint(1, 4)
    time.sleep(duration)
    print(f"Thread {file_id} finished in {duration} sec")

if __name__ == "__main__":
    threads = []
    # Create and start 5 threads
    for i in range(1, 6):
        t = Thread(target=download_file, args=(f"File-{i}",))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All downloads completed")