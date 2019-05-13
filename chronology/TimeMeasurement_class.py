from datetime import timedelta


class TimeMeasurement:
	def __init__(self, duration=None, unit='ms', count=1):
		self._duration = duration or timedelta()
		self._count = count
		self._unit = unit

	@property
	def duration(self):
		return self._duration

	@property
	def count(self):
		return self._count

	@property
	def unit(self):
		return self._unit

	def add_duration(self, duration):
		self._duration += duration
		self._count += 1

	@property
	def mean_duration(self):
		return self._duration / self._count

	def copy(self):
		return self.__class__(duration=self.duration, count=self.count)

	def __str__(self):
		return f'count:{self.count} - duration:{self.duration}'

	def __add__(self, other):
		if self.unit != other.unit:
			raise TypeError('Cannot add durations with different units!')

		if other is None or other == 0:
			return self.copy()
		return self.__class__(duration=self.duration + other.duration, count=self.count + other.count)

	def __sub__(self, other):
		if self.unit != other.unit:
			raise TypeError('Cannot subtract durations with different units!')

		if other is None or other == 0:
			return self.copy()
		return self.__class__(duration=self.duration - other.duration, count=self.count - other.count)
