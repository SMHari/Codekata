def main():
   n=int(input())
   org=n
   rev=0
   while n>0:
       remainder=n%10
       rev=rev*10+remainder
       n=n//10
   if org==rev:
       print("yes")
   else:
       print("No")
if __name__=='__main__':
    main()
