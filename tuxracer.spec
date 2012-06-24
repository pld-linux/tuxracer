Summary:	Tux Racer game
Summary(pl):	Gra Tux Racer
Name:		tuxracer
Version:	0.61
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/tuxracer/%{name}-%{version}.tar.gz
Source1:	http://download.sourceforge.net/tuxracer/%{name}-data-%{version}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.tuxracer.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Tux Racer lets you take on the role of Tux the Linux Penguin as he races down
steep, snow-covered mountains. Enter cups and compete to win the title! Tux
Racer includes a variety of options for gameplay, including the ability to race
courses in fog, at night, and under high winds

%description -l pl
Tux Racer pozwala ci wcieli� si� w rol� Tuxa, Linuksowego Pingwina podczas zjazdu
w d� pokrytych �niegiem g�r. We� udzia� w zawodach i zdob�d� tytu�! Tux Racer
zawiera wiele opcji, mi�dzy innymi mo�liwo�� zje�d�ania we mgle, w nocy i podczas
silnego wiatru.

%prep
%setup -q -a 1

%build
automake -a
aclocal
autoconf
%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games
%{__install} %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f %{name}-data-%{version}/* $RPM_BUILD_ROOT%{_datadir}/%{name}

gzip -9nf AUTHORS NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz html
%attr(755,root,root) %{_bindir}/tuxracer
%{_datadir}/%{name}
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
