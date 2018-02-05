def  main():
    rom=input().upper()
    roman_values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    final_int=0
    for i in range(len(rom)):
        if i > 0 and roman_values[rom[i]] > roman_values[rom[i-1]]:
            final_int+=roman_values[rom[i]]-2*roman_values[rom[i-1]]
        else:
            final_int += roman_values[rom[i]]
    print(final_int)

if __name__ == '__main__':
    main()
