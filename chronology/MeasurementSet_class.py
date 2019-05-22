from .TimeMeasurement_class import TimeMeasurement
from .measure_function import measure

from pandas import DataFrame


class MeasurementSet:
	def __init__(self):
		self._measurements = {}

	def __str__(self):
		return '\n'.join([f'{name} - {measurement}' for name, measurement in self._measurements.items()])

	def __getstate__(self):
		return self._measurements

	def __setstate__(self, state):
		self._measurements = state

	@property
	def measurements(self):
		"""
		:rtype: dict[str, TimeMeasurement]
		"""
		return self._measurements

	def __add__(self, other):
		"""
		:type other: MeasurementSet
		:rtype: MeasurementSet
		"""
		result = self.__class__()
		for name in set(self.measurements.keys()).union(other.measurements.keys()):

			if name in self.measurements and name in other.measurements:
				result.measurements[name] = self.measurements[name] + other.measurements[name]

			elif name in self._measurements:
				result.measurements[name] = self.measurements[name].copy()

			else:
				result.measurements[name] = other.measurements[name].copy()

		return result

	def add_measurement(self, name, timer):
		"""
		:param str name:
		:param Timer timer:
		"""
		if name in self.measurements:
			self.measurements[name] += TimeMeasurement(duration=timer.duration, unit=timer.unit)
		else:
			self.measurements[name] = TimeMeasurement(duration=timer.duration, unit=timer.unit)

	@property
	def summary_data(self):
		"""
		:rtype: DataFrame
		"""
		names = []
		total_durations = []
		units = []
		counts = []
		for name, measurement in self.measurements.items():
			names.append(name)
			total_durations.append(measurement.duration)
			units.append(measurement.unit)
			counts.append(measurement.count)

		data = DataFrame({'name': names, 'total_duration': total_durations, 'unit': units, 'count': counts})
		data['mean_duration'] = data['total_duration'] / data['count']

		return data.sort_values('total_duration', ascending=False).reset_index(drop=True)

	def measure(self, function, name, unit='ms'):
		"""
		:param callable function: function to be timed
		:type name: str
		:type unit: str
		:rtype: callable
		"""
		return measure(measurement_set=self, function=function, name=name, unit=unit)
