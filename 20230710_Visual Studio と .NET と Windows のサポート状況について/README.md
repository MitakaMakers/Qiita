# Windows と Visual Studio と .NET のサポート状況について

販売用ソフトウェアについて動作保証する Windows バージョンを明確にするため、Windows と Visual Studio と .NET のマイクロソフトのサポート状況をまとめました。他の方の参考になれば幸いです。

# Windows と Visual Studio と .NET の各バージョンのサポート状況(2023年7月版)

サポートが有効なバージョンは Windows 11, Windows 10, Visual Studio 2022-2013, NET Framework 4.7 以降, NET Framework 3.5, .NET6.0, .NET 7.0 です。
||リリース日|メインストリームサポートの終了日|延長サポートの終了日|
|---|---|---|---|
|Windows 11|2021年11月4日|未定|未定|
|Windows 10|2015年7月29日|2025年10月14日|2025年10月14日|
|Windows 8.1|2012年10月30日|2018年1月9日|2023年1月10日|
|Windows 7|2009年10月22日|2015年1月13日|2020年1月14日|
|Windows Vista|	2007年1月25日|2012年4月10日|2017年4月11日|
|Windows XP|2001年12月31日|2009年4月14日|2014年4月8日|
|Windows 2000|2000年3月31日|2005年6月30日|2010年7月13日|
|Visual Studio 2022|2021年11月8日|2027年1月12日|2032年1月13日|
|Visual Studio 2019|2019年4月2日|2024年4月9日|2029年4月10日|
|Visual Studio 2017|2017年3月7日|2022年4月12日|2027年4月13日|
|Visual Studio 2015|2015年7月20日|2020年10月13日|2025年10月14日|
|Visual Studio 2013|2014年1月15日|2019年4月9日|2024年4月9日|
|Visual Studio 2012|2012年10月31日|2018年1月9日|2023年1月10日|
|Visual Studio 2010|2010年6月29日|2015年7月14日|2020年7月14日|
|Visual Studio 2008|2008年2月19日|2013年4月9日|2018年4月10日|
|Visual Studio 2005|2006年1月27日|2011年4月12日|2016年4月12日|
|Visual Studio 2003|2003年7月10日|2008年10月14日|2013年10月8日|
|Visual Studio 2002|2002年4月15日|2007年7月10日|2009年7月14日|
|Visual Basic 6.0|1998年9月5日|2005年3月31日|2008年4月8日|
|Visual C++ 6.0|1998年9月25日|2004年9月30日|2005年9月30日|
|.NET 7|2022年11月8日|-|未定||
|.NET 6.0 (LTS)|2021年11月9日|-|2024年11月12日|
|.NET 5.0|2020年11月10日|-|2022年5月10日|
|.NET Core 3.1 (LTS)|2019年12月3日|-|2022年12月13日|
|.NET Core 3.0|2019年9月23日|-|2020年3月3日|
|.NET Core 2.2|2018年12月4日|-|2019年12月23日|
|.NET Core 2.1(LTS)|2018年5月30日|-|2021年8月21日|
|.NET Core 2.0|2017年8月14日|-|2018年10月1日|
|.NET Core 1.1|2016年11月16日|-|2019年6月27日|
|.NET Core 1.0|2016年6月27日|-|2019年6月27日|
|.NET Framework 4.8.1|2022年8月9日|-|未定|
|.NET Framework 4.8|2019年4月18日|-|未定|
|.NET Framework 4.7.2|2018年4月30日|-|未定|
|.NET Framework 4.7.1|2017年10月17日|-|未定|
|.NET Framework 4.7|2017年4月11日|-|未定|
|.NET Framework 4.6.2|2016年8月2日|-|2027年1月12日|
|.NET Framework 4.6.1|2015年11月30日|-|2022年4月26日|
|.NET Framework 4.6|2015年7月29日|-|2022年4月26日|
|.NET Framework 4.5.2|2014年5月5日|-|2022年4月26日|
|.NET Framework 4.5.1|2014年1月15日|-|2016年1月12日|
|.NET Framework 4.5|2012年10月9日|-|2016年1月12日|
|.NET Framework 4.0|2010年4月12日|-|2016年1月12日|
|.NET Framework 3.5 Service Pack 1|2007年11月19日|-|2029年1月9日|
|.NET Framework 3.0|2006年11月21日|-|2011年7月12日|
|.NET Framework 2.0|2006年2月17日|-|2011年7月12日|

