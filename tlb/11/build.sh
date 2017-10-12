#!/bin/sh
unset CDPATH
rm -rf tmp game.zip peer.zip
mkdir  tmp || exit
cp students.txt tmp
cp solutions/peer_starting_code.py tmp/peer.py
cp solutions/peer_starting_code.cgi tmp/peer.cgi
cp solutions/game_starting_code.py tmp/game.py
cp solutions/game_starting_code.cgi tmp/game.cgi
cp solutions/*.html tmp
rsync -a assessments/ tmp/assessments/
cd tmp || exit
rm -f game_success.html peer_assessments.html
chmod 700 *.py *.cgi
chmod 600 *.html
zip -qr ../peer.zip peer* assessments students.txt
zip -qr ../game.zip game*
cd ..
rm -rf tmp
