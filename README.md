# not-gartic-phone (ngp)

Running ngp.py with no options will do the following:
1. Fetch all lines from all attachments sent to not.gartic.phone@gmail.combine
2. Strip whitespace from each line, convert each line to lowercase, combine all processed lines, and remove duplicate processed lines.
3. Combine all unique, processed lines into a comma-separated string and a) write the string to skribblio.txt and b) copy the string to your clipboard.
4. This comma-separated string of phrases can be pasted into the word bank text box of a private skribbl.io room.

If ngp.py is invoked with the --dir / -d option, all files will be fetched from the specified input directory instead of from the mailbox of not.gartic.phone@gmail.com.
If invoked with the --skribb / -s option, then a private skribbl.io room will automatically be created (and the room's link printed and/or automatically sent to the senders of the email attachments) (support is pending for this feature).

# Usage

```
$ python python/nerds.py --help
Usage: useage: nerds.py [options]

Options:
  -h, --help            show this help message and exit
  -d INPUT_DIR, --dir=INPUT_DIR
                        combine and unique-ify all lines from all files in the
                        directory
  -s, --skribb          automatically start the private skribbl room
```
