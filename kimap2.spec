%define major 0
%define libname %mklibname KIMAP2 %{major}
%define devname %mklibname KIMAP2 -d
# Doesn't follow usual versioning schemes yet -- always unstable for now
%define stable unstable

Name:		kimap2
Version:	0.2.0
Release:	1
Source0:	http://download.kde.org/%{stable}/kimap2/%{version}/src/%{name}-%{version}.tar.xz
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
%setup -q
%apply_patches
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
