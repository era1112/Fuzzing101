Name: libexif
Summary: EXIF tag library
Version: 0.6.14
Release: 2
Source: http://prdownloads.sourceforge.net/libexif/%{name}-%{version}.tar.gz
Url: http://sourceforge.net/projects/libexif/
Group: System Environment/Libraries
License: GPL
# replaced Packager: header, as most people making packages will be somebody
# else. original spec file author is Mark Pulford <mark@kyne.com.au>
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}

%description
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace lots of redundant implementations in command-line
utilities and programs with GUIs.

%package devel
Summary: The files needed for libexif application development
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libexif-devel package contains the libraries and include files
that you can use to develop libexif applications.

%prep
%setup

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_libdir}/libexif.so.*
%{_libdir}/libexif.so
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/libexif.pc
%{_includedir}/libexif
%{_libdir}/libexif.la
%{_libdir}/libexif.a

