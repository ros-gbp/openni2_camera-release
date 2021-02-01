%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-openni2-launch
Version:        1.5.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS openni2_launch package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-catkin_pkg
Requires:       ros-noetic-depth-image-proc
Requires:       ros-noetic-image-proc
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-openni2-camera
Requires:       ros-noetic-rgbd-launch
Requires:       ros-noetic-rospy
Requires:       ros-noetic-roswtf
Requires:       ros-noetic-tf
Requires:       usbutils
BuildRequires:  python3-catkin_pkg
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roslaunch
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Launch files to start the openni2_camera drivers using rgbd_launch.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Feb 01 2021 Isaac I. Y. Saito <isaac.saito@plusonerobotics.com> - 1.5.1-1
- Autogenerated by Bloom

* Mon Feb 01 2021 Isaac I. Y. Saito <isaac.saito@plusonerobotics.com> - 1.5.0-2
- Autogenerated by Bloom

* Tue Jan 12 2021 Isaac I. Y. Saito <isaac.saito@plusonerobotics.com> - 1.5.0-1
- Autogenerated by Bloom

* Wed Jun 03 2020 Isaac I. Y. Saito <isaac.saito@plusonerobotics.com> - 1.4.2-1
- Autogenerated by Bloom

