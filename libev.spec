%define major 4
%define libname %mklibname ev %{major}
%define devname %mklibname ev -d

Summary:	High-performance event loop/event model
Name:		libev
Epoch:		1
Version:	4.24
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://software.schmorp.de/pkg/libev.html
Source0:	http://dist.schmorp.de/libev/%{name}-%{version}.tar.gz
Source1:	%{name}.pc.in

%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent and the Event perl module,
but aims to be faster and more correct, and also more featureful.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	High-performance event loop/event model
Group:		System/Libraries

%description -n %{libname}
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent and the Event perl module,
but aims to be faster and more correct, and also more featureful.

%files -n %{libname}
%{_libdir}/libev.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	High-performance event loop/event model
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This is the development files needed in order to develop applications using
libev.

%files -n %{devname}
%doc README
%{_includedir}/%{name}/ev*.h
%{_libdir}/libev*.so
%{_libdir}/pkgconfig/%{name}.pc 
%{_mandir}/man3/ev*

#----------------------------------------------------------------------------

%prep
%setup -q
sed -i -e "/^AM_INIT_AUTOMAKE/a\ " configure.ac

# Add pkgconfig support
cp -p %{SOURCE1} .
sed -i -e 's|Makefile|Makefile libev.pc|' configure.ac configure
sed -i -e 's|lib_LTLIBRARIES|pkgconfigdir = $(libdir)/pkgconfig\n\npkgconfig_DATA = libev.pc\n\nlib_LTLIBRARIES|' \
    Makefile.am Makefile.in

%build
export CC=gcc
autoreconf -fiv
%configure \
	--disable-static \
	--includedir=%{_includedir}/%{name}
%make

%install
%makeinstall_std
