class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        idx2=0
        processed = 0
        for i in range(m+n):
            if idx2>=n:
                break
            if processed == m:
                nums1[i] = nums2[idx2]
                idx2 +=1
                continue
            else:
                max_val = nums1[i]
            if nums1[i]>nums2[idx2]:
                temp = nums1[i]
                nums1[i]=nums2[idx2]
                idx2 += 1
                for j in range(i+1,m+n):
                    next = nums1[j]
                    nums1[j]=temp
                    temp = next
            else:
                processed += 1

sol = Solution()
nums1= [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sol.merge(nums1,1,[-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48],90)
print(nums1)