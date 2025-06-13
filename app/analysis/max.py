import pandas as pd


def compute(series: pd.Series) -> float:
  """Compute the max of a pandas Series.

    Args:
        series (pd.Series): Input series to compute the mean.

    Returns:
        float: The max of the series.

    """
  return series.max()

