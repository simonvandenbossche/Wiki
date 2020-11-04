#!/usr/bin/env python
# coding: utf-8

# ## A guide to install and use python
# 
# ### BerryConda
# 
# Berryconda is a conda based Python distribution for the Raspberry Pi.
# 
# #### Install
# Sources: [berryconda](https://github.com/jjhelmus/berryconda|BerryConda), [environment](https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b)
#   - Download correct version (BerryConda will be installed in the folder where you run one of the following commands):
#     * Raspberry Pi Zero or 1
#       * Python 2:
# ```bash
# wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda2-2.0.0-Linux-armv6l.sh</code>
# ```
#       * Python 3:
# ```bash
# wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv6l.sh</code>
# ```
#     * Raspberry Pi 2 or 3
#       * Python 2:
# ```bash
# wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda2-2.0.0-Linux-armv7l.sh</code>
# ```
#       * Python 3:
# ```bash
# wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh</code>
# ```
#   - Make the file executable and install it
# ```bash
# chmod +x Berryconda3-2.0.0-Linux-armv7l.sh
# ./Berryconda3-2.0.0-Linux-armv7l.sh
# ```
#   - Add conda command to pi <code>export PATH="/home/pi/berryconda3/bin"</code>
#   - Install new version of python
#     - Install new version (Can be any available version, I used 3.6 as example)
# ```bash
# conda config --add channels rpi
# conda install python=3.6
# ```
#     - Create environment
# ```bash
# conda create --name py36 python=3.6
# ```
#     - Activation/decativation
# ```bash
# source activate py36
# source deactivate
# ```
#   - Install RPi.GPIO (optional, in activated environment)
# ```bash
# pip install rpi.gpio
# ```
# 
