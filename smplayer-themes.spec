Summary:	Themes icons for SMPlayer
Summary(pl.UTF-8):	Motywy graficzne dla SMPlayer
Name:		smplayer-themes
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://smplayer.sourceforge.net/
Source0:	http://smplayer.sourceforge.net/linux/download/%{name}-%{version}.tar.gz
# Source0-md5:	1c1e241522ba0262b1363e3acebb3e32
Requires:	smplayer >= 0.4.12
BuildArch:	noarch

%description
This package provides icon themes for SMPlayer.

%description -l pl.UTF-8
Ten pakiet dostarcza róźne motywy graficzne dla SMPlayera.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/smplayer/themes
