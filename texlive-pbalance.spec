Name:		texlive-pbalance
Version:	64002
Release:	1
Summary:	Balance last page in two-column mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pbalance
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbalance.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package balances the columns on the last page of a
two-column document. If the page is "simple" (no footnotes,
floats, or marginpars), is uses the balance package; otherwise,
it uses \enlargethispage to make the left column shorter,
balancing the columns.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pbalance
%{_texmfdistdir}/tex/latex/pbalance
%doc %{_texmfdistdir}/doc/latex/pbalance

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
