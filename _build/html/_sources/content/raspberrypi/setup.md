## Setup

1. Download the [Raspbian Image](https://www.raspberrypi.org/downloads/raspbian/)<br>
    - Raspbian Buster with desktop and recommended software: Can have a lot of trash.
    - Raspbian Buster with desktop: Allow screen to be used
    - Raspbian Buster Lite: Minimal version with no desktop, recommended.
2. Format the SD-card using [SD card formatter](https://www.sdcard.org/downloads/formatter/)
3. Write the image to the SD-card  using [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/files/latest/download)
4. Preconfigure [ssh](ssh) (optional)
5. > Login: `pi`
    password: `raspberry`
    - To set a new password use
        ```bash
        passwd
        ```
6. Update and upgrade (this may take a while)
    ```bash
    sudo apt update
    sudo apt full-upgrade
    ```
