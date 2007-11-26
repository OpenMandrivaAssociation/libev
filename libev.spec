%define name libev
%define version 1.4.0
%define prerel beta
%define release %mkrel 0.%prerel.1
%define api 1.4
%define major 2
%define libname %mklibname ev %api %major
%define develname %mklibname -d ev

Summary: High-performance event loop/event model
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://dist.schmorp.de/libev/%{name}-%{version}-%prerel.tar.gz
License: BSD
Group: System/Libraries
Url: http://software.schmorp.de/pkg/libev.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent
(http://monkey.org/~provos/libevent/) and the Event perl module, but
aims to be faster and more correct, and also more featureful.

%package -n %libname
Summary: High-performance event loop/event model
Group: System/Libraries

%description -n %libname
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent
(http://monkey.org/~provos/libevent/) and the Event perl module, but
aims to be faster and more correct, and also more featureful.

%package -n %develname
Summary: High-performance event loop/event model
Group: Development/C
Requires: %libname = %version

%description -n %develname
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent
(http://monkey.org/~provos/libevent/) and the Event perl module, but
aims to be faster and more correct, and also more featureful.

%prep
%setup -q -n %name-%version-%prerel

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/libev*-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc README
%_bindir/event_rpcgen.py
%_includedir/ev*.h
%_libdir/libev*.a
%_libdir/libev*.so
%_libdir/libev*.la
%_mandir/man3/ev*

