'''
Created on May 21, 2018

@author: tongq
'''
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2: return 0
        arr1, arr2 = version1.split('.'), version2.split('.')
        m, n = len(arr1), len(arr2)
        i, j = 0, 0
        while i < m and j < n:
            if int(arr1[i]) > int(arr2[j]):
                return 1
            elif int(arr1[i]) < int(arr2[j]):
                return -1
            else:
                i += 1
                j += 1
        while i < m and int(arr1[i]) == 0:
            i += 1
        while j < n and int(arr2[j]) == 0:
            j += 1
        if i == m and j == n:
            return 0
        elif i == m:
            return -1
        else:
            return 1
