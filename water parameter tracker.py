
import datetime
import os
#gets the current date and time
current_date = datetime.datetime.now()
def water_parameter():

    #normal tests
    ph = str(input("whats the ph"))
    gh = str(input("whats the gh"))
    kh = str(input("whats the kh"))
    nitrates = str(input("whats the nitrate"))
    #write tests
    tests = ("\n%s\nnitrates: %s general Hardness: %s karbonate hardness: %s nitrate: %s "% (current_date,ph,gh,kh,nitrates))
    testfile = open("water parameter tracker.txt", "a")
    testfile.write(str(tests))
    testfile.close()
    #asks if you want to log optional tests
    optional_tests = input("do you want to log NH3, NO2, PO4, misc y for yes n for no: ")
     
     
    if optional_tests == ("y"):
        while optional_tests != [i for i in ("y","n")]:
            #optional tests
            phosphate = str(input("whats the phosphate"))
            ammonia = str(input("whats the ammonia"))
            nitrite = str(input("whats the nitrite"))
            chlorine = str(input("whats the the chlorine"))
            copper = str(input("whats the copper"))
            #writes optional tests
        
            optional_test = ("\n%s\nphosphate: %s ammonia: %s nitrite: %s chlorine: %s copper: %s"%(current_date,phosphate,ammonia,nitrite,chlorine,copper))
            optional_test_file = open("optional_test.txt", "a")
            optional_test_file.write(str(optional_test))
            optional_test_file.close()

    #closes program if awnser is no
    elif optional_tests == ("n"):
        os.close()
    #asks question again if awnser is somebesides yes or no
    else:
        optional_tests = input("do you want to log NH3, NO2, PO4, misc y for yes n for no:")
#runs function  
water_parameter()
#closes when function is done running
os.close

    


   
    
    



