if exist "build" del /S /Q build
mkdir build
cd build

python ..\test\test.py

cl ..\test\test.c /Fotest_c.obj /Fetest_c.exe
test_c.exe

cl ..\test\test.cpp /Fotest_cpp.obj /Fetest_cpp.exe /EHsc
test_cpp.exe

cd ..
