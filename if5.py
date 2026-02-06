# wap to check if we enter character is in upper case and lover case
ch=input("enter a character")
if(ch>='A'and ch<='Z'):
    print("upper case latter")
    ch=ch.lower()
    print("latter in lowercase is",ch)
else:
    print("lower case latter")
    ch=ch.upper()
    print("latter in uppercase is",ch)
