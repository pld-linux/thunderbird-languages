# PACKAGE MERGED INTO thunderbird.spec
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
Summary(pl.UTF-8):	Pakiety językowe dla Thunderbirda
Name:		thunderbird-languages
Version:	52.3.0
Release:	1.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	3dca2752cf45ddc03c76e9271e7cd20b
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	2d82a69409d17e0e4c3283873fe9ed1c
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	64a40a45b7303168f54a48a4582d874b
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	e3fa7e387af4be963f1a6a58fc0c0016
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	1d74a7544890e13d4bfd9408000f471e
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	c30ba85d80effddd339ed26caeb050f6
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	3c33d3fbe537ab6a44599e8c073db870
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	48d8aba0e19d804ace61e0831f95aa40
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	51e6142495445880c98bfec670d6f25f
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	39fc06788219dfee6b00b8e46aa71e7f
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source10-md5:	3ce9672d1a70d226ab28e45a9ad2fd30
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source11-md5:	489e21404cfa0448301d19057302077d
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source12-md5:	fc315d705383bb43a701a90a3ccb9dcb
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source13-md5:	8871241c401d58e8add0b173296c7cba
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source14-md5:	6b1d2d9f79fb3df279d76ead69f1edb3
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source15-md5:	79e0b8c8160402a1bb3b024876fb9666
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source16-md5:	15540c686c9b058c7edef053a981a3f2
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source17-md5:	983e6b2ec0969d0f8b26c0cbfbf565a8
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source18-md5:	e99b315bb53767411073bca4d2320763
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source19-md5:	82001a707850d9c2fd5994bb48c2bbd3
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source20-md5:	6ab4cfc3d80a86d22ebfe833baa8a67c
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source21-md5:	0f2d1293106a248bea8ff090cb083920
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source22-md5:	227e304c86e73e65d18e22f90e3f9837
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source23-md5:	7a042308bedaee0dadfe4f7d77a74818
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source24-md5:	893e9e1fdf8f1f75900ff91d157571dc
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source25-md5:	ad78889d69d75b3783ab75cec97d49ea
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source26-md5:	1d9f76630d880a55ba45823731d63400
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source27-md5:	dceacfcfd563657f9592c4b0ce7cc456
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source28-md5:	250a615a4ac9d268554fcb63bf4dcfb7
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source29-md5:	a946a46867ed3522c1ed30dfaaf46576
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source30-md5:	bf5da0a21933720ac1796e44ef719334
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source31-md5:	940a1df1b8d34708d8a5a7bd2a5e007c
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source32-md5:	c525801fe4fa0e112e8cb79d0205c9a4
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/kab.xpi
# Source33-md5:	8530c217499a0e2c398c83a67b74be75
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source34-md5:	b73951c88aec2a58ceb9f1790cf91877
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source35-md5:	4bab507394d69033a87449979656e488
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source36-md5:	d67dbcac7bc7351bf4ed1814bff2ce24
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source37-md5:	ba205ea7cb31aeb67a78547c07a77037
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source38-md5:	924dfd6b1fa9a3eb88765bc4c79f7e7c
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source39-md5:	0d408ef65f1a0ee68d42eda1006b88f8
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source40-md5:	9c8e1cc635af45cf848cf6c80e868f4c
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source41-md5:	8df6b9ad0a6dd594d1a05821e807e19c
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source42-md5:	c3ba5e9af5c05446178c89f573828404
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source43-md5:	5e0264b6e0d4d8239100aa6780962236
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source44-md5:	97f74202c0184ca0e39bf7294e8f39e5
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source45-md5:	50967648b55390914d1481240337e2e0
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source46-md5:	5472c8e5e8624abc3dca3e530a211aba
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source47-md5:	90a9de17c778311029721e3295e58ebc
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source48-md5:	211d2b7ca461b66f0278995fa8ab66eb
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source49-md5:	268544e08eb08e114119421952a7cf5c
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source50-md5:	5b13ef581128b135426630af220ddf41
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source51-md5:	066206cdd99e75aac1e3d618844e196e
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source52-md5:	7cbb542deb1d64f2451528ac833f1553
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source53-md5:	e4323b14a8901593ddead55275d44b76
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source54-md5:	8274260914e2921371accf8f06378898
Source55:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source55-md5:	87f0aa1b105972c972d417a15b0a8382
Source56:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source56-md5:	6091ab332b44eb7a99b7eabb5dcbad03
Source57:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source57-md5:	d3ace5d1dfd5975b05c8b02e8245ed85
URL:		http://www.mozilla.org/projects/thunderbird/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		thunderbirddir		%{_libdir}/thunderbird

