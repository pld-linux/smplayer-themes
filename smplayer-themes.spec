Summary:	Themes icons for SMPlayer
Summary(pl.UTF-8):	Motywy graficzne dla SMPlayera
Name:		smplayer-themes
Version:	20120919
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	4af3433f2fc7a4b543e576fb7985eb35
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
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/Gartoon
%{_datadir}/smplayer/themes/Gnome
%{_datadir}/smplayer/themes/Monochrome
%{_datadir}/smplayer/themes/Noia
%{_datadir}/smplayer/themes/Nuvola
%{_datadir}/smplayer/themes/Oxygen
%{_datadir}/smplayer/themes/Oxygen-Air
%{_datadir}/smplayer/themes/Oxygen-Refit
%{_datadir}/smplayer/themes/Silk
%{_datadir}/smplayer/themes/Tango
%{_datadir}/smplayer/themes/blackPanther-Light
%{_datadir}/smplayer/themes/blackPanther-Real
%{_datadir}/smplayer/themes/blackPanther-VistaLike
