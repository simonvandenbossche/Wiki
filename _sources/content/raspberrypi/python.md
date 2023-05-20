# Python

## BerryConda

Berryconda is a conda based Python distribution for the Raspberry Pi.
Altough you can only use version up to python 3.6.6 (november 2020), you have the advantage of an easy installation process with the conda infrastructure.

#### Install
Sources: [berryconda](https://github.com/jjhelmus/berryconda), [environment](https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b)
1. Download correct version (BerryConda will be installed in the folder where you run one of the following commands):
    * Raspberry Pi Zero or 1
        * Python 2
            ```bash
            wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda2-2.0.0-Linux-armv6l.sh
            ```
        * Python 3
            ```bash
            wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv6l.sh
            ```
    * Raspberry Pi 2 or 3
        * Python 2
            ```bash
            wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda2-2.0.0-Linux-armv7l.sh
            ```
        * Python 3
            ```bash
            wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
            ```
2. Make the file executable and install it
    ```bash
    chmod +x Berryconda3-2.0.0-Linux-armv7l.sh
    ./Berryconda3-2.0.0-Linux-armv7l.sh
    ```
3. Add conda command to pi <code>export PATH="/home/pi/berryconda3/bin"</code>
    ```{error}
    This step is wrong. Please do not follow it.
    ```
4. Install new version of python
    1. Install new version (Can be any available version, I used 3.6 as example)
        ```bash
        conda config --add channels rpi
        conda install python=3.6
        ```
    2. Create environment
        ```bash
        conda create --name py36 python=3.6
        ```
    3. Activation/decativation
        ```bash
        source activate py36
        source deactivate
        ```
5. Install RPi.GPIO (optional, in activated environment)
    ```bash
    pip install rpi.gpio
    ```

## Miniconda

sources [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

A second option is miniconda, a minimal version of anaconda. But I couldn't get this to work on the pi.