%description
Language packs for Thunderbird.

%description -l pl.UTF-8
Pakiety językowe dla Thunderbirda.

%package -n thunderbird-lang-ar
Summary:	Arabic resources for Thunderbird
Summary(pl.UTF-8):	Arabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ar
Obsoletes:	mozilla-thunderbird-lang-ar

%description -n thunderbird-lang-ar
Arabic resources for Thunderbird.

%description -n thunderbird-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ast
Summary:	Asturian resources for Thunderbird
Summary(pl.UTF-8):	Asturskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ast
Obsoletes:	mozilla-thunderbird-lang-ast

%description -n thunderbird-lang-ast
Asturian resources for Thunderbird.

%description -n thunderbird-lang-ast -l pl.UTF-8
Asturskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-be
Summary:	Belarusian resources for Thunderbird
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-be
Obsoletes:	mozilla-thunderbird-lang-be

%description -n thunderbird-lang-be
Belarusian resources for Thunderbird.

%description -n thunderbird-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-bg
Summary:	Bulgarian resources for Thunderbird
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-bg
Obsoletes:	mozilla-thunderbird-lang-bg

%description -n thunderbird-lang-bg
Bulgarian resources for Thunderbird.

%description -n thunderbird-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-bn
Summary:	Bengali (Bangladesh) resources for Thunderbird
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-bn
Obsoletes:	mozilla-thunderbird-lang-bn

%description -n thunderbird-lang-bn
Bengali (Bangladesh) resources for Thunderbird.

%description -n thunderbird-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu).

%package -n thunderbird-lang-br
Summary:	Breton resources for Thunderbird
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-br
Obsoletes:	mozilla-thunderbird-lang-br

%description -n thunderbird-lang-br
Breton resources for Thunderbird.

%description -n thunderbird-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ca
Summary:	Catalan resources for Thunderbird
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ca
Obsoletes:	mozilla-thunderbird-lang-ca

%description -n thunderbird-lang-ca
Catalan resources for Thunderbird.

%description -n thunderbird-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-cs
Summary:	Czech resources for Thunderbird
Summary(pl.UTF-8):	Czeskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-cs
Obsoletes:	mozilla-thunderbird-lang-cs

%description -n thunderbird-lang-cs
Czech resources for Thunderbird.

%description -n thunderbird-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-da
Summary:	Danish resources for Thunderbird
Summary(pl.UTF-8):	Duńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-da
Obsoletes:	mozilla-thunderbird-lang-da

%description -n thunderbird-lang-da
Danish resources for Thunderbird.

%description -n thunderbird-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-de
Summary:	German resources for Thunderbird
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-de
Obsoletes:	mozilla-thunderbird-lang-de

%description -n thunderbird-lang-de
German resources for Thunderbird.

%description -n thunderbird-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-dsb
Summary:	Lower Sorbian resources for Thunderbird
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}

%description -n thunderbird-lang-dsb
Lower Sorbian resources for Thunderbird.

%description -n thunderbird-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-el
Summary:	Greek resources for Thunderbird
Summary(pl.UTF-8):	Greckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-el
Obsoletes:	mozilla-thunderbird-lang-el

%description -n thunderbird-lang-el
Greek resources for Thunderbird.

%description -n thunderbird-lang-el -l pl.UTF-8
Greckie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-en_GB
Summary:	English (British) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-en_GB
Obsoletes:	mozilla-thunderbird-lang-en_GB

%description -n thunderbird-lang-en_GB
English (British) resources for Thunderbird.

