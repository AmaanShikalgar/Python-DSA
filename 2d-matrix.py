def searchMatrix(matrix,target):
    rows=len(matrix)
    cols=len(matrix[0])
    
    n = rows*cols
    
    left=0
    right=n-1
    
    while left<=right:
        mid =(left+right)//2
        row=mid // cols
        col=mid%cols
        value = matrix[row][col]
        
        if(value == target):
            return True
        elif(value<target):
            left= mid+1
        else:
            right=mid-1
    return False