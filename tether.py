import subprocess
import gphoto2cffi as gp
import sys

cams = gp.list_cameras()
mappings = { c.status.eosserialnumber : c._usb_address for c in cams }

if len(sys.argv) > 1:
    print(mappings)
    exit()

for c in cams:
    c.config['settings']['capturetarget'].set('Memory card')

cameras = {
    '133052001366' : 'D',
    '013020001153' : 'B',
    '023021006300' : 'C',
    '023020001506' : 'A',
}

output = '#!/bin/bash\n'
output += 'dir=$(dirname "$0")\n'
for serial, address in mappings.items():
    output+= 'pushd "$dir/CM{}/"\n'.format(cameras[serial])
    output+= 'gphoto2 --capture-tethered --port "usb:{:03d},{:03d}" --keep-raw --force-overwrite&\n'.format(*address)
    output+= "popd\n"

for serial, cam in cameras.items():
    if serial not in mappings:
        output+= "# {} not found".format(serial)
        print("\033[91m{} (cam {}) NOT FOUND!!!!!\033[0m".format(serial, cam))

with open('tether', 'w') as f:
    f.write(output)
