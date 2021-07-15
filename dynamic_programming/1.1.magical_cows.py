# A farmer has cows on several farms and he cows double in number every midnight. There is a limit M to the number of cows that can stay on a farm so
# the farmer has to relocate half the cows to a new empty farm once the number on a farm crosses the limit. Given the number of cows that exist on each farm
# on day 0, find the number of farms that would be occupied on day N.

# Solution:
# We could track each farm individually and spawn new farms as needed but this would lead to exponential space and time complexity because for some threshold day D, 
# the number of farms would be doubling for each day E, where E > D. 
# The alternative and optimal solution would be to track the frequency of farms for each possible number of cows. Since there is a limit M, we could initialize a frequency array of size M
# to store the frequencies. If cows on farms with a certain number of cows would not need to be relocated on the current day we simply set the frequency of that number of cows to zero and increment the
# frequency of double the number of cows by the former. If the cows would need to be relocated, since another farm would be created with the same number of cows (preduplication), we simply double the frequency 
# of that number of cows 

# given farms with cow counts like so: [1,3,2,1]
# for days 0 to 4 the farms transform in the following manner:
    
#      0  1   2  3  4  5  6  7  8  
#     [0, 2, 1, 1, 0, 0, 0, 0, 0]
#     [0, 0, 2, 0, 1, 0, 1, 0, 0]
#     [0, 0, 0, 0, 2, 0, 2, 0, 1]
#     [0, 0, 0, 0, 0, 0, 4, 0, 4]
#     [0, 0, 0, 0, 0, 0, 8, 0, 8]

def magical_cows(cows, limit, day):
    day_counter = 0
    cows_on_farm = [0 for _ in range(limit+1)]
    for cow_count in cows:
        cows_on_farm[cow_count] +=1
    while day_counter < day:
        index  = limit 
        while index > -1:
            if index * 2 > limit:
                cows_on_farm[index] *= 2
            else:
                cows_on_farm[index*2] += cows_on_farm[index]
                cows_on_farm[index] = 0
            index -=1
        day_counter += 1
    return cows_on_farm, sum(cows_on_farm)
    
        
        

               



if __name__ == "__main__":
    cows = [ 1, 3,2,1]
    c = 8
    print(magical_cows(cows, c, 4))
