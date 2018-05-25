# Running Windows Application on the EnvoyAI Platform
The EnvoyAI Platofrm does not currently support Windows docker containers, 
but it still can support many types of windows applications and executables
via Wine.

### What is Wine
Wine is a very mature open source project that, for the past 25 years, has
been developing a solution to run Windows applications on Linux Operating
Systems. Wine is capable of running AAA Windows only video games, Intensive
professional applications, and has support for all Visual Studio C++ Redistributables.
To learn more please visit [winehq.org](https://www.winehq.org/)

### How to the example works
The docker file installs wine, along with winetricks, which provides an
easy to use mechanism to install common dependencies like the VS C++ Resitributables.
Because many Windows and thus Wine applications require a GUI, we include
Xvfb, which provides a virtual X-Windows display without actual screen output.
It can be used to run installers and your application itself with the xvfb-run tool.

HelloWindows is a C++ Windows CLI application created in Visual Studio 2017
on Windows 10 Pro. The application was built in 'Release' mode (not 'Debug'
mode, which requires debug versions of the VS C++ redistributables). It
performs the exact same task as the [test-hello](../test-hello) example.
Unlike test-hello, because it compiles to a windows .EXE, it cannot be run
in a Linux docker container without Wine.

### Try with your code
To modify this Dockerfile to run your own exe, you must edit the line below
to copy the EXE, along with any required DLLs, to the /prog directory:
```dockerfile
ADD HelloWindows/Release /prog
```

Then edit runWine.sh to call your EXE. As described above we use xvfb-run
to run your exe inside of wine:
```bash
xvfb-run wine HelloWindows.exe
```

#### Potential issue with Windows FilePaths
Windows applications typically use drive letters and back slashes: `C:\Data\`.
Recent versions of windows can accept paths without drive letters and with
forward slashes `/envoyai/input/`. This is especially convenient for our
usa, it is suggested that any code that reads inputs, or writes outputs
simply use the unix style paths. If files must be access or saved in a different
part of the windows filesystem, then it is suggested that the `runWine.sh`
script move files into place before and/or after executing the windows code.

#### GPU usage in Wine
Wine does have OpenGL and DirectX support, so it is theoretically possible
to make sure of a GPU in Wine. However, with the additional complexities of doing
this inside of a docker container, this feature is not yet available on the
EnvoyAI platform. Please contact us if this is an important feature to you.
