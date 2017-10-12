#!/bin/sh
rm -f c_files.zip test_autotest/c_files.zip
ln -sf lab.autotest/t1.txt
ln -sf lab.autotest/t2.txt
ln -sf lab.autotest/t3.txt
cd solutions
ln -sf ../lab.autotest/t1.txt
ln -sf ../lab.autotest/t2.txt
ln -sf ../lab.autotest/t3.txt
cd ../test.autotest
zip -qr ../c_files.zip *.[ch]
