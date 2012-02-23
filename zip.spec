# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       zip
Summary:    A file compression and packaging utility compatible with PKZIP
Version:    3.0
Release:    1
Group:      Applications/Archiving
License:    BSD
URL:        http://www.info-zip.org/Zip.html
Source0:    zip30.tar.gz
Source100:  zip.yaml
Patch0:     zip-3.0-exec-shield.patch
Patch1:     zip-3.0-currdir.patch
Patch2:     zip-3.0-time.patch


%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.




%prep
%setup -q -n %{name}30

# zip-3.0-exec-shield.patch
%patch0 -p1
# zip-3.0-currdir.patch
%patch1 -p1
# zip-3.0-time.patch
%patch2 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
make -f unix/Makefile prefix=%{_prefix} "CFLAGS_NOOPT=-I. -DUNIX $RPM_OPT_FLAGS" generic_gcc  %{?_smp_mflags}
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BULD_ROOT%{_mandir}/man1

make -f unix/Makefile prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install
# << install post






%files
%defattr(-,root,root,-)
# >> files
%doc README CHANGES TODO WHATSNEW WHERE LICENSE README.CR
%doc proginfo/algorith.txt
%{_bindir}/zipnote
%{_bindir}/zipsplit
%{_bindir}/zip
%{_bindir}/zipcloak
%doc %{_mandir}/man1/zip.1*
%doc %{_mandir}/man1/zipcloak.1*
%doc %{_mandir}/man1/zipnote.1*
%doc %{_mandir}/man1/zipsplit.1*
# << files


