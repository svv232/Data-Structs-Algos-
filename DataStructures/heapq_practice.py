#using the python heapq class to build solve problem set involving 
#passengers and an airline

import heapq
class Passenger:
	def __init__(self,fn,ln,status,fair,bags):
		self._fn = fn
		self._ln = ln
		self._status = status
		self._fair = fair
		self._bags = bags
class Flight:
	def __init__(self,capacity):
		self._capacity = capacity
		self._passengers = []
		self._finalize = False

	def _value_hash(self, passenger):
		status =  ("None","Gold","Silver","Platinum","1K","Global Services","Employee")
		return (status.index(passenger._status),passenger._bags,passenger._fair,passenger)

	def finalize(self): self._finalize = True

	def board(self, passenger):
		if self._finalize: raise ValueError("I DON'T CARE IF YOU HAVE DYING PATIENTS")
		heapq.heappush(self._passengers,self._value_hash(passenger))

	def whoToRemove(self):
		ls = []
		if self._finalize:
			while len(self._passengers) > self._capacity:
				heap = heapq.heappop(self._passengers)[-1]
				ls.append(heap._fn+" "+heap._ln)
			return ls
		raise ValueError("I am not finalized")
