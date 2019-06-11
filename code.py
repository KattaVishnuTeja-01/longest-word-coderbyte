def LongestWord(sen): 

    # code goes here 
    sen = sen.split()
    max = 0
    for i in sen:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        l = 1
        for j in punctuations:
            
            if j in i:
                l = 0
                continue
            
        if l == 0:
            continue
        if len(i) > max:
            x = i
            max = len(i)
    
    
    return x
    
# keep this function call here  
x = raw_input()
print(LongestWord(x))
