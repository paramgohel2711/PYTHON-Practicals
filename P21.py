def anagram(s1, s2):
    t1=sorted(s1)
    t2=sorted(s2)
    if t1==t2:
        print("Strings Are Anagrams")
    else:
        print("Strings Are Not Anagrams")
s1=input("Enter 1st string: ")

s2=input("Enter 2nd string: ")

anagram(s1,s2)