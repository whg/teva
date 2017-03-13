import subprocess
import gphoto2cffi as gp
import sys

cameras = {
   '00000000000000000000000006031485' : 'C',
   '00000000000000000000000006020701' : 'A',
   '00000000000000000000000006006782' : 'D',
   '00000000000000000000000006020585' : 'B',
}

cams = gp.list_cameras()
mappings = { c.status.serialnumber : c._usb_address for c in cams }

output = ""
for serial, address in mappings.items():
    output+= "pushd /Volumes/ro0kie\\ HDD/_PROJECTS/IKEA_tests/CM{}/\n".format(cameras[serial])
    output+= 'gphoto2 --capture-tethered --port "usb:{:03d},{:03d}" --keep-raw --force-overwrite&\n'.format(*address)
    output+= "popd\n"

for serial in cameras.keys():
    if serial not in mappings:
        output+= "# {} not found".format(serial)
        print("{} NOT FOUND!!!!!".format(serial))

with open('tether.sh', 'w') as f:
    f.write(output)
