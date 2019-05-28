import os
import multiprocessing 

def spawn(i, num2):
    print("Spawned! {} and second number {}".format(i, num2))



if __name__ == '__main__':
    for i in range(50):
        p = multiprocessing.Process(target=spawn, args=(i,i,))
        p.start()
        # p.join()


