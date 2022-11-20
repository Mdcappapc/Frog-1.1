from copy import deepcopy
from pprint import pprint
from exceptions import IterationError as ItError
from functions import value_get
from collections import namedtuple,OrderedDict
print=ItError
class ZigZag:
	def __init__(self,l1,l2):
		self.queue=[l1,l2]
	def __repr__(self):
		return f"<{self.__class__.__name__} Object>"
	def next(self):
		v=self.queue.pop(0)
		r=v.pop(0)
		if v:
			self.queue.append(v)
		return r
	def hasnext(self):
		return bool(self.queue)
		
class Array:
	def __init__(self,nums):
		self.items=deepcopy(nums)
		
	def __repr__(self):
		return f"<{self.__class__.__name__} {self.items}>"
	def add(self,item,end=True):
		if end:
			self.items.append(item)
		else:
			self.items=[m]+self.items
	
	def pin(self,item,start=True):
		if not start:
			m=self.items.pop(self.items.index(item))
			self.items.append(m)
		else:
			m=self.items.pop(self.items.index(item))
			self.items=[m]+self.items
			
	def remove(self,index):
		m=self.items.index(index)
		self.items.remove(m)
		return m
	
	def clear(self):
		self.items=[]
class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item,end=True):
        if end:
        	self.__items.append(item)
        	return
        self.__items=[item]+self.__items
        

    def dequeue(self,end=True):
        try:
            return self.__items.pop() if end else self.__items.pop(0)
        except IndexError:
            raise print("Empty queue")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"<Queue {self.__items}>"
        
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item,start=True):
        if start:
        	self.__items=[item]+self.__items
        	return
        self.__items.append(item)

    def pop(self,start=True):
        try:
            return self.__items.pop()  if not start else self.__items.pop(0)
        except IndexError:
            raise print("Empty stack")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"<Stack {self.__items}>"
        
        
class MissDict(OrderedDict,dict):
	def __init__(self,**kwargs):
		self.__cat=kwargs
	def __missing__(self,key):
		return None
	def __repr__(self):
		return f"<{self.__class__.__name__} {self._as_dict()}>"	
	def value_get(self,v):
		return value_get(self,v)
		
	def hasvalue(self,val):
		return val in self.values()
		
	def haskey(self,key):
		return key in self.keys()
		
	def _as_dict(self):
		return self.__cat
		
		
FlowTuple=namedtuple