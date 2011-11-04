# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pictex2/pictex2.sty
# catalog-date 2007-01-13 09:26:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pictex2
Version:	20070113
Release:	1
Summary:	Adds relative coordinates and improves the \plot command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pictex2/pictex2.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex2.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Adds two user commands to standard PiCTeX. One command uses
relative coordinates, thus eliminating the need to calculate
the coordinate of every point manually as in standard PiCTeX.
The other command modifies \plot to use a rule instead of dots
if the line segment is horizontal or vertical.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pictex2/pictex2.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
