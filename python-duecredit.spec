%global modname duecredit

Name:           python-%{modname}
Version:        0.4.4.1
Release:        1%{?dist}
Summary:        Automated collection and reporting of citations for used software/methods/datasets

License:        BSD
URL:            https://pypi.python.org/pypi/duecredit
Source0:        https://pypi.python.org/packages/source/d/duecredit/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
# Test deps
BuildRequires:  python2-six
BuildRequires:  python2-nose
BuildRequires:  python2-citeproc-py
BuildRequires:  python-mock
BuildRequires:  python2-requests
BuildRequires:  scipy numpy
BuildRequires:  python-scikit-learn
BuildRequires:  python-statsmodels
BuildRequires:  python2-pandas
BuildRequires:  python-matplotlib
Requires:       python2-six
Requires:       python2-citeproc-py
Requires:       python2-requests

%description -n python2-%{modname}
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
# Test deps
BuildRequires:  python3-six
BuildRequires:  python3-nose
BuildRequires:  python3-citeproc-py
BuildRequires:  python3-mock
BuildRequires:  python3-requests
BuildRequires:  python3-scipy python3-numpy
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-statsmodels
BuildRequires:  python3-pandas
BuildRequires:  python3-matplotlib
Requires:       python3-six
Requires:       python3-citeproc-py
Requires:       python3-requests

%description -n python3-%{modname}
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
export LC_ALL=en_US.UTF-8
%py2_build
%py3_build

%install
export LC_ALL=en_US.UTF-8
%py2_install
%py3_install

# Rename binaries
pushd %{buildroot}%{_bindir}
  mv %{modname} python3-%{modname}
  sed -i '1s|^.*$|#!/usr/bin/env %{__python3}|' python3-%{modname}
  for i in %{modname} %{modname}-3 %{modname}-%{python3_version}
  do
    ln -s python3-%{modname} $i
  done

  cp python3-%{modname} python2-%{modname}
  sed -i '1s|^.*$|#!/usr/bin/env %{__python2}|' python2-%{modname}
  for i in %{modname}-2 %{modname}-%{python2_version}
  do
    ln -s python2-%{modname} $i
  done
popd

%check
nosetests-%{python2_version} -v
nosetests-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%{_bindir}/python2-%{modname}
%{_bindir}/%{modname}-2
%{_bindir}/%{modname}-%{python2_version}
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%{_bindir}/%{modname}
%{_bindir}/python3-%{modname}
%{_bindir}/%{modname}-3
%{_bindir}/%{modname}-%{python3_version}
%{python3_sitelib}/%{modname}*

%changelog
* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.4.4.1-1
- Initial package
