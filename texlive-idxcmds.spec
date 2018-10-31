# revision 31557
# category Package
# catalog-ctan /macros/latex/contrib/idxcmds
# catalog-date 2013-08-31 22:39:59 +0200
# catalog-license lppl1.3
# catalog-version 0.2a
Name:		texlive-idxcmds
Version:	0.2c
Release:	2
Summary:	Semantic commands for adding formatted index entries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/idxcmds
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands for adding formatted index
entries; it arises from the author's work on large documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/idxcmds/idxcmds.sty
%doc %{_texmfdistdir}/doc/latex/idxcmds/README
%doc %{_texmfdistdir}/doc/latex/idxcmds/idxcmds_en.pdf
%doc %{_texmfdistdir}/doc/latex/idxcmds/idxcmds_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
