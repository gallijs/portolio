# portolio

Will be a financial portfolio optimizer.

### First iteration:

* Read stock prices in csv format from a given directory.
* Plot their price from the given start date to end date.
* Option to normalize price.

## Usage
```bash
$ portolio -h
usage: portolio [-h] [-v] [-n] portfolio_directory start_date end_date

Portolio is a portfolio optimizer.

positional arguments:
  portfolio_directory  path to stock csv files
  start_date           start date
  end_date             end date

optional arguments:
  -h, --help           show this help message and exit
  -v, --version        show program's version number and exit
  -n, --normalize      normalize stock prices
```

#### Plots stock prices 
```bash
$ portolio test_data 2016-01-01 2017-01-01
```

#### Plots normalized prices 
```bash
$ portolio -n test_data 2016-01-01 2017-01-01
```
