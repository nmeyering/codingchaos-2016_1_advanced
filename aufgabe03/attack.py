import timeit
import os

ret = 256
def crack(guess):
    global ret
    timeit.timeit
    ret = os.system('./crypto {}'.format(guess))

def inc(guess):
    c = guess[-1:]
    return guess[:-1] + chr(ord(c)+1)

def main():
    guess = 'A'
    t = 0
    n = 5
    global ret
    while ret == 256:
        t = timeit.timeit(lambda: crack(guess), number=n)
        if t > len(guess)*0.1*n:
            print(guess)
            guess += 'A'
        else:
            print("\r" + guess, end='')
            guess = inc(guess)
    if ret == 0:
        print("password found: {}".format(main()))
    if ret == 512:
        print("password not found :/")

main()

