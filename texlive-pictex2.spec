# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pictex2/pictex2.sty
# catalog-date 2007-01-13 09:26:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pictex2
Version:	20180303
Release:	1
Summary:	Adds relative coordinates and improves the \plot command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pictex2/pictex2.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex2.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070113-2
+ Revision: 754902
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070113-1
+ Revision: 719258
- texlive-pictex2
- texlive-pictex2
- texlive-pictex2
- texlive-pictex2

