import subprocess
import platform
import re
 
def ping_host(host):
    os_type=platform.system().lower()

    if os_type == "windows":
        param='-n'
    else:
        param='-c'

    try:
        result=subprocess.run(
            ['ping',param,"4",host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        if result.returncode==0:
            print(f"host :{host}")
            print("status: Reachable")

            avg_time=extract_avg_time(result.stdout)
            print(f"Average Time:{avg_time}")
        else:
            print(f"host : {host}")
            print("Status Unreachable")
    except subprocess.TimeoutExpired:
        print(f"host :{host}")
        print("Status Timedout")

def extract_avg_time(output):
    match=re.search(r'avg=([\d.]+)',output)
    if not match:
        match=re.search(r'([\d.]+)/([\d.]+)/([\d.]+)',output)
    return match.group(2) + 'ms' if match else "N/A"

def multiple_ping():
    hosts=input("enter multiple hosts (comma seperated)").split(',')
    for host in hosts:
        ping_host(host.strip())

if __name__=="__main__":
    print("ping scanner ")
    choice=input("ping single host y/n: ")

    if choice.lower()=="y":
        host=input("enter hostname or ip: ")
        ping_host(host)
    else:
        multiple_ping()