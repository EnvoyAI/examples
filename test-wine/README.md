# Running Windows Application on the EnvoyAI Platform
The EnvoyAI Platofrm does not currently support Windows docker containers, 
but it still can support many types of windows applications and executables via Wine.
### What is Wine
Wine is a very mature open source project that, for the past 25 years, has been developing
a solution to run Windows applications on Linux Operating Systems. To learn more please
visit [winehq.org](https://www.winehq.org/)

### Still skeptical?
Wine is even capable of running AAA Windows only video, Intensive professional applications, and has support for all
Visual Studio C++ Redistributables.

### How to
The docker file installs wine, along with winetricks, which provides an easy to use mechanism to install common
dependencies like the VS C++ Resitributables. Because many Windows and thus Wine applications require a GUI, we include Xvfb, 
which provides a virtual X-Windows display without actual screen output. It can be used to run installers and your application
itself with the xvfb-run tool.

### The Example explained
HelloWindows is a C++ Windows CLI application created in Visual Studio 2017 on Windows 10 Pro. The application was built
in 'Release' mode (not 'Debug' mode). It reads from `/envoyai/input/name` and writes to `/envoyai/output/hello`, much like the
 [test-hello](../test-hello) example. Because it compiles to a windows .EXE, it cannot be run in a Linux docker container without Wine.
As explained above the [Dockerfile](./Dockerfile) installs Wine, winetricks, xvfb, along with the Visual Studio 2015 and
2010 C++ Redistributables. 

To modify this Dockerfile to run your own exe, you must edit the line below to copy the EXE, along with any statically linked DLLs, to the /prog directory:
```dockerfile
ADD HelloWindows/Release /prog
```

Then edit runWine.sh to call your EXE. As described above we use xvfb-run to run your exe inside of wine:
```bash
xvfb-run wine HelloWindows.exe
```