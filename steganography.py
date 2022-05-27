def help_and_exit():
    # show how program should be used and exit
    print("Usage:\n\tsteg hide \"your message here\" input_file.png output_file.png")
    print("\tsteg show input_file.png")
    exit()

if len(sys.argv) != 5 and len(sys.argv) != 3:
    help_and_exit()

operation = sys.argv[1]
if operation != "show" and operation != "hide":
    help_and_exit()

if operation == "show":
    # reveal message from target file
    file_name = sys.argv[2]
    print(f"Hidden message: {lsb.reveal(file_name)}")
else:
    # hide message in target file
    input_file_name = sys.argv[3]
    output_file_name = sys.argv[4]
    message = sys.argv[2]
    lsb.hide(input_file_name, message).save(output_file_name)
