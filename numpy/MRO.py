import dis


class A(object):
    def show(self):
        print("I am in class A")


class B(A):
    # pass
    def show(self):
        print("I am in class B")


class C(A):
    # pass
    def show(self):
        print("I am in class C")


class D(B, C):
    # pass
    def show(self):
        print("I am in class D")


dl = D()


dl.show()
# print(dl.__mro__)
print(D.__mro__)

print(dl.show.__code__)
print(dl.show.__code__.co_code)
print(dl.show.__code__.co_code.decode("utf-16"))


dis.dis(dl.show)


def outerfunction(text):
    text = text

    def innerfunction():
        print(text)
    return innerfunction


dis.dis(outerfunction)
outerfunction("Hey!")()


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)
nterms = int(input("How many terms? "))  

for i in range(nterms):
    print(recur_fibo(i))

