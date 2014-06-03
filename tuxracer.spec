Summary:	Race down mountainous terrain with Tux!
Summary(pl.UTF-8):	Zjeżdżaj z Tuksem w górzystym terenie!
Summary(pt_BR.UTF-8):	Corra montanha abaixo com o Tux!
Summary(de.UTF-8):	Tux Racer ist ein 3D-Computerspiel
Name:		tuxracer
Version:	0.61
Release:	13
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/tuxracer/%{name}-%{version}.tar.gz
# Source0-md5:	206e8197ceaf0f00b25d4e2b4156e563
Source1:	http://dl.sourceforge.net/tuxracer/%{name}-data-%{version}.tar.gz
# Source1-md5:	aef877fee9e1a56483ff01fbdfb1e4b3
Source2:	http://brcha.free.fr/data/projects/RoadsOfSerbia/RoadsOfSerbia.tar.bz2
# Source2-md5:	5eff75e60b3d4a46f97bb697d968a299
Source3:	%{name}.desktop
Source4:	%{name}.png
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-build.patch
URL:		http://tuxracer.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.4.3
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Tux Racer lets you take on the role of Tux the Linux Penguin as he
races down steep, snow-covered mountains. Enter cups and compete to
win the title! Tux Racer includes a variety of options for gameplay,
including the ability to race courses in fog, at night, and under high
winds.

%description -l pl.UTF-8
Tux Racer pozwala wcielić się w rolę Tuksa, linuksowego Pingwina
podczas zjazdu w dół pokrytych śniegiem gór. Weź udział w zawodach i
zdobądź tytuł! Tux Racer zawiera wiele opcji, między innymi możliwość
zjeżdżania we mgle, w nocy i podczas silnego wiatru.

%description -l pt_BR.UTF-8
O objetivo do Tux Racer é diversão! Corra montanha abaixo tão rápido
quanto possível e capture peixes para aumentar sua pontuação!

%description -l de.UTF-8
Tux Racer ist ein 3D-Computerspiel, welches bei Linuxnutzern sehr
beliebt ist. Die Hauptfigur ist das Maskottchen Tux. Dieses muss man
durch geschicktes Steuern durch eine verschneite Eislandschaft
rutschen lassen. Dabei müssen manchmal Hindernisse umschifft und
Heringe gesammelt werden.

%prep
%setup -q -a1 -a2
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="%{rpmcflags} -DGLX_GLXEXT_LEGACY"
%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f %{name}-data-%{version}/* $RPM_BUILD_ROOT%{_datadir}/%{name}
mv -f Roads\ Of\ Serbia/ $RPM_BUILD_ROOT%{_datadir}/%{name}/courses/contrib/roads_of_serbia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog html/*
%attr(755,root,root) %{_bindir}/tuxracer
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
