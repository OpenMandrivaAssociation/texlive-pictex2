Name:		texlive-pictex2
Version:	15878
Release:	2
Summary:	Adds relative coordinates and improves the \plot command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pictex2/pictex2.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex2.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Adds two user commands to standard PiCTeX. One command uses
relative coordinates, thus eliminating the need to calculate
the coordinate of every point manually as in standard PiCTeX.
The other command modifies \plot to use a rule instead of dots
if the line segment is horizontal or vertical.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pictex2/pictex2.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
