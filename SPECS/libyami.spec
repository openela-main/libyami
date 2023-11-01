Name:		libyami
Version:	1.3.1
Release:	1%{?dist}
Summary:	Yet Another Media Infrastructure library.

License:	ASL 2.0
URL:		https://github.com/01org/libyami
#Source0:	git source https://github.com/01org/libyami/archive/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: libX11, libX11-devel, libva, libva-devel
BuildRequires: xorg-x11-proto-devel, mt-st

%description
Yet Another Media Infrastructure.
It is YUMMY to your video experience on Linux like platform.
Yami is core building block for media solution. it parses video stream
and decodes them leverage hardware acceleration.

%prep
%autosetup 
autoreconf -vif

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_includedir}/libyami
%{_libdir}/libyami.so*
%{_libdir}/pkgconfig/libyami.pc



%changelog
* Wed Dec 05 2018 Josef Ridky <jridky@redhat.com> - 1.3.1-1
- update to new upstream version (1.3.1)

* Mon Jan 15 2018 Josef Ridky <jridky@redhat.com> - 1.2.0-2
- Resolve: #1530206 - add missing make statement

* Mon Nov 06 2017 Josef Ridky <jridky@redhat.com> - 1.2.0-1
- Initial commit
