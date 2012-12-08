%define major 4
%define libname %mklibname ev %{major}
%define develname %mklibname ev -d

Summary:	High-performance event loop/event model
Name:		libev
Epoch:		1
Version:	4.11
Release:	5
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

%description -n %{develname}
This is the development files needed in order to develop applications using
libev.

%prep
%setup -q

# Add pkgconfig support
cp -p %{SOURCE1} .
sed -i -e 's|Makefile|Makefile libev.pc|' configure.ac configure
sed -i -e 's|lib_LTLIBRARIES|pkgconfigdir = $(libdir)/pkgconfig\n\npkgconfig_DATA = libev.pc\n\nlib_LTLIBRARIES|' \
    Makefile.am Makefile.in 
aclocal
automake

%build
%configure2_5x --disable-static \
	       --includedir=%{_includedir}/%{name}
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README
%{_includedir}/%{name}/ev*.h
%{_libdir}/libev*.so
%{_libdir}/pkgconfig/%{name}.pc 
%{_mandir}/man3/ev*


%changelog
* Fri Aug 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:4.11-5
+ Revision: 816137
- Rebuild in main.
- Rebuild and move to main.

* Thu Jun 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:4.11-4
+ Revision: 803124
- rebuild

* Wed Jun 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:4.11-3
+ Revision: 802893
- oops epoch downgraded to 1 and rel bump to 2
- rel up
- resolved conflict with libevent and libev event.h file
- version update 4.11

* Tue Nov 01 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:4.04-1
+ Revision: 709244
- update to new version 4.04
- bump major to 4

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.9-3mdv2011.0
+ Revision: 609742
- rebuild

* Sat Feb 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.9-2mdv2010.1
+ Revision: 501398
- add pkgconfig support

* Sun Jan 03 2010 Frederik Himpe <fhimpe@mandriva.org> 1:3.9-1mdv2010.1
+ Revision: 485975
- update to new version 3.9

  + Michael Scherer <misc@mandriva.org>
    - add a Conflict with libevent, as they both have the same header

* Sun Aug 09 2009 Frederik Himpe <fhimpe@mandriva.org> 1:3.8-1mdv2010.0
+ Revision: 412926
- update to new version 3.8

* Sun Jul 19 2009 Funda Wang <fwang@mandriva.org> 1:3.7-1mdv2010.0
+ Revision: 397414
- New version 3.7

* Mon Feb 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.53-1mdv2009.1
+ Revision: 340738
- update to new version 3.53

* Sat Jan 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.52-1mdv2009.1
+ Revision: 328092
- update to new version 3.52

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 3.51-1mdv2009.1
+ Revision: 319983
- new version 3.51

* Wed Nov 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.49-1mdv2009.1
+ Revision: 304484
- update to new version 3.49

* Fri Oct 31 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.48-1mdv2009.1
+ Revision: 298967
- update to new version 3.48

* Wed Oct 22 2008 Funda Wang <fwang@mandriva.org> 3.45-1mdv2009.1
+ Revision: 296349
- New version 3.45

* Sat Oct 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.44-1mdv2009.1
+ Revision: 292467
- update to new version 3.44

* Mon Jul 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.43-1mdv2009.0
+ Revision: 239434
- update to new version 3.43

* Sun Jun 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.42-1mdv2009.0
+ Revision: 227861
- update to new version 3.42

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.41-1mdv2009.0
+ Revision: 211227
- obsolete old libname
- update to new version 3.41
- spec file clean

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix devel description
    - remove libevent URL

* Mon Nov 26 2007 Götz Waschk <waschk@mandriva.org> 1.4.0-0.beta.1mdv2008.1
+ Revision: 112064
- import libev

