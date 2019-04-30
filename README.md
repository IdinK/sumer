# Chronology
Chronology is a Python library for dealing with time (and date).

## Installation
```bash
pip install chronology
```

## *get_number_of_days*
It returns the number of days in a month or a year. 
If month is not given, the function returns the number of days in a year.

```python
from chronology import get_number_of_days
get_number_of_days(year=2020)
```
```json
366
```

```python
from chronology import get_number_of_days
get_number_of_days(year=2020, month=2)
```
```json
29
```

## *get_elapsed*
The *get_elapsed* method measures the elapsed time from *start* to *end* 
in one of the following units: seconds, minutes, hours, days, months, or years.

```python
from chronology import get_elapsed
from datetime import datetime
start_time = datetime.strptime('Mar 6 2019  1:33AM', '%b %d %Y %I:%M%p')
end_time = datetime.strptime('Mar 8 2019  1:32AM', '%b %d %Y %I:%M%p')
get_elapsed(start=start_time, end=end_time)
```
```json
datetime.timedelta(1, 86340)
```

```python
get_elapsed(start=start_time, end=end_time, unit='seconds')
```
```json
172740.0
```

```python
get_elapsed(start=start_time, end=end_time, unit='hours')
```
```json
47.983333333333334
```




