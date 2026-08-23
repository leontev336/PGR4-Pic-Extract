import re
import os
import time

print("""
Project Gotham Racing 4 Pic Extract

Please make sure that your .p images are in the same folder as the script!
""")
time.sleep(4)

directory = os.path.dirname(os.path.abspath(__file__))
counter = 0
for entry in os.listdir(directory):
    if entry.endswith('.p'):
        file = open(entry, 'rb')
        binary_file = file.read()
        divider_pattern = re.compile(b'\x00*(\xff\xd8\xff.*?\xff\xd9)(?=\x00{12,})', re.DOTALL)
        if divider_pattern.search(binary_file):
            images = divider_pattern.findall(binary_file)
        else:
            print("Not a valid image.")
            continue

        for i in images:
            with open(entry, 'rb') as f:
                f.seek(0x5420)
                timedate = re.sub(b'\x00', b'', f.read(41)).decode('utf-8')
                print(f'Image "{timedate[4:]}" extracted.')
                name = re.sub(r'[/\\:@]', r'_', timedate[4:])
                with open(f"{re.sub(r'\s+', r'', name)}.jpg", "wb") as f:
                    f.write(i)
                if divider_pattern.search(binary_file):
                    counter = counter + 1
                else:
                    counter = counter
    else:
        continue

if counter == 0:
    print("""
The script encountered an error. Please make sure that your images are in the same folder as the script or that they are valid PGR4 images.
    """)
else:
    print(f"Extracted {counter} images.")