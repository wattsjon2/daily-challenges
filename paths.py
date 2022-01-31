#You are given the array paths, where paths[i] = [cityAi, cityBi] means
#there exists a direct path going from cityAi to cityBi. Return the destination
#city, that is, the city without any path outgoing to another city.
#It is guaranteed that the graph of paths forms a line without any loop, therefore,
#there will be exactly one destination city.
#Example 1:
#Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
#Output: "Sao Paulo" 
#Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the
#destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
#Example 2:
#Input: paths = [["B","C"],["D","B"],["C","A"]]
#Output: "A"
#Explanation: All possible trips are: 
#"D" -> "B" -> "C" -> "A". 
#"B" -> "C" -> "A". 
#"C" -> "A". 
#"A". 
#Clearly the destination city is "A".
#Example 3:
#Input: paths = [["A","Z"]]
#Output: "Z"

def paths(arr):
    starts = set()
    ends = set()

    for i in range(len(arr)):
        starts.add(arr[i][0])
    for i in range(len(arr)):
        ends.add(arr[i][1])

    for end in ends:
        if end not in starts:
            return end


print(paths([["B","C"],["D","B"],["C","A"]]))
print(paths([["A","Z"]]))
print(paths([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

def paths2(arr):
    starts = set()
   

    for i in range(len(arr)):
        starts.add(arr[i][0])

    for i in range(len(arr)):
        if arr[i][1] not in starts:
            return arr[i][1]


print(paths2([["B","C"],["D","B"],["C","A"]]))
print(paths2([["A","Z"]]))
print(paths2([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))