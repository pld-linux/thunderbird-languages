# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=31.4.0
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Thunderbird
Summary(pl.UTF-8):	Pakiety językowe dla Thunderbird
Name:		thunderbird-languages
Version:	52.0.1
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	3fcf847660fce0b4a8aaa79b67d87667
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	200c9741f022064e9a4b297114ca246d
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	b96a8466a691fd3b83bb0f5482142e02
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	47b346dbd89452b62813a81f603ad0cb
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	24a9c11f6d7081327abfa46696bc91bd
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	45de102801322375a2fdec6221bca893
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	75f3181f6b7563aa84725b2e39f2b21b
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	6934b41f57766ebce2e235233df8b295
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	543f79945b1f472517f126546e20ae2b
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	758541a3f76c3aa1580a4adc66807c9a
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	fd903af14b2176d766c67e01525afb4a
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	b83874170e882e21156d958864828408
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	2c9e18dbbdfd0cc3b16adc82ca367efc
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	f88dc4fbafcd9bf8d80d8cc4a3164600
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	5827b7d2199d4094c115c44f2546ccf3
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	8cefba0f6e844b1cdfce61fe8049440b
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	99da94c0fbe03dd0d774a2f34d845e6e
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	9359412dc6611ba55e5faeb5de026494
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	8c70d6ff893e8db974f8c98540ba7849
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	c8ef1e946c61660e1808f6799dfe05fa
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	6e194ab501c8f9d4397edd9ef54499e8
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	71e4f1f48aca56bf50e31cdb0b235f1e
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	16059398bc36f9f165e5788022e13183
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	4c36b5af1ef69dd8720c91013b48f275
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	bb9077900d2ef99735f872eddad38c2b
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	358af7f909f138aa251668ec1bec9829
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	289fa1d6c45d8d9144c5fe6bc2572015
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	aa166b11521266bbb0631bb3e2f11409
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	4a4b2e00021af6d62288736e20b431cb
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	071d3a2a1b2251553981928670070c77
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	d1a53b11edfc3209c9f0c66340f31250
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	a450c633122bd3102639ff1494c5a63f
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	8d98a4175036bce33156aee596386c80
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	824efa26d10fb818f73ded04a351c62d
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	8ac44a959a19c3fe1cf1f8159d0a8582
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	7a404b51693f1cce468ab794f26c5180
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	0216fd03953da44c14eaf0b0b4f6a182
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	bb4c0c87f8e3e6916a5253e946c93d3d
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	bd5bf507053ce4459bbcf49ad1cbb6f9
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	8b4ef0adead28ec821c7621d1161dfba
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	aaa8f5d9cce101c59dffdba920fcf812
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	42128f2f30b7cb2c8f76f97b01558cce
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	dccafa0907e46490dc83cb7486ac58cd
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	ee0e9eaa12371af24b5480f7e5a8456b
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	e1cbcb9c6db56d252b2c9e37b4a3cb71
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	3a9a65cbb4aaa0360a40fef80cb58020
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	03520684a8d55f98593d751557afea4b
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	76adb84f1ecc4b16d6376c401903a6e8
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	297cdcbb6957a0146f9c35d0770bc154
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	bbe3ab2d7e968dc7db9bc50420f85c2f
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	bbdd39bcf327d17af17845db2f779d71
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	58162cb8ba6eb18a25db6d0ff260bf0f
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	33f3d5f944859814cfc38fe5a39ba9b5
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	17af56c07ea5af3497a136ce0f56f88e
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	64ae8759443be99018841cc40c09b9a6
URL:		http://www.mozilla.org/projects/thunderbird/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		thunderbirddir		%{_libdir}/thunderbird

%description
Language packs for Thunderbird.

%description -l pl.UTF-8
Pakiety językowe dla Thunderbird.

%package -n thunderbird-lang-ar
Summary:	Arabic resources for Thunderbird
Summary(pl.UTF-8):	Arabskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ar

%description -n thunderbird-lang-ar
Arabic resources for Thunderbird.

%description -n thunderbird-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ast
Summary:	Asturian resources for Thunderbird
Summary(pl.UTF-8):	Asturskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ast

%description -n thunderbird-lang-ast
Asturian resources for Thunderbird.

%description -n thunderbird-lang-ast -l pl.UTF-8
Asturskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-be
Summary:	Belarusian resources for Thunderbird
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-be

