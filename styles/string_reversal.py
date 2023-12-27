original = 'hello there'
result = original[::-1]
print(result)

def rev_string(str):
    if len(str) == 0:
        return str
    else:
        return rev_string(str[1:])+str[0]

print("With recursion " + rev_string(original))