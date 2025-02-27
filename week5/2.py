def merge_dicts(d1, d2):
   #your code goes here
    for key,value in d2.items() :
      if key in d1 : 
        d1[key] += value
      else :
        d1[key] = value
    
    return d1