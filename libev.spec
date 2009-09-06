%define major 3
%define libname %mklibname ev %{major}
%define develname %mklibname ev -d

Summary:	High-performance event loop/event model
Name:		libev
Epoch:		1
Version:	3.8
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
Url:		http://software.schmorp.de/pkg/libev.html
Source0:	http://dist.schmorp.de/libev/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent and the Event perl module,
but aims to be faster and more correct, and also more featureful.

%package -n %{libname}
Summary:	High-performance event loop/event model
Group:		System/Libraries
Obsoletes:	%mklibname ev 1.4 2

%description -n %{libname}
libev is a high-performance event loop/event model with lots of features.
(see benchmark at http://libev.schmorp.de/bench.html)

It is modelled (very losely) after libevent and the Event perl module,
but aims to be faster and more correct, and also more featureful.

%package -n	%{develname}
Summary:	High-performance event loop/event model
Group:		Development/C
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
# Installation failed:  file /usr/include/event.h from 
# install of lib64ev-devel-1:3.8-1mdv2010.0.x86_64 
# conflicts with file from package lib64event-devel-1.4.12-1mdv2010.0.x86_64
Conflicts:   %mklibname event -d 

%description -n %{develname}
This is the development files needed in order to develop applications using
libev.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%{_includedir}/ev*.h
%{_libdir}/libev*.a
%{_libdir}/libev*.so
%{_libdir}/libev*.la
%{_mandir}/man3/ev*
