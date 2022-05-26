# Access

## Screen, keyboard, mouse

Plug your screen, keyboard and mouse in the pi and power it up.

```{note}
The default setting for the keyboard is QWERTY.
```

---

## VNC

VNC is a network protocol which allows you to remotely control the desktop screen of your device.

### Configure

1. install vnc-server and vnc-viewer
    ```bash
    sudo apt install realvnc-vnc-server realvnc-vnc-viewer
    ```
2. enable vnc
    - Open raspberry configuration
        ```bash
        sudo raspi-config
        ```
    - navigate to `Interfacing options`
    - select `vnc` → `Yes`

### Usage

1. Download [VNC-viewer](https://www.realvnc.com/en/connect/download/viewer/) on your local machine 
2. Add a new connection: `File` → `New connection` or `CTRL+N`
3. connect

---

## SSH

SSH stand for secure shell and is a network protocol for a command-line interface to your desired device.

### Internet
- WIFI setup: add file `wpa_supplicant.conf` to the boot folder or `/etc/wpa_supplicant/wpa_supplicant.conf` on the pi [syntax](wpa_supplicant)
- Direct ethernet connection:
    1. add `ip=10.0.0.1` to the long line of `cmdline.txt` of the boot folder or `/boot/cmdline.txt` on the pi
    2. Set IP of PC
      1. Navigate on your Windows 10 to <br>
`Control Panel` → `Network and Internet` → `Network and Sharing Center` → `Change adapter settings`
      2. Right-click `Ethernet` and select `Properties`
      3. Double-click `Internet Protocol versie 4 (TCP/IPv4)`
      4. Configure connection
	  ![ipv4properties](images/ipv4properties.png)

(preconfigure_ssh)=
### Preconfigure

1. Add file `ssh` to the boot folder (no extension, no contents).
2. WIFI setup: add file `wpa_supplicant.conf` to the boot folder [syntax](wpa_supplicant)

### Configure

Enable SSH <br>
1. Open raspberry configuration
    ```bash
    sudo raspi-config
    ```
2. Navigate to **Interfacing options**
3. Select SSH → Yes

### Usage

On another computer, type in command line:
```bash
ssh pi@IP_ADDRESS
```
The pi will ask for a password, the default is `raspberry`.

