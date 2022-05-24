%define sonum 1

Name: recastnavigation
Version: 1.5.0
Release: alt1.git.5a870d42
Summary: Navigation-mesh Toolset for Games
License: Zlib
Group: Games/Other
URL: https://github.com/recastnavigation/recastnavigation

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: cmake >= 3.0
BuildRequires: gcc-c++
BuildRequires: libGLU-devel

%description
Recast is state of the art navigation mesh construction toolset for games.
Recast is accompanied with Detour, path-finding and spatial reasoning toolkit.
You can use any navigation mesh with Detour, but of course the data generated
with Recast fits perfectly.

%package -n librecastnavigation-devel
Group: System/Configuration/Hardware
Summary: Library and header files for the recastnavigation library
Requires: libDebugUtils%sonum = %version
Requires: libDetour%sonum = %version
Requires: libDetourCrowd%sonum = %version
Requires: libDetourTileCache%sonum = %version
Requires: libRecast%sonum = %version

%description -n librecastnavigation-devel
Recast is state of the art navigation mesh construction toolset for games.
Recast is accompanied with Detour, path-finding and spatial reasoning toolkit.
You can use any navigation mesh with Detour, but of course the data generated
with Recast fits perfectly.
This package contains the recastnavigation library and its header files.

%package -n libDebugUtils%sonum
Group: Games/Other
Summary: Debug Utils library for recastnavigation

%description -n libDebugUtils%sonum
This package contains the debug utilities library for the recastnavigation.

%package -n libDetour%sonum
Group: Games/Other
Summary: Detour library for recastnatnaviagtion

%description -n libDetour%sonum
This package contains the Detour library of recastnatnaviagtion.

%package -n libDetourCrowd%sonum
Group: Games/Other
Summary: Detour Crowd library for recastnatnaviagtion

%description -n libDetourCrowd%sonum
This package contains the Detour Crowd library of recastnatnaviagtion.

%package -n libDetourTileCache%sonum
Group: Games/Other
Summary: Detour Tile Cache library for recastnatnaviagtion

%description -n libDetourTileCache%sonum
This package contains the detour tile cache library of recastnatnaviagtion.

%package -n libRecast%sonum
Group: Games/Other
Summary: Recast Library for recastnatnaviagtion

%description -n libRecast%sonum
This package contains the recast library of recastnatnaviagtion.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DRECASTNAVIGATION_DEMO=OFF \
    -DRECASTNAVIGATION_EXAMPLES=OFF \
    -DRECASTNAVIGATION_TESTS=OFF \
    -DBUILD_SHARED_LIBS=1
%cmake_build

%install
%cmake_install

%files -n librecastnavigation-devel
%doc License.txt
%doc README.md
%_libdir/libDebugUtils.so
%_libdir/libDetour.so
%_libdir/libDetourCrowd.so
%_libdir/libDetourTileCache.so
%_libdir/libRecast.so
%_includedir/recastnavigation
%_libdir/pkgconfig/recastnavigation.pc

%files -n libDebugUtils%sonum
%_libdir/libDebugUtils.so.*

%files -n libDetour%sonum
%_libdir/libDetour.so.*

%files -n libDetourCrowd%sonum
%_libdir/libDetourCrowd.so.*

%files -n libDetourTileCache%sonum
%_libdir/libDetourTileCache.so.*

%files -n libRecast%sonum
%_libdir/libRecast.so.*

%changelog
* Tue May 24 2022 Alexey Ivakhnenko <vcong@altlinux.org> 1.5.0-alt1.git.5a870d42
- Initial build for Sisyphus.
