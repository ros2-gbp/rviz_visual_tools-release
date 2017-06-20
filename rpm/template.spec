Name:           ros-kinetic-rviz-visual-tools
Version:        3.4.1
Release:        0%{?dist}
Summary:        ROS rviz_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/rviz_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtx11extras-devel
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-eigen-stl-containers
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-graph-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslint
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-trajectory-msgs
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-eigen-stl-containers
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-graph-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-rviz
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf-conversions
BuildRequires:  ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-visualization-msgs

%description
Utility functions for displaying and debugging data in Rviz via published
markers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jun 20 2017 Dave Coleman <davetcoleman@gmail.com> - 3.4.1-0
- Autogenerated by Bloom

* Wed Nov 02 2016 Dave Coleman <davetcoleman@gmail.com> - 3.4.0-0
- Autogenerated by Bloom

* Wed Sep 28 2016 Dave Coleman <davetcoleman@gmail.com> - 3.3.0-0
- Autogenerated by Bloom

* Thu Jul 14 2016 Dave Coleman <davetcoleman@gmail.com> - 3.2.0-0
- Autogenerated by Bloom

* Wed Jul 06 2016 Dave Coleman <davetcoleman@gmail.com> - 3.1.0-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Dave Coleman <davetcoleman@gmail.com> - 3.0.0-0
- Autogenerated by Bloom

