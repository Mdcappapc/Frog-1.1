from dataclasses import dataclass,field
from typing import Tuple
from array import array
from abc import ABC,ABCMeta,abstractmethod
from math import prod
from random import randint
from functools import partial,update_wrapper,wraps
from copy import copy,deepcopy
from exceptions import *
from fractions import Fraction as BaseFraction

class __saver(ABC,metaclass=ABCMeta):
	"""
		Id saver for classes. You Cannot make Instance from this class.
	"""
	@abstractmethod
	def __init__(self):
		pass
	identifiers=array("h",[])
	clone_maker=lambda a:deepcopy(a)
	clone_make_flow=partial(clone_maker)
	update_wrapper(clone_make_flow,clone_maker)
class Math:
	"""
		Class for mathematical operations.
	
	"""
	def multiply(self,a,b):
		return a*b
		
	def divide(self,a,b,round=False):
		return a/b if not round else a//b
		
	def add(self,a,b):
		return a+b
		
	def subtract(self,a,b,absolute=False):
		return a-b if not absolute else (a-b if a>b else b-a)
		
	def power(self,a,b,c=1):
		return (a**b)%c
		
	def root(self,a,b=2):
		return a**(1/b)
		
	def pythagorean(self,a,b):
		return (a**2+b**2)**(1/2)
		
	def factorial(self,a):
		return math.prod(range(1,a))
	
	def log(self,a,base):
		for i in range(a):
			if pow(base,i)==a:
				return i
	
	

@dataclass(order=True)
class Number:
    """
    	Class for numbers like builtin <int> class.
    
    """
    m=0
    value:int

    def __new__(cls,*args,**kwargs):
        cls.m+=1
        return super().__new__(cls)
    def __add__(self,other):
        return self.value+other.value
    def __sub__(self,other):
        return self.value-other.value
    def __mul__(self,other):
        return self.value*other.value
    def __truediv__(self,other):
        return self.value/other.value
    def __floordiv__(self,other):
        return self.value//other.value
    def __pow__(self,other):
        return pow(self.value,other.value)
    def __ne__(self,other):
        return self.value != other.value and self.__class__ == other.__class__
    def __iadd__(self,other):
        return Number(self.value+other.value)
    def __isub__(self,other):
        return Number(self.value-other.value)
    def __imul__(self,other):
        return Number(self.value*other.value)
    def __itruediv__(self,other):
        return Number(self.value/other.value)
    def __ifloordiv__(self,other):
        return Number(self.value//other.value)
    def __ipow__(self,other):
        return Number(self.value**other.value)
    def __bool__(self):
        return self.value!=0
        
class Fraction(BaseFraction):
  	def __repr__(self):
  		return ("{}\n_\n\n{}".format(self.numerator,self.denominator))
  	
@dataclass(order=True)
class Point:
	"""
		Class For points in Cartesian coordinate system diagram.
	
	"""
	___id: int =field(init=False,compare=False,repr=False)
	
	x: int = 0
	y: int = 0
	def __post_init__(self):
		id=self.__set_id()
		while not id:
			id=self.__set_id()
		self.t_pointer : Tuple=(self.x,self.y)
	def __set_id(self):
		id=randint(-32768,32768)
		ids=__saver.identifiers
		if id not in ids:
			ids.append(id)
			self.___id=id
			return id
		return False
	def __sub__(self,other):
		x_dis=abs(self.x-other.x)
		y_dis=abs(self.y-other.y)
		dist=Math.pythagorean(self,x_dis,y_dis)
		return Number(dist)

class Vector:
		"""
			Class for Vectors in Cartesian Coordinate System.
		"""
		def __init__(self,*,head:Point,tail:Point,ht=False):
			if ht:
				self.head=head
				self.tail=tail
				x_line:Number=Number(abs(self.head.x-self.tail.x))
				y_line:Number=Number(abs(self.tail.y-self.head.y))
			else:
				self.x_line=head
				self.y_line=tail
			
		def __repr__(self):
			return f"{self.__class__.__name__}(x={self.x_line},y={self.y_line})"
		def __eq__(self,other):
			return self.y_line==other.y_line and self.x_line == other.x_line and type(self) == type(other)
		def __reversed__(self):
			return self.__class__(x_line=self.x_line*-1,y_line=self.y_line*-1)
			
		def __add__(self,other):
			new_v=Vector(x_line=self.x_line+other.x_line,y_line=self.y_line+other.y_line)
			return new_v
		
		def __sub__(self,other):
			return self+reversed(other)
			
		def __mul__(self,other):
			return Number((self.x_line*other.x_line)+(self.y_line*other.y_line))

class NumArray:
	"""
		Array Class for nums with methods:
			add(item,end=True)
			pin(item,start=True)
			remove(index)
			clear()
			Supports Mathematical operations.
	"""
	def __init__(self,nums):
		self.items=__saver.clone_maker(nums)
		
	def __repr__(self):
		return f"{self.__class__.__name__}({self.items})"
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
		
	def __add__(self,other):
		ilen=[]
		for i in range(len(self.items)):
			ilen[i]=self.items[i]+other.items[i]
		return ilen
		
	def __mul__(self,other):
		ilen=[]
		for i in range(len(self.items)):
			ilen[i]=self.items[i]*other.items[i]
		return ilen
		
	def __truediv__(self,other):
		ilen=[]
		for i in range(len(self.items)):
			ilen[i]=self.items[i]/other.items[i]
		return ilen
		
	def __floordiv__(self,other):
		ilen=[]
		for i in range(len(self.items)):
			ilen[i]=self.items[i]//other.items[i]
		return ilen
		
	def __pow__(self,other):
		ilen=[]
		for i in range(len(self.items)):
			ilen[i]=self.items[i]**other.items[i]
		return ilen
class NumQueue:
    """
		Queue Class for nums with methods:
			enqueue(item,end=True)
			dequeue(end=True)
	"""
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
            print("Empty queue")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"NumQueue({self.__items})"
        
class NumStack:
    """
		Stack Class for nums with methods:
			push(item,start=True)
			pop(index,start=True)
	"""
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
            print("Empty stack")

    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"NumStack({self.__items})"			