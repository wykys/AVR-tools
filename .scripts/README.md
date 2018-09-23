# Scripts summary
These scripts are developed to simplify the development of AVR applications.

## avr-size
The script combines memory information from the AVR database and the utility size parsing output. Memory and size information displays in a more readable form.

Te script can automatically find a binary .elf, if the two folders do not exceed the level of the two.

### Demo
`.scripts/avr-size.py --mcu=atmega8`
```
╔════════════════════════╗ ╔════════════════════════╗
║    RAM MEMORY 9.3 %    ║ ║   FLASH MEMORY 9.2 %   ║
╟────────────────────────╢ ╟────────────────────────╢
║All:               1 KiB║ ║All:               8 KiB║
║Use:                95 B║ ║Use:               750 B║
║Free:              929 B║ ║Free:           7.27 KiB║
╚════════════════════════╝ ╚════════════════════════╝
```

### Arguments
`.scripts/avr-size.py -h`
```
usage: avr-size [-h] [-e PATH_ELF] [-c] [-v] [-m MCU] [-s SIZE]

The script combines memory information from the AVR database and the utility size parsing output. Memory and size information displays in a more readable form.

optional arguments:
  -h, --help            show this help message and exit
  -e PATH_ELF, --elf PATH_ELF
                        destination elf file
  -c, --color           activated color output
  -v, --vertical        prints the tables underneath
  -m MCU, --mcu MCU     the name of the microcontroller
  -s SIZE, --size SIZE  the path to size utility

```

## avr-translate-mcu
