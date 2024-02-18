def intToRoman(num):
        Roman = {
              1: "I",
              5: "V",
              10: "X",
              50: "L",
              100: "C",
              500: "D",
              1000: "M",
              5000: "V̅",
              10000: "X̅"
        }

        strNum = str(num)
        updtLst = []
            
             
             
        def exception(check): # used to create exception in roman numrals such as 4 -> IV or 9 -> IX
                if isinstance(check,int):
                    for m in Roman:
                        for j in Roman:
                            if check == m-j:
                                check = Roman[j] + Roman[m]
                                updtLst[k] = check
                  
        for i in range(len(str(num))): # separates the numbers 
            updtLst.append(int(strNum[i])*pow(10,len(str(num))-i-1))

        

        for j in range(len(updtLst)): # Updates the list if it exist in the dictionary
            if updtLst[j] in Roman:
                 updtLst[j] = Roman[updtLst[j]]
                 

            

        for k in range(len(updtLst)):
            check = updtLst[k]
            if check !=0:
                exception(check)

          
        Cache = 0
        


        for k in range(len(updtLst)): # used to create numbers with multiples Roman letters suc as 8 -> VIII
            strCache = ''
            check = updtLst[k]
            if check !=0:
                if isinstance(check,int):
                    for j in range(len(Roman)-1,-1,-1):
                        if check>=list(Roman.keys())[j]:
                            Cache = check//list(Roman.keys())[j]
                            check -= list(Roman.keys())[j]*Cache
                            strCache += list(Roman.values())[j]*Cache
            
            
                    updtLst[k] = strCache
        
        if 0 in updtLst: # removes 0 in the final list
            last = []
            for k in updtLst:
                if isinstance(k,str):
                    last.append(k)

            updtLst = last
        

        output = ''
        for a in updtLst: # concatinate all the string values to give final roman number
            output += a
        
        return output





print(intToRoman(399))