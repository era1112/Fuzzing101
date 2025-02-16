Name: exif
Summary: A utility to display exif headers from jpeg files
Version: 0.6.15
Release: 1
Source: http://prdownloads.sourceforge.net/libexif/exif-%{version}.tar.gz
Url: http://sourceforge.net/projects/libexif/
Group: Applications/Multimedia
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libexif-devel, libmnote-devel
Requires: libexif, libmnote

%description
'exif' is a small command-line utility to show EXIF information hidden
in JPEG files. I wrote it to demonstrate the power of libexif.

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
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
