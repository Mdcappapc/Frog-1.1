from itertools import combinations,starmap
from exceptions import IterationError as ITError
def subsets(string):
	yield ()
	for y in string:
		for i in combinations(string,string.index(y)+1):
			yield i
			
def unique(iterable):
	unlst=[]
	for i in iterable:
		if i not in unlst:
			unlst.append(i)
	return unlst
		
def sym_difference(it1,it2):
	symlist=[]
	for i in it1:
		for j in it2:
			if i not in it2 and j not in it1 and i != j:
				symlist.extend([i,j])
	return unique(symlist)
	
def swap_dict(dic):
	return {v:k for k,v in dic.items()}

def weight_sorter(it,wt):
	return sorted(it,key=lambda x: wt[it.index(x)])
	
def repeated_iters(iterable,repeats):
	res=[]
	for i in range(len(iterable)):
		if repeats[i] is None:
			continue
		for j in range(repeats[i]):
			res.append(iterable[i])
	return res

def iter_count(iterable,func=lambda a:-1):
	return len(filter(iterable,func))
	
def generate(iterable,count=2):
	return [iterable for _ in range(count)]
	
def pop_items_get(iterable):
	it=list(iterable)
	for i in iterable:
		yield it
		it=list(iterable)
		it.pop(0)
def first_last_add(iterable):
	arg_get=[]
	for i,j in zip(iterable,reversed(iterable)):
		arg_get.extend([i,j])
	return arg_get
	
def add_fields(iterable,fields):
	#This function will be removed in Frog 2.2 because you can access it by swap_dict(dict(starzip(iterable,fields)))
	return {k:v for k,v in zip(fields,iterable)}

def flatten(iterable, base_type=None, levels=None):
    def step(node, level):
        if (
            ((levels is not None) and (level > levels))
            or isinstance(node, (bytes))
            or ((base_type is not None) and isinstance(node, base_type))
        ):
            yield node
            return

        try:
            tree = iter(node)
        except TypeError:
            yield node
            return
        else:
            for child in tree:
                yield from step(child, level + 1)

    yield from step(iterable, 0)
    

def starzip(*iterables):
	star=[None]*(len(iterables[0]))
	m=len(star)
	forward=list(flatten(iterables))
	for it in iterables:
		for j in it:
			star[it.index(j)]=tuple(i for i in forward if forward.index(i)%m==it.index(j))
	return star
	
def unzip(it):
	return [*starzip(*it)]	

def get_quantity(lst):
	dc={}
	for it in lst:
		if dc.get(it):
			dc[it]+=1
			continue
		dc[it]=1
	return dc
	#from collections import Counter
	#return dict(Counter(lst).items())
	
def call_repeat(lst):
	return list(flatten([[item]*item for item in lst]))
	
def value_get(dicts,value):
	for key in dicts:
		if dicts[key]==value:
			return key
	
def best_performance(*functions,args=(),kwargs={}):
	perf={}
	for i in functions:
		m=time.time()
		q=i(*args,**kwargs)
		u=time.time()
		perf[i]=(u-m)*10000
	return value_get(perf,min(perf.values())).__name__
	
def sort(arr):    
    for i in range(len(arr)):
        cursor = arr[i]
        pos =i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos -=1
        arr[pos] = cursor

    return arr
    
def double_combine(data):
	for i in data:
		for j in data:
			yield (i,j)
	
def rotate(seq,number):
	do_s=seq+seq
	if number<=len(seq):
		return do_s[number:number+len(seq)]
	else:
		return do_s[number-len(seq):number]