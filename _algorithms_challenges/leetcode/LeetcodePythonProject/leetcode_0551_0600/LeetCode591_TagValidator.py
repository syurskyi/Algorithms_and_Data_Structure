'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        import re
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
