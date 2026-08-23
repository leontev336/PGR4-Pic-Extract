# PGR4 Pic Extract

A small script I've made to exctract photos from the game Project Gotham Racing 4.

Images in PGR4 are stored in .p CON containers, which hold the image thumbnail, metadata and the image taken in photo mode. This script reads the .p containter and extracts the date and time the image was taken and the JPEG image itself.

## Usage:
1. When prompted save your image from photo mode on a USB stick,
2. Locate the image (usually located in /Content/EXXXXXXXXXXXXXXX/4D5307F9/00000001/)
3. Place the script in the same folder as your .p files (alternatively you can copy your images to a separate folder on your PC and place the script there),
4. Open a terminal window in that folder (or navigate via the terminal itself),
5. Type `python pgr4-pic-extract` or `python3 pgr4-pic-extract`,
6. Wait for the script to finish.

*AI USAGE DISCLOSURE: I have only used AI to research the image container.*