特徴的なバージョンを以下に挙げます。
+ Windows 11：32 ビット版が廃止された最初のバージョン
+ Windows 7：SHA-256 デジタル署名に対応している一番古いバージョン
+ Visual Studio 2017：Windows XP 用のコード作成をサポートする最後のバージョン
+ Visual Studio 2005：Unicode 対応 した最初のバージョン
+ Visual Studio 2003：Java 訴訟の和解条件により廃止
+ Visual Studio 2002：Java 訴訟の和解条件により廃止

# Visual Studio が対応する OS バージョンの表(2023年7月版)

以下の表の内 Yes は発売パッケージに明記されているバージョン。 カッコ付きの Yes  は 「それ以降のオペレーティングシステム」に該当しマイクロソフトのホームページに記載されているバージョン。

||Win11|Win10|Win8|Win7|Vista|XP|2000|98|
|---|---|---|---|---|---|---|---|---|
|Visual Studio 2022 開発環境|Yes|Yes|-|-|-|-|-|-|
|Visual Studio 2019 開発環境|Yes|Yes|Yes|Yes|-|-|-|-|
|Visual Studio 2017 開発環境|-|Yes|Yes|Yes|-|-|-|-|
|Visual Studio 2015 開発環境|-|Yes|Yes|Yes|-|-|-|-|
|Visual Studio 2013 開発環境|-|-|Yes|Yes|-|-|-|-|
|Visual Studio 2012 開発環境|-|-|Yes|Yes|-|-|-|-|
|Visual Studio 2010 開発環境|-|-|(Yes)|Yes|Yes|Yes|-|-|
|Visual Studio 2008 開発環境|-|-|(Yes)|(Yes)|(Yes)|Yes|Yes|-|
|Visual Studio 2005 開発環境|-|-|-|(Yes)|(Yes)|Yes|Yes|-|
|Visual Studio 2003 開発環境|-|-|-|-|-|Yes|Yes|-|
|Visual Studio 2002 開発環境|-|-|-|-|-|Yes|Yes|-|
|Visual Basic 6.0 開発環境|-|-|-|-|-|(Yes)|(Yes)|Yes|
|Visual Studio 97 開発環境|-|-|-|-|-|-|-|Yes|
|Visual C++ 2022 再頒布パッケージ|Yes|Yes|Yes|Yes|Yes|-|-|-|
|Visual C++ 2019 再頒布パッケージ|Yes|Yes|Yes|Yes|Yes|(Yes)|-|-|
|Visual C++ 2017 再頒布パッケージ|Yes|Yes|Yes|Yes|Yes|Yes|-|-|
|Visual C++ 2015 再頒布パッケージ|(Yes)|Yes|Yes|Yes|Yes|Yes|-|-|
|Visual C++ 2013 再頒布パッケージ|-|-|Yes|Yes|Yes|Yes|-|-|
|Visual C++ 2012 再頒布パッケージ|-|-|Yes|Yes|Yes|Yes|-|-|
|Visual C++ 2010 再頒布パッケージ|-|-|-|Yes|Yes|Yes|-|-|
|Visual C++ 2008 再頒布パッケージ|-|-|-|Yes|Yes|Yes|-|-|
|Visual C++ 2005 再頒布パッケージ|-|-|-|Yes|Yes|Yes|-|-|
|Visual Basic 6.0ランタイム|Yes|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|.NET 7|Yes|Yes|-|-|-|-|-|-|
|.NET 6.0 (LTS)|Yes|Yes|Yes|Yes|-|-|-|-|
|.NET 5.0|Yes|Yes|Yes|Yes|-|-|-|-|
|.NET Core 3.1 (LTS)|Yes|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.8.1|Yes|Yes|-|-|-|-|-|-|
|.NET Framework 4.8|Yes|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.7.2|-|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.7.1|-|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.7|-|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.6.2|-|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.6.1|-|Yes|Yes|Yes|-|-|-|-|
|.NET Framework 4.6|-|Yes|Yes|Yes|Yes|-|-|-|
|.NET Framework 4.5.2|-|-|Yes|Yes|Yes|-|-|-|
|.NET Framework 4.5.1|-|-|Yes|Yes|Yes|-|-|-|
|.NET Framework 4.5|-|-|Yes|Yes|Yes|-|-|-|
|.NET Framework 4.0|-|-|-|Yes|Yes|Yes|-|-|
|.NET Framework 3.5|(Yes)|(Yes)|(Yes)|(Yes)|Yes|Yes|-|-|
