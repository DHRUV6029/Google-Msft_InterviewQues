def computeLps(pattern):
            M = len(pattern)
            lps = [0] * M
    
    
            length = 0  
            i = 1

    
            while i < M:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
    
        def kmp(pat , txt, lps):
            M = len(pat)
            N = len(txt)

    

            result = []

            i = 0 
            j = 0  
            while (N - i) >= (M - j):
                if pat[j] == txt[i]:
                    j += 1
                    i += 1

                if j == M:
                    result.append(i - j )
                    j = lps[j - 1]
                elif i < N and pat[j] != txt[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return result
