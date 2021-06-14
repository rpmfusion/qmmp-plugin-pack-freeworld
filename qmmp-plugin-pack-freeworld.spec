Name:           qmmp-plugin-pack-freeworld
Version:        1.5.0
Release:        1%{?dist}
Summary:        A set of extra plugins for Qmmp

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://qmmp.ylsoftware.com/plugins.php
Source0:        http://qmmp.ylsoftware.com/files/plugins/qmmp-plugin-pack-%{version}.tar.bz2
Source1:        qmmp-plugin-pack-filter-provides.sh
%define         _use_internal_dependency_generator 0
%define         __find_provides %{_builddir}/%{buildsubdir}/qmmp-plugin-pack-filter-provides.sh

BuildRequires:  qmmp-devel >= 1.5.0
BuildRequires:  cmake
BuildRequires:  ffmpeg-devel
BuildRequires:  qt5-linguist
#BuildRequires:  taglib-devel

%description
Plugins for Qmmp from Qmmp Plugin Pack that cannot be included in Fedora.

 * FFVideo - video playback engine based on FFmpeg library

%prep
%setup -q -n qmmp-plugin-pack-%{version}
cp %{SOURCE1} .
chmod +x qmmp-plugin-pack-filter-provides.sh

%build
%cmake \
    -D USE_YTB:BOOL=FALSE \
    -D USE_FFAP:BOOL=FALSE \
    -D USE_XMP:BOOL=FALSE \
    -D USE_SRC:BOOL=FALSE \
    -D USE_GOOM:BOOL=FALSE \
    -D PLUGIN_DIR=%{_lib}/qmmp \
    .
make %{?_smp_mflags} -C %{_vpath_builddir}/src/Engines/ffvideo


%install
make DESTDIR=%{buildroot} install -C %{_vpath_builddir}/src/Engines/ffvideo


%files
%doc AUTHORS COPYING ChangeLog.rus README README.RUS
%{_libdir}/qmmp/Engines/*.so


%changelog
* Wed Jun 09 2021 Karel Volný <kvolny@redhat.com> 1.5.0-1
- new version 1.5.0

* Wed May 12 2021 Karel Volný <kvolny@redhat.com> 1.4.1-1
- new version 1.4.1

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-2
- Rebuilt for new ffmpeg snapshot

* Tue Aug 18 2020 Karel Volný <kvolny@redhat.com> 1.4.0-1
- new version 1.4.0
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php
- adapted to F33 System-Wide Change: CMake to do out-of-source builds

* Tue Mar 31 2020 Karel Volný <kvolny@redhat.com> 1.3.2-1
- new version 1.3.2
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Karel Volný <kvolny@redhat.com> 1.3.1-1
- new version 1.3.1
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.2.3-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Karel Volný <kvolny@redhat.com> 1.2.3-1
- new version 1.2.3
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Thu Jul 26 2018 Karel Volný <kvolny@redhat.com> 1.2.2-1
- new version 1.2.2
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Mon Jun 04 2018 Karel Volný <kvolny@redhat.com> 1.2.1-1
- new version 1.2.1
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php
- includes only ffvideo, the rest is in Fedora

* Mon Jul 11 2016 Karel Volný <kvolny@redhat.com> 1.1.1-1
- new version 1.1.1
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php
- uses Qt5

* Mon Jan 04 2016 Karel Volný <kvolny@redhat.com> 0.9.3-1
- new version 0.9.3
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Mon Jun 29 2015 Karel Volný <kvolny@redhat.com> 0.8.3-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jan 24 2014 Karel Volný <kvolny@redhat.com> 0.7.4-1
- new version
- see the upstream changelog at http://qmmp.ylsoftware.com/index.php

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.7.2-2
- Rebuilt

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
