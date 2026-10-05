# PGR4 Pic Extract

A small script I've made to exctract photos from the game Project Gotham Racing 4.

Images taken in PGR4's photo mode are stored in .p CON containers, which hold the image thumbnail, metadata and the JPEG image itself. This script reads the .p containter and extracts the date, time and the image taken. Date and time are used to name the image extracted.

This has only been tested on Xbox 360.

## Usage:
1. When prompted in-game, save your image from photo mode to a USB stick,
2. Locate the image (usually in /Content/EXXXXXXXXXXXXXXX/4D5307F9/00000001/),
3. Place the script in the same folder as your .p files (alternatively you can copy your .p files to a separate folder on your PC and place the script there),
4. Open a terminal window in that folder (or navigate via the terminal itself),
5. Type `python pgr4-pic-extract` or `python3 pgr4-pic-extract`,
6. Wait for the script to finish.

*AI USAGE DISCLOSURE: I have only used AI to research the image container.*
