# AVR-tools
Tools for development of AVR microcontrollers.

## Use
```bash
# compiling the project, equivalen to make
make all
# flash content
make flash
# compiling the project and programming the flash
make build_and_flash
# deletes the compilation outputs
make clean
# start avrdude terminal
make terminal
# EEPROM dump_eeprom
make dump_eeprom
# flash all (flash, EEPROM)
make flash_all
# chip testing
make chip_test
```

## Installation
### For Debian Ubuntu and their derivatives
Just enter the following command into terminal for download and run shell installation script, which automatically installs the necessary tools.
```bash
sh -c "$(wget https://raw.githubusercontent.com/wykys/AVR-tools/master/.scripts/install.sh -O -)"
```
