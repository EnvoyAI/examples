# Running Windows Application on the EnvoyAI Platform
The EnvoyAI Platofrm does not currently support Windows docker containers, 
but it still can support many types of windows applications and executables via Wine.
### What is Wine
Wine is a very mature open source project that, for the past 25 years, has been developing
a solution to running Windows application on Linux Operation Systems. To learn more please
visit [winehq.org](https://www.winehq.org/)

### Still skeptical?
Wine is even capable of running AAA Windows only video, Intensive professional applications, and has support for all
Visual Studio C++ Redistributables.

### How to
You'll see the docker file installs wine, along with winetricks, which provides an easy to use mechanism to install common
dependencies like the VS C++ Resitributables. Because many Windows and thus Wine applications require a GUI, we are forced
to use Xvfb, which acts like a virtual X-Windows display. It works pretty well to run any installers, and your application
intslef with the xvfb-run tool which creates a virtual GUI for the program passed as arguments to it. 

### The Example explained
HelloWindows is a C++ Windows CLI application created in Visual Studio 2017 on Windows 10 Pro. The application was built
in 'Release' mode (not 'Debug' mode). It simply reads from `/envoyai/input/name` and writes to `/envoyai/output/hello` similar
to [test-hello](../test-hello). Because it compiles to a windows .EXE, it cannot be run in a Linux docker container without Wine.
As explained above the [Dockerfile](./Dockerfile) installs Wine, winetricks, xvfb, along with the Visual Studio 2015 and
2010 C++ Redistributables. 

Working from this Dockerfile, to run an exe one must simply copy the EXE, along with any statically linked DLLs, as shown in the Dockerfile:
```dockerfile
ADD HelloWindows/Release /prog
```

And edit runWine.sh to call the EXE. As described above we run the exe inside of wine, inside of xvfb-run:
```bash
xvfb-run wine HelloWindows.exe
```