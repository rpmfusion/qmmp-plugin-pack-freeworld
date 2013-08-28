Name:           qmmp-plugin-pack-freeworld
Version:        0.7.2
Release:        1%{?dist}
Summary:        A set of extra plugins for Qmmp

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://qmmp.ylsoftware.com/plugins.php
Source0:        http://qmmp.ylsoftware.com/files/plugins/qmmp-plugin-pack-%{version}.tar.bz2
Source1:        qmmp-plugin-pack-filter-provides.sh
%define         _use_internal_dependency_generator 0
%define         __find_provides %{_builddir}/%{buildsubdir}/qmmp-plugin-pack-filter-provides.sh

BuildRequires:  qmmp >= %{version}
BuildRequires:  qmmp-devel >= %{version}
BuildRequires:  cmake
BuildRequires:  libmpg123-devel
BuildRequires:  qt-devel
BuildRequires:  taglib-devel

%description
Plugins for Qmmp from Qmmp Plugin Pack that cannot be included in Fedora.

 * MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library

%prep
%setup -q -n qmmp-plugin-pack-%{version}
cp %{SOURCE1} .
chmod +x qmmp-plugin-pack-filter-provides.sh

%build
%cmake \
    -D USE_FFAP:BOOL=FALSE \
    -D USE_QSUI:BOOL=FALSE \
    .
make %{?_smp_mflags} -C src/Input/mpg123


%install
make DESTDIR=%{buildroot} install -C src/Input/mpg123


%files
%doc AUTHORS COPYING ChangeLog.rus README README.RUS
%{_libdir}/qmmp/Input/*.so


%changelog
* Wed Aug 28 2013 Karel Volný <kvolny@redhat.com> 0.7.2-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Fri Jun 21 2013 Karel Volný <kvolny@redhat.com> 0.7.1-1
- new version

* Thu May 02 2013 Karel Volný <kvolny@redhat.com> 0.7.0-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index.php
- project URLs changed

* Tue Apr 02 2013 Karel Volný <kvolny@redhat.com> 0.6.6-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Jan 29 2013 Karel Volný <kvolny@redhat.com> 0.6.4-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Dec 11 2012 Karel Volný <kvolny@redhat.com> 0.6.3-1
- new version
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Fri Aug 24 2012 Karel Volný <kvolny@redhat.com> 0.6.2-2
- update spec to newer style as suggested in Fedora package review
- removed %%buildroot actions
- removed %%clean section which got empty
- removed %%defattr

* Fri Aug 17 2012 Karel Volný <kvolny@redhat.com> 0.6.2-1
- new version
- fixes FSF address issue found by rpmlint
- see upstream changelog at http://qmmp.ylsoftware.com/index_en.php

* Tue Jul 31 2012 Karel Volný <kvolny@redhat.com> 0.6.1-1
- initial RPM Fusion release
