hexdump  -e '1/40 "%08_ax: "'    -e '20/1 "%02x " "  " 20/1 "%02x " "  |"'     -e '40/1 "%_p" "|\n"'  file.bin