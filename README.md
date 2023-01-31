# still_alive

Do you have a huge SOCKS 4/5 proxy list but no way of checking if any of them work?!

## Look no further!!

still_alive.py has got you covered! It features:
- Parallel checking, for checking multiple proxies at the same time!
- A neat progress bar, so you can see how many proxies are still left!
- Outputs alive proxies to a new file!

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
