%global tl_name idxcmds
%global tl_revision 54554

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2c
Release:	%{tl_revision}.1
Summary:	Semantic commands for adding formatted index entries
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/idxcmds
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/idxcmds.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands for adding formatted index entries; it
arises from the author's work on large documents.

