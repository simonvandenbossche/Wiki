# Bash scripts

## Creation

sources: <http://linuxcommand.org/lc3_wss0010.php>

1. create script file with nano file editor
    ```bash
    nano FILEPATH.sh
    ```
2. begin the script with `#!/bin/bash`
3. add the terminal commands line by line

## Usage

sources: <https://www.geeksforgeeks.org/source-command-in-linux-with-examples/>
         <http://linuxcommand.org/lc3_wss0010.php>

* execute code in the current terminal
    ```bash
    source FILEPATH.sh
    ```
* execute code in new terminal
    1. make file executable (first time only)
        ```bash
        chmod 755 FILEPATH.sh
        ```
    2. execute code
        ```bash
        . FILEPATH.sh
        ```

## Alias

You can create a custom command for your bash script with an alias.

sources: <https://www.tecmint.com/create-alias-in-linux/>

* create a temporary alias (usable until you close your terminal)
    ```bash
    alias SHORTCOMMAND="FULLCOMMAND"
    ```
* create a permanent alias
    1. open the bashrc file
        ```bash
        nano ~/bashrc
        ```
    2. append at the end of the file the alias command
        ```bash
        alias SHORTCOMMAND="FULLCOMMAND"
        ```
    3. save and close the file with `CTRL+X` → `Y` → `ENTER`
    4. reboot
        ```bash
        sudo reboot
        ```
    

