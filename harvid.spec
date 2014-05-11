Summary:	HTTP server to extract, cache and serve still images from movie files
Name:		harvid
Version:	0.7.3
Release:	2
Group:		Video
License:	GPLv2+
Url:		http://x42.github.com/harvid/
Source0:	https://github.com/x42/harvid/archive/%{name}-%{version}.tar.gz
BuildRequires:	ffmpeg-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
Requires:	ffmpeg

%description
Harvid is a HTTP server to efficiently extract, cache and serve still images
from movie files. It provides for frame-accurate decoding and is main use-case
is to act as backend and second level cache for rendering the videotimeline in
Ardour. Harvid uses ffmpeg/libav and supports a wide variety of video codecs
and formats.

%prep
%setup -q

%build
%setup_compile_flags
make

%install
%makeinstall_std PREFIX=%{_prefix}

pushd %{buildroot}%{_bindir}
ln -s ffmpeg ffmpeg_harvid
ln -s ffprobe ffprobe_harvid
popd

%files
%doc README.md ChangeLog COPYING
%{_bindir}/%{name}
%{_bindir}/ffmpeg_harvid
%{_bindir}/ffprobe_harvid
%{_mandir}/man1/%{name}.1*
