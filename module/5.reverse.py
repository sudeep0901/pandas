def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
    print(str, i)
  return str


s = "Geeksforgeeks"
# print (reverse(s))


## using recurision

def recurse_reverse(str):
    if (len(str) == 0):
        return str

    else:
        print(str[1:], str[0])
        return recurse_reverse(str[1:]) + str[0]


name = "sudeep patel"
# print(name[1:] + name[0])

print(recurse_reverse(name))