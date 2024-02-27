Module main()
    //step 1: Declare variable below
    totalBottles = 0
    counter = 1 
    todayBottles = 0
    totalPayout = 0 
    keepGoing = "y"
    
    //step 3 
    While(keepGoing == "y")
        //step 2. ... let say variable pass by reference
        getBottle(totalBottles, todayBottles, counter)
        calcPayout(totalPayout, totalBottles)
        printInfo(totalBottles, totalPayout)
    
        Display "Do you want to run the progran again? (Enter y for yes). "
        Input keepGoing
        
    End While
End Module

//step 4:
Module getBottle(totalBottles, todayBottles, counter) //a
    While(counter <= 7 )  //b
        Display "Enter number of bottle returns for the day: "
        Input todayBottles   //c
        
        totalBottles += todayBottles //d
        counter += 1     //e
    
    End While
End Module


//step 5:
Module calcPayout(totalPayout, totalBottles) // a 
    totalPayout = 0
    totalPayout = 0.10 * totalBottles //b

End Module


//step 6:
Module printInfo(totalBottles, totalPayout)  //a 
    Display "Total bottles returned in a week are ", totalBottles     //b
    Display "Total payout for the returned bottles is $",totalPayout  //c
    
End Module
