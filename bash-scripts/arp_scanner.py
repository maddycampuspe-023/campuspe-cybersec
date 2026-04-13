import subprocess
import re

def get_arp_table():
    try:
        result=subprocess.run(
            ["arp","-a"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e :
        print("Error:",e)
        print(None)
def parse_arp(output):
    pattern=r'\((\d+\.\d+\.\d+\.\d+)\)\s+at\s+(([0-9a-f]{2}:){5}[0-9a-f]{2})'
    matches= re.findall(pattern,output,re.IGNORECASE)

    arp_list=[]
    for match in matches:
        ip=match[0],
        mac=match[1],
        arp_list.append((ip,mac))
    return arp_list
def display_arp(arp_list):
    print("\n IP address \t\t Mac Address")
    print("-" * 40)

    for ip ,mac in arp_list:
        print(f"{ip}\t\t{mac}")

    print(f"total entries:{len(arp_list)}")

def save_to_file(arp_list):
    try:
        with open("arp_results.txt",'w') as f :
            for ip, mac in arp_list:
                f.write(f"{ip}-{mac}\n")
        print("results are saved to arp_results.txt ")
    except Exception as e :
        print("error saving file ",e)

if __name__=="__main__":
    print("arp scanner")

    output=get_arp_table()

    if output:
        arp_list=parse_arp(output)
        display_arp(arp_list)

        choice=input("\n save results to file? y/n:")
        if choice.lower=='y':
            save_to_file(arp_list)