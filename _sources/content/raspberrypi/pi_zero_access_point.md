# Access point

Set up a pi zero as an access point to have a wireless network to which you can connect.

## Configure

1. Update
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
2. Install `dnsmasq` and `hostapd`
    ```bash
    sudo apt install dnsmasq hostapd
    ```
3. Create virtual interface `ap0` \
    Get the MAC address of the wlan0 interface with
    ```bash
    cat /sys/class/net/wlan0/address
    ```
    Create the file `/etc/udev/rules.d/70-persistent-net.rules`.
    And add the following line to it. Replace $mac_address (twice) with the MAC address of the wlan0 interface.
    ```
    SUBSYSTEM=="ieee80211", ACTION=="add|change", ATTR{macaddress}=="$mac_address", KERNEL=="phy0",   RUN+="/sbin/iw phy phy0 interface add ap0 type __ap",   RUN+="/bin/ip link set ap0 address $mac_address"
    ```
4. Configure the DHCP server \
    Edit the file `/etc/dnsmasq.conf` and add the following lines to it.
    ```
    interface=lo,ap0
    no-dhcp-interface=lo,wlan0
    bind-interfaces
    server=8.8.8.8
    domain-needed
    bogus-priv
    dhcp-range=192.168.200.100,192.168.200.199,12h
   ```
   The last line is the range of IP addresses that will be given to clients that connect.
5. Configure the access point \
    Edit the file `/etc/hostapd/hostapd.conf` and add the following lines to it.
    Replace $AP_SSID and $AP_PASSWORD with the desired SSID and password.
    ```
    ctrl_interface=/var/run/hostapd
    ctrl_interface_group=0
    interface=ap0
    driver=nl80211
    ssid=$AP_SSID
    hw_mode=g
    channel=11
    wmm_enabled=0
    macaddr_acl=0
    auth_algs=1
    wpa=2
    wpa_passphrase=$AP_PASSWORD
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP CCMP
    rsn_pairwise=CCMP
    ```
   Edit the file `/etc/default/hostapd` and uncomment the line `#DAEMON_CONF=""` and change it to
    ```
    DAEMON_CONF="/etc/hostapd/hostapd.conf"
    ```
6. Configure the network interface \
    Edit the file `/etc/network/interfaces` and add the following lines to it.
    ```
    source-directory /etc/network/interfaces.d

    auto lo
    auto ap0
    auto wlan0
    iface lo inet loopback
    
    allow-hotplug ap0
    iface ap0 inet static
    address 192.168.200.1
    netmask 255.255.255.0
    hostapd /etc/hostapd/hostapd.conf
    
    allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface AP1 inet dhcp
    ```
    The line of the static ip should be on the same subnet as the dhcp range in the dnsmasq config.
7. Configure bridge of the internet \
    Create the file `/bin/rpi-wifi.sh` and add the following lines to it.
    ```bash
    sleep 30
    sudo ifdown --force wlan0
    sudo ifdown --force ap0
    sudo ifup ap0
    sudo ifup wlan0
    sudo sysctl -w net.ipv4.ip_forward=1
    sudo iptables -t nat -A POSTROUTING -s 192.168.200.0/24 ! -d 192.168.200.0/24 -j MASQUERADE
    sudo systemctl restart dnsmasq
    echo "AP bridge configured"
    ```
    Make the file executable with
    ```bash
    sudo chmod +x /bin/rpi-wifi.sh
    ```

    Finally, edit crontab with
    ```bash
    sudo crontab -e
    ```
    And add
    ```
    @reboot /bin/rpi-wifi.sh
    ```