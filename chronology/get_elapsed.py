from .get_time import get_now
from datetime import datetime
SECONDS_IN_A_DAY = 60.0 * 60.0 * 24.0


def _get_elapsed(start, end=None):
	"""
	:type start: datetime
	:type end: datetime or NoneType
	:rtype timedelta
	"""
	end = end or get_now()
	return end - start


def get_elapsed_seconds(start, end=None):
	"""
	:type start: datetime
	:type end: datetime or NoneType
	:rtype: float
	"""
	delta = _get_elapsed(start=start, end=end)
	return delta.days*SECONDS_IN_A_DAY + delta.seconds + delta.microseconds / 1E6


def get_elapsed_days(start, end=None):
	"""
	:type start: datetime
	:type end: datetime or NoneType
	:rtype: float
	"""
	delta = _get_elapsed(start=start, end=end)
	return delta.days + delta.seconds/SECONDS_IN_A_DAY + delta.microseconds / 1E6 / SECONDS_IN_A_DAY


def get_elapsed_months(start, end=None):
	"""
	:type start: datetime
	:type end: datetime or NoneType
	:rtype: float
	"""
	end = end or get_now()
	return (end.year - start.year) * 12 + end.month - start.year + (end.day - start.day)/31


def get_elapsed_years(start, end=None):
	"""
	:type start: datetime
	:type end: datetime or NoneType
	:rtype: float
	"""
	return get_elapsed_months(start=start, end=end) / 12


def get_elapsed(start, end=None, unit='timedelta'):
	"""
	:param datetime start: start time
	:param datetime or NoneType end: end time, the current time is used if not provided (None entered)
	:param str unit: one of 'timedelta', 'seconds', 'minutes', 'hours', 'days', 'months', or 'years'
	:rtype: float
	"""

	u = unit[0].lower()
	if u == 't':
		return _get_elapsed(start=start, end=end)
	elif u == 's':
		return get_elapsed_seconds(start=start, end=end)
	elif u == 'd':
		return get_elapsed_days(start=start, end=end)
	elif u == 'm':
		if unit[:2] == 'mi':  		# minutes
			return get_elapsed_seconds(start=start, end=end)/60.0
		elif unit[:2] == 'mo':  	# months
			return get_elapsed_months(start=start, end=end)
		else:
			raise ValueError(f'unit:{unit} is not recognizable.')
	elif u == 'h':
		return get_elapsed_seconds(start=start, end=end)/3600.0
	elif u == 'y':
		return get_elapsed_years(start=start, end=end)
	else:
		raise ValueError(f'unit:{unit} is not recognizable.')
