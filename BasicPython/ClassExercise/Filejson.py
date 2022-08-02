from ast import Lambda
import json
# a='{"name":"liza", "age":20}'
# res = json.loads(a)

# print(res)
# print(type(res))
# print(json.dumps(res), type(json.dumps(res)))

# print(eval(a), type(eval(a)))

# b='[1,2,3,]'

# print(eval(b))
# print(type(eval(b)))


#Map

def A(i):
    i+=10
    return i
a = map(A, [1,2,3])

b = map(lambda x:x+10, [5,9,6])

print(list(a))
print(list(b))

#Args and Kwargs
def A(i, j):
    print(i, j)

A(4,5)

def test(*args, **kwargs):
    val = kwargs.get('a')
    print(val)

test(5, **{'a':1})