%define major 5
%define libname %mklibname qt5purchasing %{major}
%define devname %mklibname qt5purchasing -d
%define beta %{nil}

Name:	qt5-qtpurchasing
Version: 5.9.0
Release: 0.%{beta}.1
%if "%{beta}" != "%{nil}"
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/qtpurchasing-opensource-src-%{version}-%{beta}.tar.xz
%else
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/qtpurchasing-opensource-src-%{version}.tar.xz
%endif
Summary: Qt library for in-app purchases
URL: https://github.com/qtproject/qtpurchasing
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)

%description
Qt library for in-app purchases

%package -n %{libname}
Summary: Qt library for in-app purchases
Group: System/Libraries

%description -n %{libname}
Qt library for in-app purchases

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package examples
Summary: Example code for the %{name} library
Group: Development/C
Requires: %{devname} = %{EVRD}
BuildRequires: pkgconfig(Qt5Widgets)

%description examples
Example code for the %{name} library

%prep
%if "%{beta}" != "%{nil}"
%setup -qn qtpurchasing-opensource-src-%{version}-%{beta}
%else
%setup -qn qtpurchasing-opensource-src-%{version}
%endif
%qmake_qt5 *.pro

%build
%make

%install
make install install_docs INSTALL_ROOT="%{buildroot}"
find "%{buildroot}" -type f -name '*.prl' -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/qml/QtPurchasing

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Qt5Purchasing
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/*.prl

%files examples
%{_libdir}/qt5/examples/purchasing
