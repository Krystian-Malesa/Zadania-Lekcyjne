{'id':1, 'value':5},
{'id':2, 'value':3},
{'id':3, 'value':5},
{'id':4, 'value':8},
{'id':5, 'value':3},



def quicksort_dicts(arr, key='value'):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x[key] <= pivot[key]]
    greater = [x for x in arr[1:] if x[key] > pivot[key]]
    return quicksort_dicts(lesser,key) + [pivot] + quicksort_dicts(greater,key)

posortowane_dane = quicksort_dicts(dane)

print("Posortowana lista wleudg 'value': ")
for imte in posortowane_dane:
    print(item)