starts=lambda s,ch:s.startswith(ch)
text=input("enter a string")
char=input("enter a character")
print("starts with",char+":",starts(text,char))