%description -n thunderbird-lang-be
Belarusian resources for Thunderbird.

%description -n thunderbird-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-bg
Summary:	Bulgarian resources for Thunderbird
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-bg

%description -n thunderbird-lang-bg
Bulgarian resources for Thunderbird.

%description -n thunderbird-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-bn
Summary:	Bengali (Bangladesh) resources for Thunderbird
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Thunderbird (wersja dla Bangladeszu)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-bn

%description -n thunderbird-lang-bn
Bengali (Bangladesh) resources for Thunderbird.

%description -n thunderbird-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Thunderbird (wersja dla Bangladeszu).

%package -n thunderbird-lang-br
Summary:	Breton resources for Thunderbird
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-br

%description -n thunderbird-lang-br
Breton resources for Thunderbird.

%description -n thunderbird-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ca
Summary:	Catalan resources for Thunderbird
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ca

%description -n thunderbird-lang-ca
Catalan resources for Thunderbird.

%description -n thunderbird-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-cs
Summary:	Czech resources for Thunderbird
Summary(pl.UTF-8):	Czeskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-cs

%description -n thunderbird-lang-cs
Czech resources for Thunderbird.

%description -n thunderbird-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-da
Summary:	Danish resources for Thunderbird
Summary(pl.UTF-8):	Duńskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-da

%description -n thunderbird-lang-da
Danish resources for Thunderbird.

%description -n thunderbird-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-de
Summary:	German resources for Thunderbird
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-de

%description -n thunderbird-lang-de
German resources for Thunderbird.

%description -n thunderbird-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-el
Summary:	Greek resources for Thunderbird
Summary(pl.UTF-8):	Greckie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-el

%description -n thunderbird-lang-el
Greek resources for Thunderbird.

%description -n thunderbird-lang-el -l pl.UTF-8
Greckie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-en_GB
Summary:	English (British) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-en_GB

%description -n thunderbird-lang-en_GB
English (British) resources for Thunderbird.

%description -n thunderbird-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-en_US
Summary:	English (American) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-en_US

%description -n thunderbird-lang-en_US
English (American) resources for Thunderbird.

%description -n thunderbird-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-es_AR
Summary:	Spanish (Andorra) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbird (wersja dla Andory)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-es_AR

%description -n thunderbird-lang-es_AR
Spanish (Andorra) resources for Thunderbird.

%description -n thunderbird-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbird (wersja dla Andory).

