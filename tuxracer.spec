Summary:	Tux Racer game
Summary(pl):	Gra Tux Racer
Name:		tuxracer
Version:	0.61
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/tuxracer/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/tuxracer/%{name}-data-%{version}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.tuxracer.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	tcl-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1


%description
Tux Racer lets you take on the role of Tux the Linux Penguin as he races
down steep, snow-covered mountains. Enter cups and compete to win the 
title! Tux Racer includes a variety of options for gameplay, including 
the ability to race courses in fog, at night, and under high winds

%description -l pl
Tux Racer pozwala ci wcieliæ siê w rolê Tuxa, Linuksowego Pingwina
podczas zjazdu w dó³ pokrytych ¶niegiem gór. We¼ udzia³ w zawodach i
zdob±d¼ tytu³! Tux Racer zawiera wiele opcji, miêdzy innymi mo¿liwo¶æ
zje¿d¿ania we mgle, w nocy i podczas silnego wiatru.

%prep
%setup -q -a 1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_applnkdir}/Games/Racing,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games/Racing
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f %{name}-data-%{version}/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog html/*
%attr(755,root,root) %{_bindir}/tuxracer
%{_datadir}/%{name}
%{_applnkdir}/Games/Racing/*.desktop
%{_pixmapsdir}/*
