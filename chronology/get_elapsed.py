from .get_time import get_now
SECONDS_IN_A_DAY = 60.0 * 60.0 * 24.0

def _get_elapsed(start, end=None):
	end = end or get_now()
	return end - start

def get_elapsed_seconds(start, end=None):
	delta = _get_elapsed(start=start, end=end)
	return delta.days*SECONDS_IN_A_DAY + delta.seconds + delta.microseconds / 1E6

def get_elapsed_days(start, end=None):
	delta = _get_elapsed(start=start, end=end)
	return delta.days + delta.seconds/SECONDS_IN_A_DAY + delta.microseconds / 1E6 / SECONDS_IN_A_DAY

def get_elapsed(start, end=None, unit='timedelta'):
	"""
	:param datetime.datetime start: start time
	:param datetime.datetime or NoneType end: end time, the current time is used if not provided (None entered)
	:param str unit: one of 'timedelta', 'seconds', 'minutes', 'hours', 'days'
	:rtype: float
	"""

	u = unit[0].lower()
	if u=='t':
		return _get_elapsed(start=start, end=end)
	elif u=='s':
		return get_elapsed_seconds(start=start, end=end)
	elif u=='d':
		return get_elapsed_days(start=start, end=end)
	elif u=='m':
		return get_elapsed_seconds(start=start, end=end)/60.0
	elif u=='h':
		return get_elapsed_seconds(start=start, end=end)/3600.0
	else:
		raise ValueError(f'unit:{unit} is not recognizable.')