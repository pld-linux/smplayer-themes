Summary:	Themes icons for SMPlayer
Summary(pl.UTF-8):	Motywy graficzne dla SMPlayera
Name:		smplayer-themes
Version:	0.1.2
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://smplayer.sourceforge.net/linux/download/%{name}-%{version}.tar.gz
# Source0-md5:	8b0601ed48f0c02e59d5c788a127d056
URL:		http://smplayer.sourceforge.net/
Requires:	smplayer >= 0.4.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
