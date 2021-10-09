#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Convert OCaml parsetrees between different major versions
Summary(pl.UTF-8):	Konwersja drzew analizy OCamla między głównymi wersjami
# "ocaml-" prefix + "ocaml-migrate-parsetree" library name
Name:		ocaml-ocaml-migrate-parsetree
Version:	2.2.0
Release:	1
License:	LGPL v2.1 with linking exception
Group:		Libraries
#Source0Download: https://github.com/ocaml-ppx/ocaml-migrate-parsetree/releases
Source0:	https://github.com/ocaml-ppx/ocaml-migrate-parsetree/releases/download/v%{version}/ocaml-migrate-parsetree-v%{version}.tbz
# Source0-md5:	1d2699aab74fcd46b71178b4f3ccbcb5
URL:		https://github.com/ocaml-ppx/ocaml-migrate-parsetree
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml < 1:4.14
BuildRequires:	ocaml-dune >= 2.3
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
This library converts between parsetrees of different OCaml versions
(from 4.02 through 4.13).

This package contains files needed to run bytecode executables using
migrate-parsetree library.

%description -l pl.UTF-8
Ta biblioteka dokonuje przekształceń drzew analizy między różnymi
wersjami OCamla (od 4.02 do 4.13).

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki migrate-parsetree.

%package devel
Summary:	Convert OCaml parsetrees between different major versions - development part
Summary(pl.UTF-8):	Konwersja drzew analizy OCamla między głównymi wersjami - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
migrate-parsetree library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki migrate-parsetree.

%prep
%setup -q -n ocaml-migrate-parsetree-v%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ocaml-migrate-parsetree/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ocaml-migrate-parsetree

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ocaml-migrate-parsetree
%{_libdir}/ocaml/ocaml-migrate-parsetree/META
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmi
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmt
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmti
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.a
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmx
%{_libdir}/ocaml/ocaml-migrate-parsetree/*.cmxa
%endif
%{_libdir}/ocaml/ocaml-migrate-parsetree/dune-package
%{_libdir}/ocaml/ocaml-migrate-parsetree/opam
