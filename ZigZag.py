import math

def convert(s, numRows):
        rows = numRows
        K = len(s)
        addCol = numRows - 2
        cols = 0
        if numRows == 1:
             return s
        elif numRows > len(s):
             cols = 1
        else:
             
            while True: # Determining number of columns of the list
                K -= numRows
                cols+=1
                if K<numRows:
                    cols += K
                    break
                
                
                K -= addCol
                cols+=addCol
                if K<numRows:
                    cols += 1
                    break
        
        output = [[0 for a in range(cols)] for b in range(rows)] # creating an empty 2-D Array
        count = 0
        OutStr = ''
        c = 0
        newRow = 0
        nextRow = rows-1
        
        while c<cols:
            if newRow == 0: # Filling data vertically
                nextRow = rows-1
                for j in range(rows):
                    if count>=len(s):
                        break
                    output[j][c]= s[count]
                    count+=1

            c+=1
            
            nextRow -= 1
            newRow = nextRow
            if nextRow != 0:    # Filling data diagonally
                if count>=len(s):
                        break
                output[nextRow][c]= s[count]
                count+=1

        for i in range(rows): # creating a concatinated string horizontally
            for j in range(cols):
                if output[i][j] != 0:
                    OutStr += output[i][j]

        return OutStr,output
            
            
            
        
            
        

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
