from .get_time import get_now
from .get_elapsed import get_elapsed
from datetime import timedelta


class Timer:
	def __init__(self, unit='ms', start_now=True):
		self._unit = unit
		self._start_time = None
		self._duration = None
		if start_now:
			self.start()

	def start(self):
		"""
		:rtype: NoneType
		"""
		if self._start_time is not None:
			raise RuntimeError('Timer has already started!')
		self._duration = None
		self._start_time = get_now()

	def pause(self):
		self._duration += self.get_elapsed()
		self._start_time = None

	def reset_timer(self):
		"""
		:rtype: NoneType
		"""
		self._start_time = None

	def get_elapsed(self):
		"""
		:rtype: float or timedelta
		"""
		now = get_now()
		if self._start_time is not None:
			if self._duration is None:
				return get_elapsed(start=self._start_time, end=now, unit=self._unit)
			else:
				return get_elapsed(start=self._start_time, end=now, unit=self._unit) + self.duration
		else:
			raise RuntimeError('Timer is not activated yet!')

	def stop(self):
		"""
		:rtype: NoneType
		"""
		self._duration = self.get_elapsed()
		self.reset_timer()

	@property
	def duration(self):
		"""
		:rtype: float or timedelta
		"""
		return self._duration

	@property
	def unit(self):
		return self._unit
