# still_alive.py

Do you have a huge SOCKS 4/5 proxy list but no way of checking if any of them work?!

## Look no further!!

still_alive.py has got you covered! It features:
- Parallel checking, for checking multiple proxies at the same time!
- A neat progress bar, so you can see how many proxies are still left!
- Outputs alive proxies to a new file!
- The proxies are written at the end of the check to minimize disk I/O!

**Just make sure that your proxies follow the traditional IPV4 format!**

✔ Valid! 
> 12.345.67.890:1234

❌ Invalid
> HTTP://12.345.67.890:1234

> HTTPS://12.345.67.890:1234

# Install

`git clone https://github.com/NotoriusNeo/still_alive`

`pip install tqdm`

`python3.11 still_alive.py [-h] -i INPUT_FILE -o OUTPUT_FILE [-t TIMEOUT]`

Other Python versions may work, but was built with 3.11 in mind!

# Usage

```
usage: still_alive.py [-h] -i INPUT_FILE -o OUTPUT_FILE [-t TIMEOUT]

Bulk check Socks Proxy status.

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Input file with proxy list
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file for alive proxies
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout (in seconds) for proxy connection, the default is 10
```
