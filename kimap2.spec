%define major 0
%define libname %mklibname KIMAP2 %{major}
%define devname %mklibname KIMAP2 -d
# Doesn't follow usual versioning schemes yet -- always unstable for now
%define stable unstable
%define snapshot %{nil}

Name:		kimap2
Version:	0.4.0
Release:	2
#Source0:	http://download.kde.org/%{stable}/kimap2/%{version}/src/%{name}-%{version}.tar.xz
Source0:  https://invent.kde.org/pim/kimap2/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Summary:	KDE library for handling the IMAP protocol
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Mime)
BuildRequires: pkgconfig(libsasl2)

%description
KDE library for handling the IMAP protocol

%package -n %{libname}
Summary: KDE library for handling the IMAP protocol
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for accessing data over DAV

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
rm -f %{buildroot}%{_libdir}/libkimap2test.a

%files

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
