Name:           ros-indigo-openni2-camera
Version:        0.2.8
Release:        0%{?dist}
Summary:        ROS openni2_camera package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       openni-devel
Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  openni-devel
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
Drivers for the Asus Xtion and Primesense Devices. For using a kinect with ROS,
try the freenect stack

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Aug 17 2017 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.8-0
- Autogenerated by Bloom

* Tue Jun 07 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.7-0
- Autogenerated by Bloom

* Thu May 05 2016 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.6-0
- Autogenerated by Bloom

* Thu Oct 15 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.5-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.4-0
- Autogenerated by Bloom

* Fri Jan 16 2015 Michael Ferguson <developers@unboundedrobotics.com> - 0.2.3-0
- Autogenerated by Bloom

