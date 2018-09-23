# AVR-tools
Tools for development of AVR microcontrollers.

## Project wizard
### First step
Open the terminal and go to path where you want to create your AVR project. Use the `cd` command to move.

### Getting the project template
Getting the template is easy. Just clone this repository.
```bash
# if you prefer SSH
git clone git@github.com:wykys/AVR-tools.git
# else use HTTPS
git clone https://github.com/wykys/AVR-tools.git
```

### Set the name of the project folder
Use the `mv` command to change the folder name.
```bash
# replace the the_name_of_your_project with the desired name
mv AVR-tools the_name_of_your_project
# and go to your project folder
cd the_name_of_your_project
```

### Open project in editor
Open your project in your favorite text editor. Choose one option.
```bash
# for Atom
atom .
# for Visual Studio Code
code .
```

### Makefile settings
`Makefile` describes the build of the project. It also allows you to run auxiliary tools such as programming the target processor or analyzing compilation results.

The `Makefile` file is located in the root directory of your project. Using a text editor, you can edit the variables as required by the application.

#### Project name
It affects the names of the generated files.
```makefile
# find the following line
TARGET = DEMO
# change DEMO for the name of your project
TARGET = the_name_of_your_project
```

#### Target microcontroller
The names of available microcontrollers are available [here](https://gcc.gnu.org/onlinedocs/gcc/AVR-Options.html).
```makefile
# find the following line
CHIP = atmega328p
# change CHIP
CHIP = the_name_of_your_chip
```

#### Code size optimization
It affects the size and speed of the application.

| __OPT__ |  __DESCRIPTION__  |
|---------|-------------------|
| -O0 | optimization is off   |
| -O1 | optimization level 1  |
| -O2 | optimization level 2  |
| -O3 | optimization level 3  |
| -Os | size optimization     |

```makefile
# find the following line
OPT = -Os
# change OPT
OPT = required_optimization
```

#### Changing the programmer
List of supported programmers `avrdude` is [here](https://www.nongnu.org/avrdude/user-manual/avrdude_4.html)
```makefile
# find the following line
AVRDUDE = avrdude -p $(shell $(WTR)) -c arduino -P $(shell $(WFS))
# change AVRDUDE
# port is required only for some programmers
AVRDUDE = avrdude -p $(shell $(WTR)) -c your_programmer -P programmer_port
```

### Use `make`
`Makefile` allows compilation, programming and debugging applications.
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