%description -n thunderbird-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-en_US
Summary:	English (American) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-en_US
Obsoletes:	mozilla-thunderbird-lang-en_US

%description -n thunderbird-lang-en_US
English (American) resources for Thunderbird.

%description -n thunderbird-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-es_AR
Summary:	Spanish (Andorra) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-es_AR
Obsoletes:	mozilla-thunderbird-lang-es_AR

%description -n thunderbird-lang-es_AR
Spanish (Andorra) resources for Thunderbird.

%description -n thunderbird-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory).

%package -n thunderbird-lang-es
Summary:	Spanish (Spain) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-es
Obsoletes:	mozilla-thunderbird-lang-es

%description -n thunderbird-lang-es
Spanish (Spain) resources for Thunderbird.

%description -n thunderbird-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii).

%package -n thunderbird-lang-et
Summary:	Estonian resources for Thunderbird
Summary(pl.UTF-8):	Estońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-et
Obsoletes:	mozilla-thunderbird-lang-et

%description -n thunderbird-lang-et
Estonian resources for Thunderbird.

%description -n thunderbird-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-eu
Summary:	Basque resources for Thunderbird
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-eu
Obsoletes:	mozilla-thunderbird-lang-eu

%description -n thunderbird-lang-eu
Basque resources for Thunderbird.

%description -n thunderbird-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-fi
Summary:	Finnish resources for Thunderbird
Summary(pl.UTF-8):	Fińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fi
Obsoletes:	mozilla-thunderbird-lang-fi

%description -n thunderbird-lang-fi
Finnish resources for Thunderbird.

%description -n thunderbird-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-fr
Summary:	French resources for Thunderbird
Summary(pl.UTF-8):	Francuskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fr
Obsoletes:	mozilla-thunderbird-lang-fr

%description -n thunderbird-lang-fr
French resources for Thunderbird.

%description -n thunderbird-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-fy
Summary:	Frisian resources for Thunderbird
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-fy
Obsoletes:	mozilla-thunderbird-lang-fy

%description -n thunderbird-lang-fy
Frisian resources for Thunderbird.

%description -n thunderbird-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ga
Summary:	Irish resources for Thunderbird
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ga
Obsoletes:	mozilla-thunderbird-lang-ga

%description -n thunderbird-lang-ga
Irish resources for Thunderbird.

%description -n thunderbird-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-gd
Summary:	Gaelic resources for Thunderbird
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-gd
Obsoletes:	mozilla-thunderbird-lang-gd

%description -n thunderbird-lang-gd
Gaelic resources for Thunderbird.

%description -n thunderbird-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-gl
Summary:	Galician resources for Thunderbird
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-gl
Obsoletes:	mozilla-thunderbird-lang-gl

%description -n thunderbird-lang-gl
Galician resources for Thunderbird.

%description -n thunderbird-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-he
Summary:	Hebrew resources for Thunderbird
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-he
Obsoletes:	mozilla-thunderbird-lang-he

%description -n thunderbird-lang-he
Hebrew resources for Thunderbird.

%description -n thunderbird-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-hr
Summary:	Croatian resources for Thunderbird
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hr
Obsoletes:	mozilla-thunderbird-lang-hr

%description -n thunderbird-lang-hr
Croatian resources for Thunderbird.

%description -n thunderbird-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-hsb
Summary:	Upper Sorbian resources for Thunderbird
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}

%description -n thunderbird-lang-hsb
Upper Sorbian resources for Thunderbird.

%description -n thunderbird-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-hu
Summary:	Hungarian resources for Thunderbird
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hu
Obsoletes:	mozilla-thunderbird-lang-hu

%description -n thunderbird-lang-hu
Hungarian resources for Thunderbird.

%description -n thunderbird-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-hy
Summary:	Armenian resources for Thunderbird
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-hy
Obsoletes:	mozilla-thunderbird-lang-hy

%description -n thunderbird-lang-hy
Armenian resources for Thunderbird.

%description -n thunderbird-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-id
Summary:	Indonesian resources for Thunderbird
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-id
Obsoletes:	mozilla-thunderbird-lang-id