%package -n thunderbird-lang-es
Summary:	Spanish (Spain) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbird (wersja dla Hiszpanii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-es

%description -n thunderbird-lang-es
Spanish (Spain) resources for Thunderbird.

%description -n thunderbird-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbird (wersja dla Hiszpanii).

%package -n thunderbird-lang-et
Summary:	Estonian resources for Thunderbird
Summary(pl.UTF-8):	Estońskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-et

%description -n thunderbird-lang-et
Estonian resources for Thunderbird.

%description -n thunderbird-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-eu
Summary:	Basque resources for Thunderbird
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-eu

%description -n thunderbird-lang-eu
Basque resources for Thunderbird.

%description -n thunderbird-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-fi
Summary:	Finnish resources for Thunderbird
Summary(pl.UTF-8):	Fińskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-fi

%description -n thunderbird-lang-fi
Finnish resources for Thunderbird.

%description -n thunderbird-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-fr
Summary:	French resources for Thunderbird
Summary(pl.UTF-8):	Francuskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-fr

%description -n thunderbird-lang-fr
French resources for Thunderbird.

%description -n thunderbird-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-fy
Summary:	Frisian resources for Thunderbird
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-fy

%description -n thunderbird-lang-fy
Frisian resources for Thunderbird.

%description -n thunderbird-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ga
Summary:	Irish resources for Thunderbird
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ga

%description -n thunderbird-lang-ga
Irish resources for Thunderbird.

%description -n thunderbird-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-gd
Summary:	Gaelic resources for Thunderbird
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-gd

%description -n thunderbird-lang-gd
Gaelic resources for Thunderbird.

%description -n thunderbird-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-gl
Summary:	Galician resources for Thunderbird
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-gl

%description -n thunderbird-lang-gl
Galician resources for Thunderbird.

%description -n thunderbird-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-he
Summary:	Hebrew resources for Thunderbird
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-he

%description -n thunderbird-lang-he
Hebrew resources for Thunderbird.

%description -n thunderbird-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-hr
Summary:	Croatian resources for Thunderbird
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-hr

%description -n thunderbird-lang-hr
Croatian resources for Thunderbird.

%description -n thunderbird-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-hu
Summary:	Hungarian resources for Thunderbird
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-hu

%description -n thunderbird-lang-hu
Hungarian resources for Thunderbird.

%description -n thunderbird-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-hy
Summary:	Armenian resources for Thunderbird
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-hy

%description -n thunderbird-lang-hy
Armenian resources for Thunderbird.

%description -n thunderbird-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-id
Summary:	Indonesian resources for Thunderbird
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-id

%description -n thunderbird-lang-id
Indonesian resources for Thunderbird.

%description -n thunderbird-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-is
Summary:	Icelandic resources for Thunderbird
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-is

%description -n thunderbird-lang-is
Icelandic resources for Thunderbird.

%description -n thunderbird-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-it
Summary:	Italian resources for Thunderbird
Summary(pl.UTF-8):	Włoskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-it

%description -n thunderbird-lang-it
Italian resources for Thunderbird.

%description -n thunderbird-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ja
Summary:	Japanese resources for Thunderbird
Summary(pl.UTF-8):	Japońskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ja

%description -n thunderbird-lang-ja
Japanese resources for Thunderbird.

%description -n thunderbird-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ko
Summary:	Korean resources for Thunderbird
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ko

%description -n thunderbird-lang-ko
Korean resources for Thunderbird.

%description -n thunderbird-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-lt
Summary:	Lithuanian resources for Thunderbird
Summary(pl.UTF-8):	Litewskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-lt

%description -n thunderbird-lang-lt
Lithuanian resources for Thunderbird.

%description -n thunderbird-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-nb
Summary:	Norwegian Bokmaal resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-nb

%description -n thunderbird-lang-nb
Norwegian Bokmaal resources for Thunderbird.

%description -n thunderbird-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-nl
Summary:	Dutch resources for Thunderbird
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-nl

%description -n thunderbird-lang-nl
Dutch resources for Thunderbird.

%description -n thunderbird-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-nn
Summary:	Norwegian Nynorsk resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-nn

%description -n thunderbird-lang-nn
Norwegian Nynorsk resources for Thunderbird.

%description -n thunderbird-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-pa
Summary:	Panjabi resources for Thunderbird
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pa

%description -n thunderbird-lang-pa
Panjabi resources for Thunderbird.

%description -n thunderbird-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-pl
Summary:	Polish resources for Thunderbird
Summary(pl.UTF-8):	Polskie pliki językowe dla Thunderbird
Group:		I18n
URL:		http://www.thunderbird.pl/
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pl

%description -n thunderbird-lang-pl
Polish resources for Thunderbird.

%description -n thunderbird-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pt_BR

%description -n thunderbird-lang-pt_BR
Portuguese (Brazil) resources for Thunderbird.

%description -n thunderbird-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-pt
Summary:	Portuguese (Portugal) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Thunderbird (wersja dla Portugalii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pt

%description -n thunderbird-lang-pt
Portuguese (Portugal) resources for Thunderbird.

%description -n thunderbird-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Thunderbird (wersja dla Portugalii).

%package -n thunderbird-lang-rm
Summary:	Romansh resources for Thunderbird
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-rm

%description -n thunderbird-lang-rm
Romansh resources for Thunderbird.

%description -n thunderbird-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ro
Summary:	Romanian resources for Thunderbird
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ro

%description -n thunderbird-lang-ro
Romanian resources for Thunderbird.

%description -n thunderbird-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ru
Summary:	Russian resources for Thunderbird
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ru

%description -n thunderbird-lang-ru
Russian resources for Thunderbird.

%description -n thunderbird-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-si
Summary:	Sinhala resources for Thunderbird
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-si

%description -n thunderbird-lang-si
Sinhala resources for Thunderbird.

%description -n thunderbird-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-sk
Summary:	Slovak resources for Thunderbird
Summary(pl.UTF-8):	Słowackie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-sk

%description -n thunderbird-lang-sk
Slovak resources for Thunderbird.

%description -n thunderbird-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-sl
Summary:	Slovene resources for Thunderbird
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-sl

%description -n thunderbird-lang-sl
Slovene resources for Thunderbird.

%description -n thunderbird-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-sq
Summary:	Albanian resources for Thunderbird
Summary(pl.UTF-8):	Albańskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-sq

%description -n thunderbird-lang-sq
Albanian resources for Thunderbird.

%description -n thunderbird-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-sr
Summary:	Serbian resources for Thunderbird
Summary(pl.UTF-8):	Serbskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-sr

%description -n thunderbird-lang-sr
Serbian resources for Thunderbird.

%description -n thunderbird-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-sv
Summary:	Swedish resources for Thunderbird
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-sv

%description -n thunderbird-lang-sv
Swedish resources for Thunderbird.

%description -n thunderbird-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Thunderbird
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Thunderbird (wersja dla Sri Lanki)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-ta_LK

%description -n thunderbird-lang-ta_LK
Tamil (Sri Lanka) resources for Thunderbird.

%description -n thunderbird-lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Thunderbird (wersja dla Sri Lanki).

%package -n thunderbird-lang-tr
Summary:	Turkish resources for Thunderbird
Summary(pl.UTF-8):	Tureckie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-tr

%description -n thunderbird-lang-tr
Turkish resources for Thunderbird.

%description -n thunderbird-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-uk
Summary:	Ukrainian resources for Thunderbird
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-uk

%description -n thunderbird-lang-uk
Ukrainian resources for Thunderbird.

%description -n thunderbird-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-vi
Summary:	Vietnamese resources for Thunderbird
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-vi

%description -n thunderbird-lang-vi
Vietnamese resources for Thunderbird.

%description -n thunderbird-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Thunderbird.

%package -n thunderbird-lang-zh_CN
Summary:	Simplified Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-zh_CN

%description -n thunderbird-lang-zh_CN
Simplified Chinese resources for Thunderbird.

%description -n thunderbird-lang-zh_CN -l pl.UTF-8
Chińskie (uproszczone) pliki językowe dla Thunderbird.

%package -n thunderbird-lang-zh_TW
Summary:	Traditional Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Thunderbird
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-zh_TW

%description -n thunderbird-lang-zh_TW
Traditional Chinese resources for Thunderbird.

%description -n thunderbird-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Thunderbird.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang

	fix1=chrome/$lang/locale/$lang/branding/brand.{dtd,properties}
	# rebrand locale for Thunderbird
	cd $lang
	cp -p $file .
	unzip -q $lang.xpi install.rdf $fix1
	sed -i -e 's/Mozilla Thunderbird/Thunderbird/g; s/Thunderbird/Thunderbird/g;' $fix1
	zip -q0 $lang.xpi $fix1
	if ! grep -q "<em:minVersion>%{version}</em:minVersion>" install.rdf; then
		echo "$lang.xpi most likely doesn't work with thunderbird %{version}!" >&2
		exit 1
	fi
	%{__rm} -rf chrome install.rdf
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 54 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{thunderbirddir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{thunderbirddir}/extensions/langpack-$basename@thunderbird.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n thunderbird-lang-ar
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ar@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ast
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ast@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-be
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-be@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-bg
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-bg@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-bn
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-bn-BD@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-br
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-br@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ca
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ca@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-cs
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-cs@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-da
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-da@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-de
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-de@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-el
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-el@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-en_GB
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-en-GB@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-en_US
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-en-US@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-es_AR
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-es-AR@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-es
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-es-ES@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-et
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-et@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-eu
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-eu@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-fi
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fi@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-fr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fr@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-fy
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fy-NL@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ga
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ga-IE@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-gd
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-gd@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-gl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-gl@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-he
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-he@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-hr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hr@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-hu
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hu@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-hy
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hy-AM@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-id
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-id@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-is
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-is@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-it
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-it@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ja
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ja@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ko
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ko@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-lt
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-lt@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-nb
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nb-NO@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-nl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nl@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-nn
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nn-NO@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-pa
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pa-IN@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-pl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pl@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-pt_BR
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pt-BR@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-pt
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pt-PT@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-rm
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-rm@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ro
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ro@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ru
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ru@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-si
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-si@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-sk
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sk@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-sl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sl@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-sq
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sq@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-sr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sr@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-sv
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sv-SE@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-ta_LK
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ta-LK@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-tr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-tr@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-uk
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-uk@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-vi
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-vi@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-zh_CN
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-zh-CN@thunderbird.mozilla.org.xpi

%files -n thunderbird-lang-zh_TW
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-zh-TW@thunderbird.mozilla.org.xpi
