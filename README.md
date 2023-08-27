# Simple cmake project

This is a simple cmake project created to demonstrate target dependencies and observe how these are built/linked together

The project has the following components

* Exe1 depends on LibB
* LibB depends on LibA
* LibA depends on custom targat Custom1

Note: Added a bunch of weird `#define` which serves the purpose of increasing the compile time for each class for easier dependency tracking