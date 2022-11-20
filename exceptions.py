class BaseFrogException(TypeError):
	def __init__(self,msg,cr):
		if not cr in [0,1,2,3,4]:
			raise RuntimeError("\033[31;1mcr must be 4 or 3 or 2 or 1 or 0.\033[0;0m")
		i=1 if cr==2 else (3 if cr==1 else (6 if cr==0 else (5 if cr==3 else 8)))
		bc=  1 if cr==4 else 0
		msg_bound= "ERROR" if cr==2 else ("WARNING" if cr==1 else ("CRITICAL" if cr==3 else ("DEBUG" if cr==0 else "SUPERCRITICAL")))
		print(f"\033[3{i};4{bc};1m{msg_bound}: Program Failed")


class IterationError(BaseFrogException):
	pass