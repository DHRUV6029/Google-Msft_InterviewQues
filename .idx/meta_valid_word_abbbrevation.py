class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i , j = 0 , 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i+=1
                j+=1
            else:
                #they are not equal so we need to proceed further only if 
                #abbr[j] is a digit

                if abbr[j].isdigit() and abbr[j]!='0':
                    jumps = 0
                    while j<len(abbr) and abbr[j].isdigit():
                        jumps = jumps * 10 + int(abbr[j])
                        j+=1

                    #now move i pointet jumps forward
                    i = i+jumps-1
                    j-=1
                else:
                    return False
                
                i+=1
                j+=1

            
        return i == len(word) and j == len(abbr)
