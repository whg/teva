Config
------

Edit `cameras.py` with the mapping of camera serial number to position (e.g. A, B, etc).

Tethering
---------

All commands can either be run by double clicking on them in Finder or in the Terminal by prefixing a `./`, e.g. `./tether`


1. After plugging in all of the cameras, run `init`. This will create a file called `tether`. You will need run `init` this every time there's a hardware change. If `init` can't find all the cameras specified in `cameras.py`, it will print out the missing ones and wait until you press enter to continue.

2. To run the tethering, execute `tether`. This will populate the right folders when the photos get tethered.

3. When you're done, or something goes wrong, execute the `stop`.

Making GIFs
-----------

Run `make-gif`, this will take photos from the folders, create GIFs and show them in Safari.

**Parameters**

- Framerate: this is set a delay between frames, it's on line 59 of `make-gif`. The value is in 1/100ths of a second
- Size: On line 54, change the number after `-resize`. If you omit a the number after the `x` it will scale proportionately.
