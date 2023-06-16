from sys import argv

if len(argv) == 1 :
    print("Hello, world!")
    
elif argv[1].endswith(".txt") :
    with open(argv[1]) as f:
        words = f.read()
        words = words.split()
        counts = dict()
        for word in words :
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1
    #print(counts)
    for i,word in enumerate(counts) :
        word = word.lower()
        print(i+1,"-",word,":",counts[word])
    
elif len(argv) == 2 :
    print(argv[1][::-1])

