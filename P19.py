def vc(s):
    v=0
    c=0
    for i in s:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            v=v+1
        else:
            c=c+1
    return (v,c)
s=input("Enter a String:")
x=vc(s)
print(x)
print("Number of vowels:",x[0])
print("Number of consonants:",x[1])
