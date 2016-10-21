This will build RPMs for the pyfacter library.

I wish Python had better native RPM support. 

Usage:

    yum groupinstall "Development Tools"
    yum install spectool
    make rpms

The rest is done by specfile.

Clones Source0: https://github.com/knorby/%{name}/archive/v%{version}.tar.gz, grabbing the name and version from those fields from spec.
