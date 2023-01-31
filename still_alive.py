import argparse
import socket
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Bulk check Socks Proxy status.')
parser.add_argument('-i','--input_file', help='Input file with proxy list', required=True)
parser.add_argument('-o','--output_file', help='Output file for alive proxies', required=True)
parser.add_argument('-t','--timeout', help='Timeout (in seconds) for proxy connection, the default is 10', default=10, type=int)
args = parser.parse_args()

# set the timeout to 10 seconds
socket.setdefaulttimeout(args.timeout)

# function that takes a proxy host and port and check if the proxy is alive
def is_socks_proxy_alive(proxy_host, proxy_port):
    try:
        # create a new socket and connect to the proxy
        sock = socket.create_connection((proxy_host, proxy_port))
        sock.close()
        return f"{proxy_host}:{proxy_port} is alive."
    except:
        # if the connection failed return error message
        return f"{proxy_host}:{proxy_port} is not alive."

# open the input file and read the proxies from it
with open(args.input_file, "r") as f:
    proxy_list = [tuple(proxy.strip().split(":")) for proxy in f.readlines()]

try:
    # create a ProcessPoolExecutor and use it to check the status of the proxies in parallel
    with ProcessPoolExecutor() as executor:
        # wrap the map method with tqdm to show progress bar
        results = list(tqdm(executor.map(is_socks_proxy_alive, [host for host,port in proxy_list], [int(port) for host,port in proxy_list]), total=len(proxy_list)))
        alive_proxy = set()
        # iterate over the results to get the alive proxy
        for res in results:
            if "is alive" in res:
                alive_proxy.add(res.split(":")[0]+":"+res.split(":")[1])
        # open the output file to write the alive proxies to it
        with open(args.output_file, "w") as f:
            for proxy in alive_proxy:
                f.write(proxy + "\n")
except KeyboardInterrupt:
    # handle the KeyboardInterrupt exception
    executor.shutdown(wait=False)
    print("\nExiting program...")
