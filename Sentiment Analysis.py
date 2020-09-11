punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char,"")
    return str1
def get_pos(str1):
    a = str1.lower()
    a = strip_punctuation(a)
    lst = a.split(" ")
    #print(a)
    p_count = 0
    for word in positive_words:
        for x in lst:
            if word == x:
                p_count += 1
    return p_count
def get_neg(str1):
    b = str1.lower()
    b = strip_punctuation(b)
    lst = b.split(" ")
    #print(b)
    n_count = 0
    for word in negative_words:
        for x in lst:
            if word == x:
                n_count += 1
    return n_count

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def run(file):
    csvFile = open(file, 'r')
    lines = csvFile.readlines()
    
    lines = lines[1:]
    neg_count = []
    pos_count = []
    wordList = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[0]
        wordList.append(i)
    for i in wordList:
        neg_count.append(get_neg(i))
        pos_count.append(get_pos(i))
    res = ['retweet_count,reply_count,pos_count,neg_count,score']
    
    res = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[1:]
        res.append(i)
    temp = []
    for i in res:
        i = list(map(int, i))
        temp.append(i)
    res = temp
    for i in range(len(res)):
        res[i].append(pos_count[i])
        res[i].append(neg_count[i])
        res[i].append(pos_count[i] - neg_count[i])
        
    temp = []
    for i in res:
        temp.append(','.join('%s' %id for id in i))
    res = temp
    
    res.insert(0, "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    print(res)
    res = '\n'.join('%s' % id for id in res)
    with open("resulting_data.csv", 'w') as csvFile:
        write = csvFile.write(res)


if __name__ == '__main__':
    run('project_twitter_data.csv')