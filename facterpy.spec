%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           facterpy
Version:        0.1
Release:        1%{?dist}
Group:          Applications/Systems
Summary:        Python library to provide cached interface to puppet facter.

License:        BSD
URL:            https://github.com/knorby/facterpy
Source0:        https://github.com/knorby/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
#BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-setuptools
Requires(pre):  shadow-utils
Requires:       python
Requires:       PyYAML

%define service_name %{name}d

%description
A python library that supports gathering facter facts (with chaching abilities.)

%prep
%setup -q -n %{name}-%{version}

%build

%pre

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
#######mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
######mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
%post

%preun

%postun

%files
%{python_sitelib}/facter
%{python_sitelib}/%{name}*.egg-info
########%attr(0755,-,-) %{_bindir}/%{name}

%changelog
* Wed Oct 19 2016 Jonathan Kelley <jon@jon-kelley.com> - 0.0.1-1
- First revision of spec.

