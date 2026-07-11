%global tl_name pbalance
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Balance last page in two-column mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pbalance
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package balances the columns on the last page of a two-column
document. If the page is "simple" (no footnotes, floats, or marginpars),
is uses the balance package; otherwise, it uses \enlargethispage to make
the left column shorter, balancing the columns.

