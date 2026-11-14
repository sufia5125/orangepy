# orangepy
A lightweight health checker for numpy arrays. 

Orangepy inspects numeric and boolean arrays and reports patterns like missing values, infinities, constant columns, and duplicate rows.

## Installation

```bash
pip install orangepy
```

## Example Usage
### In code:

```python
import numpy as np
from orangepy import inspect

data = np.array([
    [1, 5],
    [2, 5],
    [np.nan, 5],
])

report = inspect(data)
print(report.summary())
```

### From CLI:

```bash
orangepy example.npy
```

 Use --json for output in JSON format:

```bash
orangepy example.npy --json
```
## License

MIT

                               /\_/\
                              ( o.o )
                               > ^ <
