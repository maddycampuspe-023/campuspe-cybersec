import subprocess
import shutil

def check_nmap():
    return shutil.which("nmap") is not None

def run_nmap(target, scan_type):
    try:
        if scan_type=="1":
            cmd=["nmap","-sn",target]
        elif scan_type=="2":
            cmd=["nmap",target]
        elif scan_type=="3":
            ports=input("enter the port range :(eg 0-1000)")
            cmd=["nmap","-p",ports,target]
        elif scan_type=="4":
            cmd=["nmap","-sV",target]
        elif scan_type=="5":
            cmd=["nmap","-O",target]
        else:
            print("Invalid choice...")
            return
        print("Scanning Please Wait...")

        result=subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        print(result.stdout)

        Choice=input("save results to the file? y/n")
        if Choice.lower()=='y':
            with open("nmap_results.txt","w")as f:
                f.write(result.stdout)
            print("results are saved to the nmap_results.txt")
    except subprocess.TimeoutExpired:
        print("Scan timedout")
    except Exception as e :
        print("Error: ",e)
if __name__=="__main__":
    print("nmap Scanner")

    if not check_nmap():
        print("nmap is not installed")
        exit()
    print("nmap is installed")
    target=input("enter target IP or network :")

    print("\n Select scan type :")
    print("1.Host scan :")
    print("2.port Discovery:")
    print("3.custom port scan :")
    print("4.Service version detection: ")
    print("5.OS detection:")

    choice=input("enter the choice (1-5): ")

    run_nmap(target,choice)