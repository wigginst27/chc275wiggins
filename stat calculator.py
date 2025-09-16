"""
save this for later

Statistics Calculator
"""
#import seaborn as sns
import re 

def printmenu():
    print ("  ")
    print("1.Maximum")
    print("2.Minimum")
    print("3.Median")
    print("4.Mean")
    print("5.Clear List")
    print("0.Quit")
    

def getlist():

    list = []
    check = True
    while check == True:
        number = input('Enter an Integer: ')#not done

        if number == "p":
            if len(list)<1:
                print ("No Input")
    
            else:
                return list
        elif re.search(r'\d+', number):
            list.append(int(number))
            """
        elif number == re('\d+') :
            list.append(int(number))  
            """    
        else:
            print ("Not a number")

def getmaximum(userlist):  
    userlist.sort()     #sorts the list numericlly
    last = (len(userlist)) - 1 #gets the last number
    return "The Maximun is " + userlist[last]

def getminimum(userlist):
    userlist.sort()   #sorts the list numericlly
    return "The Minimum is " + (str(userlist[0]))  #gets the first number

def getmedian(userlist):
    userlist.sort()  #sorts the list numericlly
    mid = (len(userlist))//2

    if  len(userlist) %2 ==1:
        return "The Median is " + (str(userlist[mid]))
    else:
        avrge = userlist[mid] + userlist[mid - 1] 
        return "The Median is " + (str(avrge/2))
    
def getmean(userlist):
    userlist.sort
    mean = 0
    length = len(userlist)
    for loop in userlist:
        mean = mean + loop
    return "The Mean is " + (str(mean/length))
    #return sum(userlist)/len(userlist)
    
def emptyList():
    print("empty")

def main():
    print ("lortyy™")
    print ("Welcome to the Statistic Calculator")
    print ("Enter Your Numbers One a Time")
    print ('Press "p" Once You Are Done') 
    userlist = getlist()
    check = True
    while check == True:
        printmenu()
        option = input("Type what Number You Want ").strip()
        if option == "1":
            print(getmaximum(userlist))
        elif option == "2": 
            print(getminimum(userlist))
        elif option == "3":  
            print(getmedian(userlist))
        elif option == "4": 
            print(getmean(userlist))
        elif option == "5":
            print ("List Has Been Cleared!")
            print(main())
        elif option == "0":
            print ("Goodbye ✌️")
            exit()
        elif re.search(r'\D+', option):
            print ("Please put a number")

if __name__ =="__main__":
    main()
