import time
n=int(input("Enter time in seconds : "))
while n:
    mins=n//60
    sec=n%60
    print("{:02d}:{:02d}".format(mins,sec),end="\n")
    time.sleep(1)
    n-=1
print("time completed!")
