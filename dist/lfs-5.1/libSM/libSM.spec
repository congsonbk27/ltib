%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : X.Org X11 libSM runtime library
Name            : libSM
Version         : 1.0.2
Release         : 5
License         : MIT/X11
Vendor          : Freescale
Packager        : LTIB addsrpms
Group           : System Environment/Libraries
URL             : http://www.x.org
Source0         : ftp://ftp.x.org/pub/individual/lib/libSM-1.0.2.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

NOTE: this was imported by ltib -m addsrpms libSM-1.0.2-5.fc9.src.rpm

%Prep

%setup -q


%Build
./configure \
    --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} \
	--disable-static
make


%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f


%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
