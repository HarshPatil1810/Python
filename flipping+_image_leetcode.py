class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            r.reverse()
            for i in range(len(r)):
                r[i]=1-r[i]
                
        return image
