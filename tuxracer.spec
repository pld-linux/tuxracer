Summary:	Tux Racer game
Summary(pl):	Gra TuxRacer
Name:		tuxracer
Version:	0.61
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://download.sourceforge.net/tuxracer/%{name}-%{version}.tar.gz
Source1:	http://download.sourceforge.net/tuxracer/%{name}-data-%{version}.tar.gz
URL:		http://www.tuxracer.com/
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
Tux Racer pozwala ci wcieliæ siê w rolê Tuxa, Linuksowego Pingwina podczas zjazdu
w dó³ pokrytych ¶niegiem gór. We¼ udzia³ w zawodach i zdob±d¼ tytu³! Tux Racer
zawiera wiele opcji, miêdzy innymi mo¿liwo¶æ zje¿d¿ania we mgle, w nocy i podczas
silnego wiatru.

%prep
%setup  -q

%build
%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}
cd $RPM_BUILD_ROOT%{_datadir}
tar xfz %{SOURCE1}
mv %{name}{-data-%{version},}
cd -

gzip -9nf AUTHORS NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/tuxracer
%{_datadir}/%{name}
