Summary:	Tux Racer game
Summary(pl):	Gra Tux Racer
Name:		tuxracer
Version:	0.61
Release:	7
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
URL:		http://www.tuxracer.com/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.4.3
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Tux Racer lets you take on the role of Tux the Linux Penguin as he
races down steep, snow-covered mountains. Enter cups and compete to
win the title! Tux Racer includes a variety of options for gameplay,
including the ability to race courses in fog, at night, and under high
winds.

%description -l pl
Tux Racer pozwala wcieliæ siê w rolê Tuksa, Linuksowego Pingwina
podczas zjazdu w dó³ pokrytych ¶niegiem gór. We¼ udzia³ w zawodach i
zdob±d¼ tytu³! Tux Racer zawiera wiele opcji, miêdzy innymi mo¿liwo¶æ
zje¿d¿ania we mgle, w nocy i podczas silnego wiatru.

%prep
%setup -q -a1 -a2
%patch -p1

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
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_applnkdir}/Games/Racing,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Games/Racing
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
%{_applnkdir}/Games/Racing/*.desktop
%{_pixmapsdir}/*
