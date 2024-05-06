# asgmt-5-programming-design-2024
Assignment 5: Programming Design 2024.

## 01. Define a class `SquareSqrtArgs` which instantiates objects with two methods `square_args()` and `sqrt_args()` that take flexible integers and returns their squared and square-root values in a `list`.

```python
class SquareSqrtArgs:
    """
    >>> square_sqrt_args = SquareSqrtArgs()
    >>> type(square_sqrt_args)
    '__main__.SquareSqrtArgs'
    >>> square_sqrt_args.square_args(0, 1, 2)
    [0, 1, 4]
    >>> square_sqrt_args.sqrt_args(0, 1, 4)
    [0.0, 1.0, 2.0]
    >>> square_sqrt_args.square_args(3, 4, 5)
    [9, 16, 25]
    >>> square_sqrt_args.sqrt_args(9, 16, 25)
    [3.0, 4.0, 5.0]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `MinMaxFinder` instantiates objects with 1 attribute `integer_list` and 4 methods `find_min()`, `find_max()`, `find_idxmin()`, and `find_idxmax()`.

```python
class MinMaxFinder:
    """
    >>> min_max_finder = MinMaxFinder([2, 3, 5, 7, 11, 11, 7, 5, 3, 2])
    >>> min_max_finder.integer_list
    [2, 3, 5, 7, 11, 11, 7, 5, 3, 2]
    >>> min_max_finder.find_min()
    2
    >>> min_max_finder.find_max()
    11
    >>> min_max_finder.find_idxmin()
    [0, 9]
    >>> min_max_finder.find_idxmax()
    [4, 5]
    >>> min_max_finder = MinMaxFinder([10, 9, 8, 6, 4, 1, 1, 4, 6, 8, 9, 10])
    >>> min_max_finder.integer_list
    [10, 9, 8, 6, 4, 1, 1, 4, 6, 8, 9, 10]
    >>> min_max_finder.find_min()
    1
    >>> min_max_finder.find_max()
    10
    >>> min_max_finder.find_idxmin()
    [5, 6]
    >>> min_max_finder.find_idxmax()
    [0, 11]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class `CommonDivisors` which instantiates objects with 2 attributes `x_divisors` and `y_divisors`, and 1 method `get_common_divisors()`.

```python
class CommonDivisors:
    """
    >>> cd = CommonDivisors(3, 6)
    >>> cd.x_divisors
    {1, 3}
    >>> cd.y_divisors
    {1, 2, 3, 6}
    >>> cd.get_common_divisors()
    {1, 3}
    >>> cd = CommonDivisors(4, 8)
    >>> cd.x_divisors
    {1, 2, 4}
    >>> cd.y_divisors
    {1, 2, 4, 8}
    >>> cd.get_common_divisors()
    {1, 2, 4}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `PrimeJudger` which instantiates objects with 2 methods `get_divisors()` and `is_prime()`.

```python
class PrimeJudger:
    """
    >>> pj = PrimeJudger(1)
    >>> pj.get_divisors()
    {1}
    >>> pj.is_prime()
    False
    >>> pj = PrimeJudger(2)
    >>> pj.get_divisors()
    {1, 2}
    >>> pj.is_prime()
    True
    >>> pj = PrimeJudger(4)
    >>> pj.get_divisors()
    {1, 2, 4}
    >>> pj.is_prime()
    False
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `import_zip_codes_json()` which imports the `zip_codes.json` as a `list` in working directory.

```python
def import_zip_codes_json() -> list:
    """
    >>> zip_codes_json = import_zip_codes_json()
    >>> type(zip_codes_json)
    list
    >>> len(zip_codes_json)
    378
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `lookup_zip_code()` which returns the 3-digit zip code in integer format given the name of county and town in Taiwan, based on `zip_codes.json` in working directory.

```python
def lookup_zip_code(county: str, town: str) -> int:
    """
    >>> lookup_zip_code("臺北市", "中正區")
    100
    >>> lookup_zip_code("基隆市", "中正區")
    202
    >>> lookup_zip_code("臺北市", "中山區")
    104
    >>> lookup_zip_code("基隆市", "中山區")
    203
    >>> lookup_zip_code("臺北市", "大安區")
    106
    >>> lookup_zip_code("臺中市", "大安區")
    439
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `lookup_county_town()` which returns the the name of county and town in Taiwan given 3-digit zip code in integer format, based on `zip_codes.json` in working directory.

```python
def lookup_county_town(zip_code: int) -> tuple:
    """
    >>> lookup_county_town(100)
    ('臺北市', '中正區')
    >>> lookup_county_town(202)
    ('基隆市', '中正區')
    >>> lookup_county_town(104)
    ('臺北市', '中山區')
    >>> lookup_county_town(203)
    ('基隆市', '中山區')
    >>> lookup_county_town(106)
    ('臺北市', '大安區')
    >>> lookup_county_town(439)
    ('臺中市', '大安區')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `import_countries_json()` which imports the `countries.json` as a `list` in working directory.

```python
def import_countries_json() -> list:
    """
    >>> countries_json = import_countries_json()
    >>> type(countries_json)
    list
    >>> len(countries_json)
    249
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `lookup_country_iso_codes()` which returns the 2-digit and 3-digit ISO country code given the name of country, based on `countries.json` in working directory.

```python
def lookup_country_iso_codes(country: str) -> tuple:
    """
    >>> lookup_country_iso_codes("Taiwan")
    ('TW', 'TWN')
    >>> lookup_country_iso_codes("Japan")
    ('JP', 'JPN')
    >>> lookup_country_iso_codes("Lithuania")
    ('LT', 'LTU')
    >>> lookup_country_iso_codes("Slovenia")
    ('SI', 'SVN')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `lookup_country_name()` which returns the name of country given 2-digit or 3-digit ISO country code based on `countries.json` in working directory.

```python
def lookup_country_name(iso_code: str) -> str:
    """
    >>> lookup_country_name("TW")
    'Taiwan'
    >>> lookup_country_name("TWN")
    'Taiwan'
    >>> lookup_country_name("JP")
    'Japan'
    >>> lookup_country_name("JPN")
    'Japan'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```