%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tcl-cmark
Summary:       Tcl bindings to the cmark-gfm CommonMark/Markdown library
Version:       1.0
Release:       0
License:       BSD-3 License
Group:         Development/Libraries/Tcl
Source:        tcl-cmark-1.0.tar.gz
Patch0:        version.patch
URL:           https://github.com/apnadkarni/tcl-cmark
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.5
BuildRequires: cmark-gfm-devel
Requires:      tcl >= 8.5
BuildRoot:     %{buildroot}

%description
tcl-cmark implementes Tcl bindings to the cmark-gfm Github Flavoured
CommonMark/Markdown library.

%prep
%setup -q -n %{name}-%{version}
%patch0 

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
%{directory}/share/man/mann

