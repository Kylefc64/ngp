import os,glob, imaplib, email,webbrowser
from email.header import decode_header
from optparse import OptionParser


def main():
	# account credentials
	username = 'not.gartic.phone@gmail.com'
	password = 'NotGarticPhone399'


	def clean(text):
	    # clean text for creating a folder
	    return "".join(c if c.isalnum() else "_" for c in text)

	# create an IMAP4 class with SSL
	imap = imaplib.IMAP4_SSL("imap.gmail.com")
	# authenticate
	imap.login(username, password)

	status, messages = imap.select("INBOX")

	#convert messages to int
	messages = int(messages[0])
	#now that messages is an int, N, which represents the number 
	#of emails in inbox we will search, can be told to search
	# all the messages
	N = messages


	for i in range(messages, messages-N, -1):
	    # fetch the email message by ID
	    res, msg = imap.fetch(str(i), "(RFC822)")
	    for response in msg:
		if isinstance(response, tuple):
		    # parse a bytes email into a message object
		    msg = email.message_from_bytes(response[1])
		    # decode the email subject
		    subject, encoding = decode_header(msg["Subject"])[0]
		    if isinstance(subject, bytes):
			# if it's a bytes, decode to str
			subject = subject.decode(encoding)
		    # decode email sender
		    From, encoding = decode_header(msg.get("From"))[0]
		    if isinstance(From, bytes):
			From = From.decode(encoding)
		    print("Subject:", subject)
		    print("From:", From)
		    # if the email message is multipart
		    if msg.is_multipart():
			# iterate over email parts
			for part in msg.walk():
			    # extract content type of email
			    content_type = part.get_content_type()
			    content_disposition = str(part.get("Content-Disposition"))
			    try:	         	
				# get the email body
				body = part.get_payload(decode=True).decode()
			    except:
				pass
			    if content_type == "text/plain" and "attachment" not in content_disposition:
				# print text/plain emails and skip attachments
				print(body)
			    elif "attachment" in content_disposition:
				# download attachment
				filename = part.get_filename()
				if filename:
				    folder_name = clean("subject")
				    if not os.path.isdir(folder_name):
					# make a folder for this email (named after the subject)
					os.mkdir(folder_name)
				    filepath = os.path.join(folder_name, filename)
				    # download attachment and save it
				    open(filepath, "wb").write(part.get_payload(decode=True))
		    else:
			# extract content type of email
			content_type = msg.get_content_type()
			# get the email body
			body = msg.get_payload(decode=True).decode()
			if content_type == "text/plain":
			    # print only text email parts
			    print(body)
		    if content_type == "text/html":
			# if it's HTML, create a new HTML file and open it in browser
			folder_name = clean(subject)
			if not os.path.isdir(folder_name):
			    # make a folder for this email (named after the subject)
			    os.mkdir(folder_name)
			filename = "index.html"
			filepath = os.path.join(folder_name, filename)
			# write the file
			open(filepath, "w").write(body)
			# open in the default browser
			webbrowser.open(filepath)
		    print("="*100)




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

	# close the connection and logout
	imap.close()
	imap.logout()

	if __name__ == "__main__":
	    main()