%description -n thunderbird-lang-id
Indonesian resources for Thunderbird.

%description -n thunderbird-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-is
Summary:	Icelandic resources for Thunderbird
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-is
Obsoletes:	mozilla-thunderbird-lang-is

%description -n thunderbird-lang-is
Icelandic resources for Thunderbird.

%description -n thunderbird-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-it
Summary:	Italian resources for Thunderbird
Summary(pl.UTF-8):	Włoskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-it
Obsoletes:	mozilla-thunderbird-lang-it

%description -n thunderbird-lang-it
Italian resources for Thunderbird.

%description -n thunderbird-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ja
Summary:	Japanese resources for Thunderbird
Summary(pl.UTF-8):	Japońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ja
Obsoletes:	mozilla-thunderbird-lang-ja

%description -n thunderbird-lang-ja
Japanese resources for Thunderbird.

%description -n thunderbird-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-kab
Summary:	Kabyle resources for Thunderbird
Summary(pl.UTF-8):	Kabylskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}

%description -n thunderbird-lang-kab
Kabyle resources for Thunderbird.

%description -n thunderbird-lang-kab -l pl.UTF-8
Kabylskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ko
Summary:	Korean resources for Thunderbird
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ko
Obsoletes:	mozilla-thunderbird-lang-ko

%description -n thunderbird-lang-ko
Korean resources for Thunderbird.

%description -n thunderbird-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-lt
Summary:	Lithuanian resources for Thunderbird
Summary(pl.UTF-8):	Litewskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-lt
Obsoletes:	mozilla-thunderbird-lang-lt

%description -n thunderbird-lang-lt
Lithuanian resources for Thunderbird.

%description -n thunderbird-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-nb
Summary:	Norwegian Bokmaal resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nb
Obsoletes:	mozilla-thunderbird-lang-nb

%description -n thunderbird-lang-nb
Norwegian Bokmaal resources for Thunderbird.

%description -n thunderbird-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-nl
Summary:	Dutch resources for Thunderbird
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nl
Obsoletes:	mozilla-thunderbird-lang-nl

%description -n thunderbird-lang-nl
Dutch resources for Thunderbird.

%description -n thunderbird-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-nn
Summary:	Norwegian Nynorsk resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-nn
Obsoletes:	mozilla-thunderbird-lang-nn

%description -n thunderbird-lang-nn
Norwegian Nynorsk resources for Thunderbird.

%description -n thunderbird-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-pa
Summary:	Panjabi resources for Thunderbird
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pa
Obsoletes:	mozilla-thunderbird-lang-pa

%description -n thunderbird-lang-pa
Panjabi resources for Thunderbird.

%description -n thunderbird-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-pl
Summary:	Polish resources for Thunderbird
Summary(pl.UTF-8):	Polskie pliki językowe dla Thunderbirda
Group:		I18n
URL:		http://www.thunderbird.pl/
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pl
Obsoletes:	mozilla-thunderbird-lang-pl

%description -n thunderbird-lang-pl
Polish resources for Thunderbird.

%description -n thunderbird-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pt_BR
Obsoletes:	mozilla-thunderbird-lang-pt_BR

%description -n thunderbird-lang-pt_BR
Portuguese (Brazil) resources for Thunderbird.

%description -n thunderbird-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-pt
Summary:	Portuguese (Portugal) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-pt
Obsoletes:	mozilla-thunderbird-lang-pt

%description -n thunderbird-lang-pt
Portuguese (Portugal) resources for Thunderbird.

%description -n thunderbird-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii).

%package -n thunderbird-lang-rm
Summary:	Romansh resources for Thunderbird
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-rm
Obsoletes:	mozilla-thunderbird-lang-rm

%description -n thunderbird-lang-rm
Romansh resources for Thunderbird.

%description -n thunderbird-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ro
Summary:	Romanian resources for Thunderbird
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ro
Obsoletes:	mozilla-thunderbird-lang-ro

%description -n thunderbird-lang-ro
Romanian resources for Thunderbird.

