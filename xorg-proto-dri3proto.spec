Summary:	DRI3 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI3
Name:		xorg-proto-dri3proto
Version:	1.0
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dri3proto-%{version}.tar.bz2
# Source0-md5:	a3d2cbe60a9ca1bf3aea6c93c817fee3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRI3 (Direct Rendering Infrastructure 3) extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia DRI3 (Direct Rendering Infrastructure 3).

%package devel
Summary:	DRI3 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI3
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DRI3 (Direct Rendering Infrastructure 3) extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia DRI3 (Direct Rendering Infrastructure 3).

%prep
%setup -q -n dri3proto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc ChangeLog dri3proto.txt
%{_includedir}/X11/extensions/dri3proto.h
%{_pkgconfigdir}/dri3proto.pc
