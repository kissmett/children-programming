text = '''
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
'''
# 统计以上文本中的每个文字出现了多少次
text = text.lower()
text = text.replace('.',' ').replace('(',' ').replace(')',' ').replace('#',' ').replace('/',' ').replace('\'',' ')
wordlist = text.split()
print(wordlist)
# wordset = {'#'}
# for word  in wordlist:
#     wordset.add(word)

wordset = set(wordlist)
print(wordset)
#此时的wordset中是text中不重复的所有单词
wordcountdict = {}
for word in wordset:
    cnt = text.count(word)
    print('{0}:{1}'.format(word,cnt))
    wordcountdict[word] = cnt
print(wordcountdict)    


