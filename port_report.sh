#!/bin/bash 

if [ -z "$1" ]; then 
    echo "Usage:$0 <target_ip>"
    exit 1
fi

TARGET=$1
DATE=$(date +%Y-%m-%d)
OUTPUT="scan_${TARGET}_${DATE}.txt"
echo "Scanning target : $TARGET"
echo "Saving results to $OUTPUT"

PORTS=(21 22 80 443 3306)
OPEN_COUNT=0

echo "port scan report for $TARGET ">$OUTPUT
echo "Date : $DATE" >> $OUTPUT
echo "-------">> $OUTPUT

for PORT in "${PORTS[@]}"
do 
    timeout 1 bash -c "echo > /dev/tcp/$TARGET/$PORT" 2>/dev/null
    if [ $? -eq 0 ] ; then 
        echo "port $PORT: OPEN "|tee -a $OUTPUT
        ((OPEN_COUNT++))
    else 
        echo "port $PORT: CLOSED "|tee -a $OUTPUT
    fi 
done 
echo "-------">>$OUTPUT
echo "Total Open Ports : $OPEN_COUNT"|tee -a $OUTPUT
