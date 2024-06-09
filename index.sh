#!/bin/bash

# Check if at least one argument (host) is provided
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <host> [start_port] [end_port]"
  exit 1
fi

# Define variables
HOST=$1
START_PORT=${2:-1}
END_PORT=${3:-65535}

# Function to scan a single port
scan_port() {
  local host=$1
  local port=$2
  nc -z -w1 $host $port
  return $?
}

echo "Starting scan on host: $HOST from port $START_PORT to $END_PORT"

# Start time
START_TIME=$(date +%s)

# Scan ports in the range
for (( port=$START_PORT; port<=$END_PORT; port++ )); 
3 do
  if scan_port $HOST $port; then
    echo "Port $port is open"
  fi
done

# End time
END_TIME=$(date +%s)
TOTAL_TIME=$((END_TIME - START_TIME))

echo "Scan completed in $TOTAL_TIME seconds."
