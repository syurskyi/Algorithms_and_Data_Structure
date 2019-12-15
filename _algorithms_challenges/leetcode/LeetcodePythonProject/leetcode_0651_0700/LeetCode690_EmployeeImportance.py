'''
Created on Oct 24, 2017

@author: MT
'''
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        hashmap = {}
        for emp in employees:
            hashmap[emp.id] = hashmap.get(emp.id, []) + [emp]
        queue = []
        for emp in employees:
            if emp.id == id:
                queue.append(emp)
        res = 0
        while queue:
            emp = queue.pop(0)
            subs = emp.subordinates
            res += emp.importance
            for sub in subs:
                queue += hashmap.get(sub, [])
        return res
