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
#Patch0:		-
URL:		http://www.tuxracer.com/
#BuildPrereq:	-
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
#Prereq:		-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description

%description -l pl

%prep
%setup  -q
#%patch0 -p1

%build
#rm -f missing
#libtoolize --copy --force
#gettextize --copy --force
#aclocal
#autoconf
#automake -a -c

#CPPFLAGS="-I/usr/X11R6/include"
#export CFLAGS

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
