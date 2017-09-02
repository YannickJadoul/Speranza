Findings 02/09/2017
===================
- pyinstrument_cext: seems to be working (tested 32 and 64 bit 2.7), and to be linked against the right 90 DLL. However, only C code. Uses cibuildwheel.
- Our copy of pybind python_example: does not work in either 32 and 64 bit. Linked against both VCRUNTIME140.DLL as well as MSVCP140.DLL.

TODO
- Test: C vs. C++ - build pyinstrument_cext as C++ code?
- Test: build python_example with cibuildwheel.
- Make sure to keep an eye on both 32 and 64, because 64 bit seems to not be the only problematic case.


