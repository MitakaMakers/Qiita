Windows デスクトップソフトを開発するにあたり対応する OS バージョンを明確にするため、Windows と Visual Studio、.NET のマイクロソフトのサポート状況をまとめました。他の方の参考になれば幸いです。

## 各ソフトウェアのサポート期限
Windows と VisualStudio、.NET のサポート期限を図示します。期限が明らかでない製品は予想期限を書いてます。

![124_Windows と Visual Studio と .NET のサポート状況.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/b5f4d899-ae22-cd48-f6b5-ce56f229b172.png)

## Windows の各バージョンのサポート状況

サポートが有効なバージョンは **Windows 10, 11** です。

|ソフトウェア名|リリース日|メインストリームサポートの終了日|延長サポートの終了日|
|---|---|---|---|
|[Windows 12?](https://iphone-mania.jp/news-574913/)|[2026年?](https://www.windowscentral.com/software-apps/windows-11/why-windows-12-probably-isnt-happening-this-year)|---|2037年?|
|[**Windows 11**](https://learn.microsoft.com/ja-jp/windows/release-health/windows11-release-information)|2021年11月4日|**サポート内**|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-11-home-and-pro)|
|[**Windows 10**](https://learn.microsoft.com/ja-jp/windows/release-health/status-windows-10-22h2)|2015年7月29日|**2025年10月14日**|[**2025年10月14日**](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-10-home-and-pro)|
|[Windows 8.1](https://support.microsoft.com/ja-jp/windows/windows-8-1-update-kb-2919355-%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B-b189a9bd-0b33-f4a4-2092-4a5be0ebcb61)|2012年10月30日|2018年1月9日|[2023年1月10日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-81)|
|[Windows 7](https://support.microsoft.com/ja-jp/windows/windows-7-service-pack-1-sp1-%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B-b3da2c0f-cdb6-0572-8596-bab972897f61)|2009年10月22日|2015年1月13日|[2020年1月14日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-7)|
|[Windows Vista](https://www.microsoft.com/ja-jp/download/details.aspx?id=51462)|	2007年1月25日|2012年4月10日|[2017年4月11日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-7)|
|[Windows XP](https://www.microsoft.com/ja-JP/download/details.aspx?id=55245)|2001年12月31日|2009年4月14日|[2014年4月8日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-xp)|
|[Windows 2000](https://www.catalog.update.microsoft.com/Search.aspx?q=891861)|2000年3月31日|2005年6月30日|[2010年7月13日](https://www.microsoft.com/ja-jp/windows/lifecycle/default.aspx)|
|Windows ME|2000年9月23日|2006年7月11日|2006年7月11日|
|Windows 98|1998年6月25日|2006年7月11日|2006年7月11日|
|Windows 95|1995年8月24日|2001年12月31日|2001年12月31日|

特徴的なバージョンを以下に挙げます。
+ Windows 7 SP1：[SHA-256 デジタル署名に対応している](https://learn.microsoft.com/ja-jp/security-updates/securityadvisories/2015/3033929?redirectedfrom=MSDN)一番古い Windows
+ Windows XP：MS-DOS の16ビットソフトウェアが動く最後の Windows

## 特殊用途向け Windows 10 の紹介

標準よりサポート期間が長い 特殊用途向け Windows 10 のサポート期限を紹介します。

|ソフトウェア名|リリース日|メインストリームサポートの終了日|延長サポートの終了日|
|---|---|---|---|
|Windows 10 拡張セキュリティ更新プログラム|2025年10月15日|---|2028年10月14日|
|Windows 10 Enterprise LTSC 2019|2018年11月13日|2024年1月9日|[2029年1月9日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-10-enterprise-ltsc-2019)|
|Windows 10 IoT Enterprise LTSC 2021|2021年11月16日|2027年1月12日|[2032年1月13日](https://learn.microsoft.com/ja-jp/lifecycle/products/windows-10-iot-enterprise-ltsc-2021)|

### Windows 10 拡張セキュリティ更新プログラム
拡張セキュリティ更新プログラムは Windows 10　サポート終了後に最長3年間、セキュリティパッチが提供される有償のライセンスです。

- インプレス > Windows 10の組織向け有償延長サポート、導入方法や料金が発表
[https://pc.watch.impress.co.jp/docs/news/1582053.html](https://pc.watch.impress.co.jp/docs/news/1582053.html)

### Windows 10 Enterprise LTSC 2019
Windows 10 LTSC は、インターネットやクラウドに接続できない環境で、デスクトップ環境を必要とする特定用途（医療機器や銀行の ATM など）向けに提供される製品です。
リリースされた時点のハードウエアがサポート対象となります。部品の生産終了や在庫切れが発生すると継続利用ができなくなる可能性があります。

- アイティメディア > 再考、Windows 10 Enterprise LTSC
[https://atmarkit.itmedia.co.jp/ait/articles/1812/05/news039.html](https://atmarkit.itmedia.co.jp/ait/articles/1812/05/news039.html)

### Windows 10 IoT Enterprise LTSC 2021
Windows 10  IoT Enterprise はPOS、工場の生産ラインなど、特定用途の端末向けの組み込み OS です。通常のセキュリティー機能より強固な、組込み端末向けのセキュリティー機能が搭載されています。

- EPSON > Windows 10 IoT Enterprise LTSC（Windows Embedded OS）とは
[https://shop.epson.jp/pc/emb/embqa/](https://shop.epson.jp/pc/emb/embqa/)

## Visual Studio の各バージョンのサポート状況

サポートが有効なバージョンは **Visual Studio 2022, 2019, 2017, 2015** です。

|ソフトウェア名|リリース日|メインストリームサポートの終了日|延長サポートの終了日|
|---|---|---|---|
|**Visual Studio 2022**|2021年11月8日|**2027年1月12日**|[**2032年1月13日**](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2022)|
|**Visual Studio 2019**|2019年4月2日|2024年4月9日|[**2029年4月10日**](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2019)|
|**Visual Studio 2017**|2017年3月7日|2022年4月12日|[**2027年4月13日**](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2017)|
|**Visual Studio 2015**|2015年7月20日|2020年10月13日|[**2025年10月14日**](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2015)|
|Visual Studio 2013|2014年1月15日|2019年4月9日|[2024年4月9日](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2013)|
|Visual Studio 2012|2012年10月31日|2018年1月9日|[2023年1月10日](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2012)|
|Visual Studio 2010|2010年6月29日|2015年7月14日|[2020年7月14日](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2010)|
|Visual Studio 2008|2008年2月19日|2013年4月9日|[2018年4月10日](https://learn.microsoft.com/ja-jp/lifecycle/products/visual-studio-2008)|
|Visual Studio 2005|2006年1月27日|2011年4月12日|[2016年4月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-visual-studio-2005)|
|Visual Studio 2003|2003年7月10日|2008年10月14日|[2013年10月8日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-visual-studio-net-2003)|
|Visual Studio 2002|2002年4月15日|2007年7月10日|2009年7月14日|
|Visual Basic 6.0|1998年9月5日|2005年3月31日|[2008年4月8日](https://learn.microsoft.com/ja-jp/lifecycle/faq/developer-tools#microsoft-visual-basic)|
|Visual C++ 6.0|1998年9月25日|2004年9月30日|2005年9月30日|

特徴的なバージョンを以下に挙げます。
+ Visual Studio 2017：Windows XP 用のコード作成をサポートする最後の C++ 環境
+ Visual Studio 2003：[Visual J++ 訴訟の和解条件により廃止](https://ja.wikipedia.org/wiki/Microsoft_Visual_J%2B%2B#)
+ Visual Studio 2002：[Visual J++ 訴訟の和解条件により廃止](https://ja.wikipedia.org/wiki/Microsoft_Visual_J%2B%2B#)
+ Visual Studio 6.0：[Visual J++ 訴訟の和解条件により廃止](https://ja.wikipedia.org/wiki/Microsoft_Visual_J%2B%2B#)

## .NET の各バージョンのサポート状況

サポートが有効なバージョンは **.NET 3.5, 4.6.2, 4.7, 4.8, 6.0, 7.0, 8.0** です。6.0, 7.0 は１年以内にサポート終了の予定です。

|ソフトウェア名|リリース日|サポートの終了日|
|---|---|---|
|[.NET 10](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core#cadence)|2025年11月?|2028年11月?|
|[.NET 9](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core#cadence)|2024年11月?|2026年5月?|
|[**.NET 8.0**](https://dotnet.microsoft.com/ja-jp/download/dotnet/8.0)|[2023年11月14日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-and-net-core)|[**2026年11月10日**](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core)|
|[**.NET 7.0**](https://dotnet.microsoft.com/ja-jp/download/dotnet/7.0)|[2022年11月8日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-and-net-core)|[**2024年5月14日**](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core)|
|[**.NET 6.0**](https://dotnet.microsoft.com/ja-jp/download/dotnet/6.0)|[2021年11月9日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-and-net-core)|[**2024年11月12日**](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core)|
|[.NET Core 3.1](https://dotnet.microsoft.com/ja-jp/download/dotnet/3.1)|[2019年12月3日](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core)|[2022年12月13日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-and-net-core)|
|[.NET Core 2.1](https://dotnet.microsoft.com/ja-jp/download/dotnet/2.1)|[2018年5月30日](https://dotnet.microsoft.com/ja-jp/platform/support/policy/dotnet-core)|[2021年8月21日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-and-net-core)|
|[**.NET Framework 4.8.1**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net481)|2022年8月9日|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 4.8**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net48)|2019年4月18日|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 4.7.2**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net472)|2018年4月30日|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 4.7.1**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net471)|2017年10月17日|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 4.7**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net47)|2017年4月11日|[**サポート内**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 4.6.2**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net462)|2016年8月2日|[**2027年1月12日**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.6.1](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net461)|2015年11月30日|[2022年4月26日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.6](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net46)|2015年7月29日|[2022年4月26日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.5.2](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net452)|2014年5月5日|[2022年4月26日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.5.1](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net451)|2014年1月15日|[2016年1月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.5](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net45)|2012年10月9日|[2016年1月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 4.0](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net40)|2010年4月12日|[2016年1月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[**.NET Framework 3.5**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net35-sp1)|2007年11月19日|[**2029年1月9日**](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 3.0](https://www.microsoft.com/ja-jp/download/details.aspx?id=3005)|2006年11月21日|[2011年7月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|
|[.NET Framework 2.0](https://www.microsoft.com/ja-jp/download/details.aspx?id=16614)|2006年2月17日|[2011年7月12日](https://learn.microsoft.com/ja-jp/lifecycle/products/microsoft-net-framework)|

## .NET の実行環境が動く Windows バージョン

.NET プログラムを動かすためのランタイムライブラリが対応する Windows バージョンを以下に示します。

|ソフトウェア名|11|10|8.1|7|Vista|XP|2000|
|---|---|---|---|---|---|---|---|
|[**.NET 8.0**](https://github.com/dotnet/core/blob/main/release-notes/8.0/supported-os.md)|Yes|Yes|-|-|-|-|-|-|
|[**.NET 7.0**](https://dotnet.microsoft.com/ja-jp/download/dotnet/7.0)|Yes|Yes|-|-|-|-|-|-|
|[**.NET 6.0**](https://dotnet.microsoft.com/ja-jp/download/dotnet/6.0)|Yes|Yes|Yes|Yes|-|-|-|
|[.NET Core 3.1](https://dotnet.microsoft.com/ja-jp/download/dotnet/3.1)|Yes|Yes|Yes|Yes|-|-|-|
|[**.NET Framework 4.8.1**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net481)|[**22H2**](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-481)|[**22H2**](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-481)|-|-|-|-|-|
|[**.NET Framework 4.8**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net48)|[**21H2**](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-48)|[**21H2**<br>1903](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-48)|Yes|Yes|-|-|-|
|[**.NET Framework 4.7.2**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net472)|-|[1803](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-472)|Yes|Yes|-|-|-|
|[**.NET Framework 4.7.1**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net471)|-|[1709](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-471)|Yes|Yes|-|-|-|
|[**.NET Framework 4.7**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net47)|-|[1703](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-47)|Yes|Yes|-|-|-|
|[**.NET Framework 4.6.2**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net462)|-|[1607](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-462)|Yes|Yes|-|-|-|
|[.NET Framework 4.6.1](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net461)|-|[1511](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-461)|Yes|Yes|-|-|-|
|[.NET Framework 4.6](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net46)|-|[1507](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-46)|Yes|Yes|Yes|-|-|
|[.NET Framework 4.5.2](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net452)|-|-|Yes|Yes|Yes|-|-|
|[.NET Framework 4.5.1](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net451)|-|-|[8.1](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-451)|Yes|Yes|-|-|
|[.NET Framework 4.5](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net45)|-|-|[8](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-45)|Yes|Yes|-|-|
|[.NET Framework 4.0](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net40)|-|-|-|Yes|Yes|Yes|-|
|[**.NET Framework 3.5**](https://dotnet.microsoft.com/ja-jp/download/dotnet-framework/net35-sp1)|Opt|Opt|Opt|[7](https://learn.microsoft.com/en-us/dotnet/framework/migration-guide/versions-and-dependencies#net-framework-35)|Yes|Yes|Yes|-|

Yes はランタイムライブラリがインストール可能である事を示します。その他の文字は Windows にデフォルトでインストールされる事を示し、[詳細な OS のバージョン](https://qiita.com/mmake/items/748232d9f31b0a0c842e#windows-10-%E3%81%AE%E5%90%84%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E7%8A%B6%E6%B3%81)を表します。

## Visual Studio 開発環境が動く Windows バージョン

Visual Studio のプログラミング開発環境が対応する Windows バージョンを以下に示します。

|ソフトウェア名|11|10|8.1|7|Vista|XP|2000|98|
|---|---|---|---|---|---|---|---|---|
|[**Visual Studio 2022**](https://learn.microsoft.com/ja-jp/visualstudio/releases/2022/release-notes)|Yes|Yes|-|-|-|-|-|-|
|[**Visual Studio 2019**](https://learn.microsoft.com/ja-jp/visualstudio/releases/2019/release-notes)|Yes|Yes|Yes|Yes|-|-|-|-|
|[**Visual Studio 2017**](https://learn.microsoft.com/ja-jp/visualstudio/releasenotes/vs2017-relnotes)|-|Yes|Yes|Yes|-|-|-|-|
|[**Visual Studio 2015**](https://learn.microsoft.com/ja-jp/visualstudio/releasenotes/vs2015-update3-vs)|-|Yes|Yes|Yes|-|-|-|-|
|[Visual Studio 2013](https://learn.microsoft.com/ja-jp/visualstudio/releasenotes/vs2013-update5-vs)|-|-|Yes|Yes|-|-|-|-|
|[Visual Studio 2012](https://learn.microsoft.com/ja-jp/visualstudio/releasenotes/vs2012-update4-vs)|-|-|Yes|Yes|-|-|-|-|
|[Visual Studio 2010 SP1](https://learn.microsoft.com/ja-jp/visualstudio/releasenotes/vs2010-sp1-vs)|-|-|(Y)|Yes|Yes|Yes|-|-|
|[Visual Studio 2008 SP1](https://www.microsoft.com/ja-jp/download/details.aspx?id=13276)|-|-|(Y)|(Y)|(Y)|Yes|Yes|-|
|[Visual Studio 2005 SP1](https://www.microsoft.com/ja-jp/download/details.aspx?id=42945)||-|-|(Y)|(Y)|Yes|Yes|-|
|[Visual Studio 6.0 SP6](https://www.microsoft.com/ja-jp/download/details.aspx?id=50722)|[(U)](https://qiita.com/mmake/items/3fb4ae920e2efe4b619c)|[(U)](https://qiita.com/mmake/items/3fb4ae920e2efe4b619c)|[(U)](https://qiita.com/mmake/items/3fb4ae920e2efe4b619c)|(U)|(Y)|(Y)|Yes|

Yes はVisual Studio の発売パッケージに明記された OS を示します。カッコ付きの Y はマイクロソフトのホームページに記載されている対応 OS である事を示します。

## C++, VB6 の実行環境が動く Windows バージョン

VC++, VB6 プログラムを動かすためのランタイムライブラリが対応する Windows バージョンを以下に示します。

|ソフトウェア名|11|10|8.1|7|Vista|XP|2000|
|---|---|---|---|---|---|---|---|
|[**Visual C++ 2022<BR> 再頒布可能パッケージ**](https://learn.microsoft.com/ja-JP/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)|Yes|Yes|Yes|Yes|Yes|-|-|
|[**Visual C++ 2019<BR> 再頒布可能パッケージ**](https://learn.microsoft.com/ja-JP/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)|Yes|Yes|Yes|Yes|Yes|[(Yes)](https://learn.microsoft.com/ja-JP/cpp/windows/latest-supported-vc-redist?view=msvc-170#notes)|-|
|[**Visual C++ 2017<BR> 再頒布可能パッケージ**](https://forest.watch.impress.co.jp/library/software/software_11538/)|Yes|Yes|Yes|Yes|Yes|Yes|-|
|[**Visual C++ 2015<BR> 再頒布可能パッケージ**](https://www.microsoft.com/ja-jp/download/details.aspx?id=53840)|Yes|Yes|Yes|Yes|Yes|Yes|-|
|[Visual C++ 2013<BR> 再頒布可能パッケージ](https://www.microsoft.com/ja-jp/download/details.aspx?id=40784)|-|-|Yes|Yes|Yes|Yes|-|
|[Visual C++ 2012<BR> 再頒布可能パッケージ](https://www.microsoft.com/ja-jp/download/details.aspx?id=30679)|-|-|Yes|Yes|Yes|Yes|-|
|[Visual C++ 2010<BR> 再頒布可能パッケージ](https://www.microsoft.com/ja-jp/download/details.aspx?id=26999)|-|-|-|Yes|Yes|Yes|-|
|[Visual C++ 2008<BR> 再頒布可能パッケージ](https://www.microsoft.com/ja-jp/download/details.aspx?id=26368)|-|-|-|Yes|Yes|Yes|-|
|[Visual C++ 2005<BR> 再頒布可能パッケージ](https://www.microsoft.com/ja-jp/download/details.aspx?id=26347)|-|-|-|Yes|Yes|Yes|-|
|[**Visual Basic 6.0<BR> ランタイム**](https://learn.microsoft.com/ja-jp/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy)|[RTM](https://learn.microsoft.com/ja-jp/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy#windows-7-sp1-81-10--11)|[RTM](https://learn.microsoft.com/ja-jp/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy#windows-7-sp1-81-10--11)|[RTM](https://learn.microsoft.com/ja-jp/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy#windows-7-sp1-81-10--11)|[RTM](https://learn.microsoft.com/ja-jp/previous-versions/msdn10/cc707268(v=msdn.10))|[RTM](https://learn.microsoft.com/ja-jp/previous-versions/msdn10/cc707268(v=msdn.10))|[RTM](https://www.vector.co.jp/soft/win95/util/se342080.html)|[RTM](https://www.vector.co.jp/soft/win95/util/se342080.html)|

RTM は Windows にデフォルトでインストールされる事を示します。Yes はランタイムライブラリがインストール可能である事を示します。
