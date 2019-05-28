import os
from multiprocessing import Pool


def job(num):
    return num * num


if __name__ == '__main__':
    p = Pool(processes=20)
    data =p.map(job, range(20))
    p.close()
    print("finished")
    print(data)

