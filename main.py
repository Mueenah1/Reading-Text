# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open('./story.txt', 'r') as file_story:
        read_file = file_story.read()
    return read_file
    
    

    
    #return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split = text.split()
    #print(split)
    count ={}
    for i in split:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(count_words())

    #return {"as": 10, "would": 20}