from optparse import OptionParser
import os,glob

def main():
    usage = "useage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-d", "--dir", type="string", dest="input_dir", help="combine and unique-ify all lines from all files in the directory")
    (options, args) = parser.parse_args()

    if (options.input_dir is None):
        parser.error("not enough number of arguments")
		
    phrases = set()

    # Add all lines from each file in the directory to the set
    for filename in glob.glob(os.path.join(options.input_dir, '*.txt')):
        for line in open(filename, 'r'):
            # Remove whitespace and convert to lowercase before adding to the set
            phrases.add(line.strip().lower())
		
    # Write out all items from the set
    f = open("skribblio.txt", "w")
    for phrase in phrases:
        f.write("%s," % phrase)

if __name__ == "__main__":
    main()