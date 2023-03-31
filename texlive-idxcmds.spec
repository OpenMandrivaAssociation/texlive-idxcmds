Name:		texlive-idxcmds
Version:	54554
Release:	2
Summary:	Semantic commands for adding formatted index entries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/idxcmds
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
