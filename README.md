# timestomp-detector
- This tool detects timestomping by analyzing the MAC timestamps.

## Authors
- Written for CSEC464: Computer System Forensics

- Written by Scott Brink and Jake Brown

## Dependencies
- `apt-get install sleuthkit`

## Usage
- Run `timeline.sh` to generate the timeline using Sleuthkit tools.  Check the help message in `timeline.sh` for more options when running the script.

- Run `reader.py` to read through the output file and analyze to check for timestomping.
