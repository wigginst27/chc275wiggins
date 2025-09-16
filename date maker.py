"""""

Foundation of Code 275 - 1
Made a Date Predictor for December 2024
"""""
def main():

    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


    var1 = int(input("Choose a day in December"))
                            # for var1 in range (0,31):
    #if var1 == range(0,31):
    print ( "The " + str(var1) + " of December is a " + days[var1%7] )
        
   
    




if __name__=="__main__":
    main()