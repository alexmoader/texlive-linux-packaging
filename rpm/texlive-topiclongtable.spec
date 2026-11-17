%define oname topiclongtable

Summary:	Extend longtable with cells that merge hierarchically
Name:		texlive-topiclongtable
Version:	54758
Release:	1
License:	LPPL1.3
Group:		Publishing
Url:		http://www.ctan.org
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/%{oname}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/%{oname}.doc.tar.xz
BuildRequires:	texlive-tlpkg
Requires:	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	tex(zref-abspage.sty)
Provides:	tex(topiclongtable.sty) = 2024
BuildArch:	noarch

%description
This LaTeX package extends longtable implementing cells that:
merge with the one above if it has the same content, do not
merge with the one above unless the ones on the left are
merged, are well behaved with respect to longtable chunking on
page breaks, and automatically draw the correct separation
lines. The typical use case is a table spanning multiple pages
that contains a list of hierarchically organized topics (hence
the package name). The package depends on array, expl3,
longtable, multirow, xparse, and zref-abspage.

%files
%doc %{_texmfdistdir}/doc/latex/topiclongtable
%{_texmfdistdir}/tex/latex/topiclongtable

#------------------------------------------------------------------

%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
rm -rf tlpkg
cp -fpar * %{buildroot}%{_texmfdistdir}
