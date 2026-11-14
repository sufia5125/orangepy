import numpy as np
from numpy.typing import ArrayLike
from orangepy.report import ArrayReport

def inspect(array :ArrayLike) -> ArrayReport:
    """insepct without modifying the array"""
    data = np.asarray(array)
    is_numeric = (
        np.issubdtype(data.dtype, np.number)
        or np.issubdtype(data.dtype, np.bool_)
    ) 
    if not is_numeric:
        raise TypeError(
            "Only numeric and boolean arrays are supported."
        )
        
    nan_count = int(np.isnan(data).sum())
    infinite_count = int(np.isinf(data).sum())
    
    constant_columns = []
    duplicate_rows=0
    if data.ndim ==2:
        for col_index in range(data.shape[1]):
            column = data[:, col_index]
            
            if column.size ==0:
                continue
            
            if np.all(np.isfinite(column)) and np.all(
                column == column[0]
            ):
                constant_columns.append(col_index)        
        if data.shape[0] > 1:
           _, counts = np.unique(
               data, axis=0, return_counts=True
           )
           duplicate_rows = int(np.sum(counts - 1))
           
    return ArrayReport(
        shape=data.shape,
        dtype=str(data.dtype),
        size=int(data.size),
        nan_count=nan_count,
        infinite_count=infinite_count,
        constant_columns=tuple(constant_columns),
        duplicate_rows=duplicate_rows,
    )
