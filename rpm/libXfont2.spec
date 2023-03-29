Name:       libXfont2
Version:    2.0.6
Release:    1%{?dist}
Summary:    X font handling library for server & utilities
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libxfont
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto) >= 2.1.3
BuildRequires:  pkgconfig(xorg-macros) >= 1.10
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(zlib)

%description
libXfont provides the core of the legacy X11 font system, handling the index
files (fonts.dir, fonts.alias, fonts.scale), the various font file formats,
and rasterizing them.  It is used by the X display servers (Xorg, Xvfb, etc.)
and the X Font Server (xfs), but should not be used by normal X11 clients.  X11
clients access fonts via either the new APIs in libXft, or the legacy APIs in
libX11.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure --disable-freetype
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/X11/fonts/libxfont2.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xfont2.pc
