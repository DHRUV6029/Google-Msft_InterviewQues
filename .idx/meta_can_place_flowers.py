class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:

                left = True if (i==0 or flowerbed[i-1]==0) else False
                right = True if (i == len(flowerbed)-1 or flowerbed[i+1]==0) else False

                if left and right:
                    flowerbed[i] = 1
                    n-=1

                    if n<=0:return True

        return n == 0
