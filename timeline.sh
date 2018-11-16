#!/bin/bash
#
# Purpose:  Gather a forensic timeline based on inode information to be given
#           to python file to parse and analyze.
#
# Author:   Scott Brink
#
# Basic Usage:
#       1. Image file
#           - ./timeline.sh -d / -i floppy.dd -t 2000-01-01 
#       2. On self
#           - ./timeline.sh -d / -t 2000-01-01
#
# Dependencies:
#      1. Sleuthkit
#  

# Usage message
if [ -z $1 ]; then
    echo "Usage: ./timeline.sh -d DIRECTORY -i IMAGE -t TIME(2000-01-01 format) -o OUTPUT_FILE"
    exit
fi

# Default parameters
DIRECTORY="/"
IMAGE=""
TIME="2000-01-01"
OUTPUT="default.csv"

# Help dialog
function helpDialog(){
    echo "Timeline Creation Tool"
    echo "Options:"
    echo "      -d (--directory)= Specify which directory to start from (default is \"/\")."
    echo "      -i (--image)    = Specify if you are testing an image file (if not selected, will check own system)."
    echo "      -t (--time)     = Specify what time to start from in year-month-day format (if not selected, time will be 2000-01-01)."
    echo "      -o (--output)   = Specify an output file (if not selected, file will be default.csv)." 
    echo "      -h (--help)     = Display help dialog."
    exit
}

# Gather Arguments
POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -d|--directory)     # Directory to start at
    DIRECTORY="$2"
    shift               # past argument
    shift               # past value
    ;;
    -i|--image)         # Image file
    IMAGE="$2"
    shift               # past argument
    shift               # past value
    ;;
    -t|--time)          # Date (2000-01-01)
    TIME="$2"
    shift               # past argument
    shift               # past value
    ;;
    -o|--output)
    OUTPUT="$2"         # Output
    shift               # past argument
    shift               # past value
    ;;
    -h|--help)
    HELP="$2"           # Help dialog
    helpDialog 
    ;;  
    --default)
    DEFAULT=YES
    shift               # past argument
    ;;
    *)                  # unknown option
    POSITIONAL+=("$1")  # save it in an array for later
    shift               # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

# If no image specified, do it on self.
if [ -z "$IMAGE" ]; then
    mac-robber $DIRECTORY | mactime -d -m $TIME > $OUTPUT
# If image specified, do it on image.
elif [ -n "$IMAGE" ]; then
    fls -r -m $DIRECTORY $IMAGE | mactime -d -m $TIME > $OUTPUT
fi
