# Chronology
Chronology is a Python library for dealing with time (and date).

## Installation
```bash
pip install chronology
```

## Usage

### *get_elapsed*
The *get_elapsed* method measures the elapsed time from *start* to *end* 
in one of the following units: seconds, minutes, hours, or days.

```python
from chronology import get_elapsed
from datetime import datetime
start_time = datetime.strptime('Mar 6 2019  1:33AM', '%b %d %Y %I:%M%p')
end_time = datetime.strptime('Mar 8 2019  1:32AM', '%b %d %Y %I:%M%p')

get_elapsed(start=start_time, end=end_time)
# output: datetime.timedelta(1, 86340)

get_elapsed(start=start_time, end=end_time, unit='seconds')
# output: 172740.0

get_elapsed(start=start_time, end=end_time, unit='hours')
# output: 47.983333333333334
```



