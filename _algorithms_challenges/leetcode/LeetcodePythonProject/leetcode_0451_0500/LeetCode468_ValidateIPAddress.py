'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if ':' in IP and self.checkIP6(IP):
            return 'IPv6'
        elif '.' in IP and self.checkIP4(IP):
            return 'IPv4'
        return 'Neither'
    
    def checkIP4(self, ip):
        arr = ip.split('.')
        if len(arr) != 4: return False
        for elem in arr:
            if not elem: return False
            if elem.startswith('0') and len(elem) > 1: return False
            if not elem.isdigit() or int(elem) > 255:
                return False
        return True
    
    def checkIP6(self, ip):
        arr = ip.split(':')
        if len(arr) != 8: return False
        digits = set(list('0123456789abcdefABCDEF'))
        for i, elem in enumerate(arr):
            if i > 0 and len(elem) > 4: return False
            if i == 0 and len(elem) > 4:
                if elem[:len(elem)-4] != '0'*(len(elem)-4):
                    return False
            if not elem: return False
            for c in elem:
                if c not in digits:
                    return False
        return True
