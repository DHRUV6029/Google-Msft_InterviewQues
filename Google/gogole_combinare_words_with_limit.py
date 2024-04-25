# Given a String array words contains words and an integer array score contains score of each word such that score[i] represents score of word at ith position. Find the max score you can achieve using the combination of words with following rules :

# you're given limit integer value, the combination of words used to get maxscore cannot exceed the size limit provided in limit value.
# any word can be used multiple times . Eg: words=[sun,moon] score=[5,4] limit=7 then maxscore=10 as the score of combination "sunsun"=5+5=10 and has size 6 which is less than limit 7, hence condition is satisfied.
# words are allowed to overlap and form new word. After overlap, the new word can have combined power.
# Eg. words=[energy, green] score=[4,3] limit=9 then we can use new formed word greenergy with score value =(4+3)=7 here maxscore=7 as greenergy having score=7 and size=9 can be used here
# Sample Input



 n=2 words=["pack", "acknowledge", "edged"] score=[2,12,3] limit=13