#!/usr/bin/env bash
# install AVR-tools for Debian and Ubuntu derivates
# wykys 2018


# download Atmel AVR toolchain and extract
# from http://www.microchip.com/mplab/avr-support/avr-and-arm-toolchains-c-compilers
TMP="/tmp"
AVR_TOOLCHAIN_TAR="avr-toolchain.tar.gz"
AVR_TOOLCHAIN_URL="http://www.microchip.com/mymicrochip/filehandler.aspx?ddocname=en605750"
AVR_TOOLCHAIN_DIR="avr8-gnu-toolchain-linux_x86_64"
AVR_TOOLCHAIN_INSTALL_DIR="/opt"
cd $TMP
echo "Downloading AVR toolchain"
wget $AVR_TOOLCHAIN_URL -O $AVR_TOOLCHAIN_TAR
echo "Unpacking AVR toolchain"
tar -zxvf $AVR_TOOLCHAIN_TAR
echo "Removing old AVR toolchain"
sudo rm -rf $AVR_TOOLCHAIN_TAR $AVR_TOOLCHAIN_INSTALL_DIR/$AVR_TOOLCHAIN_DIR
echo "Installing AVR toolchain"
sudo mv $AVR_TOOLCHAIN_DIR $AVR_TOOLCHAIN_INSTALL_DIR


# install required packages
sudo apt-get install python3 python3-serial avrdude make git
