<p align="center"><img src="https://raw.githubusercontent.com/ryan-byrne/pycobb/main/files/pycobb.png" width="200"/><p>

* [Report Issues and Bugs](https://github.com/ryan-byrne/pycobb/issues/)
* Check out the [Documentation](https://pycobb.readthedocs.io/en/latest/)

## Installation

With PIP:

```
pip install pycobb
```
From source:

```
git clone https://github.com/ryan-byrne/pycobb
cd pycobb
python install setup.py
```

## Usage

### Python

The `pycobb` [Python Package](https://pypi.org/project/pycobb/) and it's associated functions can be easily imported into an existing Python Project.

```python

import pycobb

df = pycobb.get(pitchers=["Trevor Bauer"], batters=["Javier Baez"], years=[2018,2019])

```

This `pycobb.get()` returns a [pandas DataFrame](https://pandas.pydata.org/) with stats on every pitch **Trevor Bauer** threw to **Javier Baez** in the **2018** and **2019** seasons.

### Command Line Interface (CLI)

`pycobb` can return that same DataFrame from the command line. The option `--print` prints the DataFrame to the console:

```
pycobb get -p Trevor+Bauer -b Javier+Baez -y 2019 --print
```
Returns:

```
  pitch_type   game_date  release_speed  ...  spin_axis  delta_home_win_exp delta_run_exp
0         SL  2019-08-09           78.2  ...         80               0.058        -0.514
1         SL  2019-08-09           79.3  ...         81               0.000        -0.084
2         SL  2019-08-09           79.4  ...         87               0.046        -0.382
3         SL  2019-08-09           78.7  ...         81               0.020        -0.319
4         FC  2019-08-09           81.0  ...         68               0.000        -0.091
5         FF  2019-08-09           94.7  ...        202               0.000         0.121
6         FC  2019-08-09           81.7  ...         55               0.000         0.054
7         FC  2019-08-09           82.2  ...         70               0.000        -0.050
8         SL  2019-08-09           78.4  ...         79               0.000         0.037

[9 rows x 92 columns]
```

### Additional Search Parameters

For a full list of search parameters, [review the documentation](example.com)
