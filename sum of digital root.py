n=int(input("enter th number:"))
if n==0:
    digital_root=0
else:    
    digit_root=n%9
      if n%9==0:
        digital_root=9
print(f"the digital rootof{n}is",digital_root)    