import concurrent.futures
import time


def sleeping(index, n):
    print('{:2d} starts sleep'.format(index))
    time.sleep(n)
    print('{:2d} ends sleep'.format(index))


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_dos = []
        for i, n in enumerate([5, 12, 4, 2, 1, ]):
            future = executor.submit(sleeping, i, n)
            to_dos.append(future)
        for future in concurrent.futures.as_completed(to_dos):
            future.result()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('Total Using {}s'.format(end - start))
