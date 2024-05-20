# if __name__ == '__main__':
#     n = int(input())
# for i in range(n):
#      name = i * i
#      print(name)   

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        elif year % 400 == 0:
            leap = True 
        else:
            leap = False               
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))