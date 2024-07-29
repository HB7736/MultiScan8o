from sys import path
from os.path import dirname, abspath
path.append(dirname(dirname(abspath(__file__))))
from window import terminal

def use_Hacking_banner():
    terminal.execute_command(command=Hacking_banner,
                            width=78,
                            height=8, autoclose=True)


Hacking_banner = r'''
#!/bin/bash

animate_text() {
    clear
    echo -n -e "$2$3$1\033[0m"
    sleep 0.1
}

a1="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗                  
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝                  
"

a2="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗               
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝               
"

a3="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗            
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝            
"

a4="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗██╗         
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝╚═╝         
"

a5="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗██╗██╗      
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝╚═╝╚═╝      
"

a6="
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗                      
   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝                      
   ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗                     
   ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║                     
   ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗██╗██╗██╗   
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝   
"

red="\033[31m"
green="\033[32m"
blue="\033[34m"


for i in {1..5}
do
    # Main script
    animate_text "$a1" "$red"
    animate_text "$a2" "$red"
    animate_text "$a3" "$green"
    animate_text "$a4" "$green"
    animate_text "$a5" "$blue"
    animate_text "$a6" "$blue"
done
exit 0
'''

if __name__=="__main__":
    use_Hacking_banner()