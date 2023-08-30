if not exist "build" mkdir build
cd build

python ..\test\test.py

cl ..\test\test.c /Fotest_c.obj /Fetest_c.exe
test_c.exe

cd ..