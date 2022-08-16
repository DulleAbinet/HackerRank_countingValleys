def countingValleys(steps, path):
    # Write your code here
    nw_list =[0]*(len(path) + 1)
    cnt = 0
    for i in range(1,len(nw_list)):
        if path[i-1]== "D":
            cnt = -1
        else:
            cnt = 1
        nw_list[i]= nw_list[i-1] + cnt
    left = 0
    right = 2
    mid = 1
    cnt = 0
    while right < len(nw_list):
        if nw_list[mid] < 0 :
            if nw_list[left] == 0 and nw_list[right] != 0:    
                right += 1
                mid += 1
            else:
                cnt +=1
                left = right
                mid = left +1
                right +=2
        else:
            if nw_list[right] == 0:
                left = right
                mid = left 
                right +=1 
            mid += 1
            right +=1 
                       
    return cnt                    