%description -n thunderbird-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ru
Summary:	Russian resources for Thunderbird
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ru
Obsoletes:	mozilla-thunderbird-lang-ru

%description -n thunderbird-lang-ru
Russian resources for Thunderbird.

%description -n thunderbird-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-si
Summary:	Sinhala resources for Thunderbird
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-si
Obsoletes:	mozilla-thunderbird-lang-si

%description -n thunderbird-lang-si
Sinhala resources for Thunderbird.

%description -n thunderbird-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-sk
Summary:	Slovak resources for Thunderbird
Summary(pl.UTF-8):	Słowackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sk
Obsoletes:	mozilla-thunderbird-lang-sk

%description -n thunderbird-lang-sk
Slovak resources for Thunderbird.

%description -n thunderbird-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-sl
Summary:	Slovene resources for Thunderbird
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sl
Obsoletes:	mozilla-thunderbird-lang-sl

%description -n thunderbird-lang-sl
Slovene resources for Thunderbird.

%description -n thunderbird-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-sq
Summary:	Albanian resources for Thunderbird
Summary(pl.UTF-8):	Albańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sq
Obsoletes:	mozilla-thunderbird-lang-sq

%description -n thunderbird-lang-sq
Albanian resources for Thunderbird.

%description -n thunderbird-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-sr
Summary:	Serbian resources for Thunderbird
Summary(pl.UTF-8):	Serbskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sr
Obsoletes:	mozilla-thunderbird-lang-sr

%description -n thunderbird-lang-sr
Serbian resources for Thunderbird.

%description -n thunderbird-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-sv
Summary:	Swedish resources for Thunderbird
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-sv
Obsoletes:	mozilla-thunderbird-lang-sv

%description -n thunderbird-lang-sv
Swedish resources for Thunderbird.

%description -n thunderbird-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Thunderbird
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki)
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-ta_LK
Obsoletes:	mozilla-thunderbird-lang-ta_LK

%description -n thunderbird-lang-ta_LK
Tamil (Sri Lanka) resources for Thunderbird.

%description -n thunderbird-lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki).

%package -n thunderbird-lang-tr
Summary:	Turkish resources for Thunderbird
Summary(pl.UTF-8):	Tureckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-tr
Obsoletes:	mozilla-thunderbird-lang-tr

%description -n thunderbird-lang-tr
Turkish resources for Thunderbird.

%description -n thunderbird-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-uk
Summary:	Ukrainian resources for Thunderbird
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-uk
Obsoletes:	mozilla-thunderbird-lang-uk

%description -n thunderbird-lang-uk
Ukrainian resources for Thunderbird.

%description -n thunderbird-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-vi
Summary:	Vietnamese resources for Thunderbird
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-vi
Obsoletes:	mozilla-thunderbird-lang-vi

%description -n thunderbird-lang-vi
Vietnamese resources for Thunderbird.

%description -n thunderbird-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-zh_CN
Summary:	Simplified Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-zh_CN
Obsoletes:	mozilla-thunderbird-lang-zh_CN

%description -n thunderbird-lang-zh_CN
Simplified Chinese resources for Thunderbird.

%description -n thunderbird-lang-zh_CN -l pl.UTF-8
Chińskie (uproszczone) pliki językowe dla Thunderbirda.

%package -n thunderbird-lang-zh_TW
Summary:	Traditional Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Thunderbirda
Group:		I18n
Requires:	thunderbird >= %{version}
Provides:	thunderbird-lang-resources = %{version}
Obsoletes:	icedove-lang-zh_TW
Obsoletes:	mozilla-thunderbird-lang-zh_TW

%description -n thunderbird-lang-zh_TW
Traditional Chinese resources for Thunderbird.

%description -n thunderbird-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Thunderbirda.

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
%setup -qcT %(seq -f '-a %g' 0 57 | xargs)

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

%files -n thunderbird-lang-dsb
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-dsb@thunderbird.mozilla.org.xpi

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

%files -n thunderbird-lang-hsb
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hsb@thunderbird.mozilla.org.xpi

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

%files -n thunderbird-lang-kab
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-kab@thunderbird.mozilla.org.xpi

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
