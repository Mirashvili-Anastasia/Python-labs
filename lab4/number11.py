def intersect_recursive(list1, list2, result=None, index=0):
    if result is None:
        result = []
    
    if index >= len(list1):
        return result
    
    current_element = list1[index]
    
    if current_element in list2 and current_element not in result:
        result.append(current_element)
    
    return intersect_recursive(list1, list2, result, index + 1)

print(intersect_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8]))
print(intersect_recursive([5, 8, 2], [2, 9, 1]))
print(intersect_recursive([5, 8, 2], [7, 4]))