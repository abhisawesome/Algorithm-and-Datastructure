# [5,6,2,4,8]
 
#     1
#     1
#  1ww1
# 11ww1
# 11w11
# 11w11
# 11111
# 11111

# Output index:2 water level 4

def findLargest(inputIndex):
    inp = inputIndex[:]
    max1 = max(inp)
    inp.remove(max1)
    max2 = max(inp)
    return max1,max2
def findWaterLevel(inputIndex,max1,max2):
    indexMax1 = inputIndex.index(max1)
    indexMax2 = inputIndex.index(max2)
    if(indexMax1>indexMax2):
        indexMax1,indexMax2 = indexMax2,indexMax1
    maxWater= 0
    index = None
    for height in inputIndex[indexMax1+1:indexMax2]:
        if((max2-height) > maxWater):
            maxWater = max2-height
            index = inputIndex.index(height)
    return maxWater,index
        

inputValue = [5,6,2,4,8]

max1,max2 = findLargest(inputValue)
print('result(max water level,index)',findWaterLevel(inputValue,max1,max2))

