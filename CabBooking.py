#Ask question(repeat)

while True:

    count=""
    carAC=int(25)
    carNonAC=int(20)
    vanAC=int(25)
    vanNonAC=int(20)
    threewheel=int(30)
    truck=int(15)
    lorry=int(17)
    user = "user01"
    password= "password"
    RemoveVehicle = "1234WP"
    
    #Main Menu
    print("")
    print("")
    print("WELCOME TO THE CAB SERVICE - S92076589")
    print("")
    print("1.Request a Cab")
    print("2.Apply to work as a Driver")
    print("3.Add Vehicle")
    print("4.Remove Vehicle")
    print("5.See available vehicles in each category")
    print("")

    option=int(input("Enter your prefferedd option:"))

    #option1 : Request a Cab

    if option==1:
        print("")
        print("Car:maximum number of passengers - 3 and 4 AC/ Non AC")
        print("Van:Maximum number of passengers - 6 and 8 AC/ Non AC")
        print("3 Wheelers:Maximum number of passengers - 3")
        print("Trucks:Size – 7 ft and 12 ft")
        print("Lorry:Max load and size - 2500kg and 3500kg")
        print("")
        print("")
        name=str(input("Enter your Name:"))
        phone=int(input("Enter your Phone Number:"))
        if (len(str(phone))) != 10:
            print("")
            print("Phone Number must contain 10 Digits")
            continue
        vehicle=str(input("Enter prefered vehicle type:"))
        if str(vehicle) == ("Car"):
            if carAC < 0 or carNonAC <0:
                print("")
                print("Currently Unavailable")
                continue
            # car = car -int(1)
        elif str(vehicle) == ("Van"):
            if vanAC < 0 or vanNonAC < 0:
                print("")
                print("Currently Unavailable")
                continue
            # van = van -int(1)
        elif str(vehicle) == ("3 Wheel"):
            if threewheel < 0:
                print("")
                print("Currently Unavailable")
                continue
            threewheel = threewheel -int(1)
        elif str(vehicle) == ("Truck"):
            if truck < 0:
                print("")
                print("Currently Unavailable")
                continue
            truck = truck -int(1)
        elif str(vehicle) == ("Lorry"):
            if lorry < 0:
                print("")
                print("Currently Unavailable")
                continue
            lorry = lorry -int(1)  
        else :
            print("")
            print("Invalid Vehicle Name")
            continue
        
        ac=str(input("AC or NonAC:"))
        if str(vehicle) == ("Car"):
            if str(ac) == ("AC"):
                if carAC < 0:
                    print("Sorry AC cars currently unavailable")
                    continue
            if str(ac) == ("NonAC"):
                if carNonAC < 0:
                    print("Sorry NonAC cars currently unavailable")
                    continue
        if str(vehicle) == ("Van"):
            if str(ac) == ("AC"):
                if vanAC < 0:
                    print("Sorry AC vans currently unavailable")
                    continue
            if str(ac) == ("NonAC"):
                if vanNonAC < 0:
                    print("Sorry NonAC vans currently unavailable")
                    continue
        passengers=int(input("Number of Passengers:"))
        if str(vehicle) == ("Car"):
            if int(passengers) > 4:
                print("")
                print("Maximum Number of Passengers is 4")
                continue
        if str(vehicle) == ("Van"):
            if int(passengers) > 8:
                print("")
                print("Maximum Number of Passengers is 8")
                continue
        if str(vehicle) == ("3 Wheel"):
            if int(passengers) > 3:
                print("")
                print("Maximum Number of Passengers is 3")
                continue
        addressP=str(input("Enter the Pickup Address:"))
        addressD=str(input("Enter the Drop Address:"))
        dateTime=str(input("Enter the Pickup time and Date (dd/mm/yyyy-hh/mm):"))
        print("")
        print("")
    
        print("Your Ride is Ready...")


    #option2 : Apply to work as a driver
        
    if option==2:
        print("")
        nameD=str(input("Enter your Name:"))
        addressD=str(input("Enter your Address:"))
        dobD=str(input("Enter your Date of Birth (dd/mm/yyyy):"))
        ageD=int(input("Enter your Age:"))
        if (ageD < 18):
            print("")
            print("Sorry, you can not Apply")
        else:
            phoneD=str(input("Enter your Phone Number:"))
            if (len(str(phone))) != 10:
                print("")
                print("Phone Number must contain 10 Digits")
                continue
            nicD=str(input("Enter your NIC Number:"))
            genderD=str(input("Enter your Gender (Male/Female):"))
            licenseNumD=str(input("Enter your Drivers License Number:"))
        
            print("")
            print("Assigned Form")
            print("")
            print("Details of the Driver")
            print("")
            print("Name : " +nameD)
            print("NIC : " +nicD)
            print("Gender :" +genderD)
            print("License Number : " +licenseNumD)
            print ("Phone Number : " +phoneD)



    #option3 : Add Vehicle

    if option==3:
        print("")
        vehicleType=str(input("Enter Type of the Vehicle:"))
        ac=str(input("AC or NonAC"))
        vehicleNum=str(input("Enter the Vehicle Number:"))
        userID=str(input("Enter your User ID:"))
        if str(userID) != user:
            print("")
            print("Invalid user ID")
            continue
        passwordD=str(input("Enter your Password:"))
        if str(passwordD) != password:
            print("")
            print("Invalid Password")
            continue
        print("")
        print("")
       
        print("Vehicle added Successfully...")

        if str(vehicle) == ("Car"):
            if str(ac) == ("AC"):
                carAC = carAC + int(1)
            if str(ac) == ("NonAC"):
                carNonAC = carNonAC + int(1)
        elif str(vehicle) == ("Van"):
            if str(ac) == ("AC"):
                vanAC = vanAC + int(1)
            if str(ac) == ("NonAC"):
                vanNonAC = vanNonAC + int(1)
        elif str(vehicle) == ("3 Wheel"):
            threewheel = threewheel + int(1)
        elif str(vehicle) == ("Truck"):
            truck = truck + int(1)
        elif str(vehicle) == ("Lorry"):
            lorry = lorry + int(1)  
        else :
            print("Invalid Vehicle Name") 

    #option4 : Remove Vehicle

    if option==4:
        print("")
        vehicleType=str(input("Enter Type of the Vehicle:"))
        vehicleNum=str(input("Enter the Vehicle Number:"))
        if str(vehicleNum) != RemoveVehicle:
            print("")
            print("Invalid Vehicle Number")
            continue
        userID=str(input("Enter your User ID:"))
        if str(userID) != user:
            print("")
            print("Invalid user ID")
            continue
        passwordD=str(input("Enter your Password:"))
        if str(passwordD) != password:
            print("")
            print("Invalid Password")
            continue
        print("")
        print("")

        print("Vehicle Successfully Removed...")


    #option5 : See available vehicles in each category
        
    if option==5:
        print("")
        print("AC Car -" +str(carAC))
        print("NonAC Car -" +str(carNonAC))
        print("AC van -" +str(vanAC))
        print("NonAC van -" +str(vanNonAC))
        print("3 Wheels -" +str(threewheel))
        print("Truck -" +str(truck))
        print("Lorry -" +str(lorry))
    

    print("\n")
