# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def count(cars):
    """
    Count the occurences of each item in a text file.
    
    Parameters
    ----------
    
    file = enter file you want to count
    
    Returns
    -------
    List with items + number
    
    """
    

    itemcount={}
    for item in cars:
        if item  in itemcount.keys():
            itemcount[item] += 1
        else:
            itemcount[item] = 1
    print (item,itemcount)