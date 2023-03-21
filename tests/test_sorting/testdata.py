# Data that sorts the normal list in ascending order
dataset1 = (
    [1, 60, 14, 45, 4, 31, 20, 90, 11],
    True,
    lambda x: x,
    [1, 4, 11, 14, 20, 31, 45, 60, 90]
)

# Data to get the sorted list in the descending order
dataset2 = (
    [1, 60, 14, 45, 4, 31, 20, 90, 11],
    False,
    lambda x: x,
    [90, 60, 45, 31, 20, 14, 11, 4, 1]
)

# Data containing a list of nested elements to get the list in ascending 
# order based on the size of the element
dataset3 = (
    [{'_id': '123-23-23328371', 'size': 1},
     {'_id': '123-23-23328371', 'size': 60},
     {'_id': '123-23-23328371', 'size': 14},
     {'_id': '123-23-23328371', 'size': 45},
     {'_id': '123-23-23328371', 'size': 4},
     {'_id': '123-23-23328371', 'size': 31},
     {'_id': '123-23-23328371', 'size': 20},
     {'_id': '123-23-23328371', 'size': 90},
     {'_id': '123-23-23328371', 'size': 11}],
    True,
    lambda x: x.get('size'),
    [{'_id': '123-23-23328371', 'size': 1},
     {'_id': '123-23-23328371', 'size': 4},
     {'_id': '123-23-23328371', 'size': 11},
     {'_id': '123-23-23328371', 'size': 14},
     {'_id': '123-23-23328371', 'size': 20},
     {'_id': '123-23-23328371', 'size': 31},
     {'_id': '123-23-23328371', 'size': 45},
     {'_id': '123-23-23328371', 'size': 60},
     {'_id': '123-23-23328371', 'size': 90}]
)

# TODO: Advanced usage datasets