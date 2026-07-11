%global tl_name pictex2
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adds relative coordinates and improves the \plot command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pictex2/pictex2.sty
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pictex2.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Adds two user commands to standard PiCTeX. One command uses relative
coordinates, thus eliminating the need to calculate the coordinate of
every point manually as in standard PiCTeX. The other command modifies
\plot to use a rule instead of dots if the line segment is horizontal or
vertical.

