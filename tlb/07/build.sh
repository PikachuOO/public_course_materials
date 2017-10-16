#!/bin/sh
for f in lab.autotest/song?.txt lab.autotest/lyrics
do
    ln -sf $f .
done
rm -f lyrics.zip
zip -qr lyrics.zip lyrics song?.txt
test -d solutions || exit
cd solutions
ln -sf ../lyrics .
for f in ../song?.txt
do
    ln -sf "$f"
done
