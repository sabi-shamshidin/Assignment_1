# Assignment_1
Assignment 1, Python

## Title

You are now in my repository, which is dedicated to the first assignment in the python course. 
The assignment was to write a Python code which 
* Pulls the data from coingecko.com
* Filters out top N cryptocurrencies by market capitalization 

The work was done by a second year student from SE-2008 group - Shamshidin Sabina.

## Installation

### For this assignment, I installed two libraries:

#### CoinGecko

PyPl
```terminal
pip3 install pycoingecko
```

or from source

```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```
#### and Pandas

Pypl
```terminal
pip3 install pandas
```
## Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

import pandas
```
## Examples

The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.
Any optional parameters can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

For any parameter:

* Lists are supported as input for multiple-valued comma-separated parameters (e.g. see /simple/price usage examples).

* Booleans are supported as input for boolean type parameters; they can be str ('true', 'false'') or bool (True, False) (e.g. see /simple/price usage examples).

#### Usage examples:

```python
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')
{'bitcoin': {'usd': 3461.27}, 'ethereum': {'usd': 106.92}, 'litecoin': {'usd': 32.72}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])
{'bitcoin': {'usd': 3459.39, 'eur': 3019.33}, 'ethereum': {'usd': 106.91, 'eur': 93.31}, 'litecoin': {'usd': 32.72, 'eur': 28.56}}

# optional parameters can be passed as defined in the API doc (https://www.coingecko.com/api/docs/v3)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
# OR (also booleans can be used for boolean type arguments)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
```
