Name:		texlive-seu-ml-assign
Version:	62933
Release:	2
Summary:	Southeast University Machine Learning Assignment template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/seu-ml-assign
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seu-ml-assign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seu-ml-assign.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a template for the Southeast University Machine
Learning Assignment that can be easily adapted to other usages.
This template features a colorful theme that makes it look
elegant and attractive. You can also find the template
available on Overleaf.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/seu-ml-assign
%doc %{_texmfdistdir}/doc/latex/seu-ml-assign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
