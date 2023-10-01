"""main file where all test code is run from""" 
import time
import sys
from hashmap import HashMap
class FunctionHits:
    """keeps track of how many function calls there are"""     
    def __init__(self, count=0):
        self.count = count

class CacheHits:
    """keeps track of how many cache hits there are"""    
    def __init__(self, count=0):
        self.count = count

cache = HashMap() 
function_hits = FunctionHits() 
cache_hits = CacheHits()
ROW = sys.argv[1]

def weight_on(r,c):
    """calculates the wait on a person in a specified row and column"""
    function_hits.count += 1
    second_person = 200
    if c - 1 < 0 or c > r - 1 :
        second_person = 0
    if c < 0 or c > r:
        return 0
    if r <= 0:
        return 0
    try:
        cache_hits.count += 1
        return cache.get((r,c))
    except:
        cache_hits.count -= 1
        new_weight = (second_person + 200 + weight_on(r - 1,c - 1) + weight_on(r - 1,c))/2
        cache.set((r,c), new_weight)
        return new_weight

master_list = []
start_time = time.time()
for i in range(int(ROW)):
    something = []
    for x in range(int(ROW)):
        yes = int(i)
        no = int(x)
        if i >= x:
            something.append(round(weight_on(yes, no), 2))     
    master_list.append(something)

end_time = time.time()

for lists in master_list:     
    print(*lists)

print("\nElapsed time: " + str(end_time - start_time) + " Seconds") 
print("Number of function calls: " + str(function_hits.count)) 
print("Number of cache hits: " + str(cache_hits.count))