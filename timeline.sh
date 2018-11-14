#!/bin/bash
#
# Purpose:  Gather a forensic timeline based on inode information to be given
#           to python file to parse and analyze.
#
# Author:   Scott Brink
#
# TODO, Convert to a real way to help rather than this lazy garbage
# Basic Usage:
#       1. Image file
#           - ./timeline.sh -d / -i floppy.dd -t 2000-01-01 
#       2. On self
#           - ./timeline.sh -d / -t 2000-01-01
#
# TODO  1. Error Checking
#       2. Good File Names (optional parameter?)
#       3. Help Documentation
#       4. Usage Message
#       5. Dependencies (fls, mactime, mac-robber)
#  

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
    mac-robber $DIRECTORY | mactime -d -m $TIME > self.csv
# If image specified, do it on image.
elif [ -n "$IMAGE" ]; then
    fls -r -m $DIRECTORY $IMAGE | mactime -d -m $TIME > image.csv
fi
