# Utility-Kernel
_Advertisement:_ You're on someone's computer. That computer does not have python or any programming language to easily manipulate the system.
What do you do? You download the Utility Kernel with the default Commissioner and start programming in python or in one of the many scripting languages the Utility Kernel provides (see the notes below for how).

_How does the Utility Kernel work? (explanation of the starting process)_ The Utility Kernel is starts by starting its many socket pipes (localhost:9000,9050,9100,9150,9200) that handle the interpretation of sent commands, each pipe having a special role. Then it starts the _commission.exe_ file which acts like a shell and interfaces with the Kernel's many pipes for the user to interact with. 

_Purpose of each pipe:_

  9000: Kinect Terminal by https://github.com/AstroBolo
  
  9050: Launch Anything by me (Tobey)

  9100: 3DV Utility Kernel by me (Tobey)

  9150: NT System Shell by Microsoft Corporation (https://microsoft.com)

  9200: Logging Interface by me (Tobey)

_Important Notes:_ 

  1. When calling 9000 (Kinect Terminal), _echo me_ is changed to _echo_me_.
  2. When calling 9100 (Utility Kernel 3DV), _promptuser_ is changed to _prompt_.
  3. In the Kernel **all** inputs are dismissed and are converted to the arguments which come after the command (eg. echo_me test, 1 regedit, prompt print("Test"), et cetera...).
  4. In **all** the terminals error handling is upgraded.
  5. In the Kernel you can use python by sending _prompt_ and your command to 9100.
  6. If you just want the Kernel for automation (**NOT** creating apps) you could just use the default commissioner (commission.exe) which asks you for commands and then finds which terminal is the best for your command and sends it. It starts up with the Kernel as mentioned above.

## PLEASE CONTRIBUTE TO THE KERNEL
