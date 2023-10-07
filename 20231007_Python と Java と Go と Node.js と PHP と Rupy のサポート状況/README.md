# Python と Java と Go と Node.js と PHP と Rupy のサポート状況について (2023.10)

オープンソース系のプログラム言語のサポート状況をまとめました。他の方の参考になれば幸いです。

# Python の各バージョンのサポート状況

サポートが有効な Python のバージョンは **Python 3.8, 3.9, 3.10, 3.11** です。
3.8 は1年以内にサポート終了の予定です。

|バージョン系列|最新バージョン|リリース日|バグ修正の対応期間|セキュリティ修正の対応期間|
|---|---|---|---|---|
|**Python 3.11**|3.11.5|[2022年10月24日](https://peps.python.org/pep-0664/#schedule)|[**2024年4月1日**](https://peps.python.org/pep-0664/#bugfix-releases)|[**2027年10月**](https://peps.python.org/pep-0664/#lifespan)|
|**Python 3.10**|3.10.13|[2021年10月4日](https://peps.python.org/pep-0619/#schedule)|[2023年4月5日](https://peps.python.org/pep-0619/#bugfix-releases)|[**2026年10月**](https://peps.python.org/pep-0619/#source-only-security-fix-releases)|
|**Python 3.9**|3.9.18|[2020年10月5日](https://peps.python.org/pep-0596/#schedule)|[2022年5月17日](https://peps.python.org/pep-0596/#bugfix-releases)|[**2025年10月**](https://peps.python.org/pep-0596/#lifespan)|
|**Python 3.8**|3.8.18|[2019年10月14日](https://peps.python.org/pep-0569/#schedule)|[2021年5月3日](https://peps.python.org/pep-0569/#bugfix-releases)|[**2024年10月**](https://peps.python.org/pep-0569/#source-only-security-fix-releases)|
|Python 3.7|3.7.17|[2018年6月27日](https://peps.python.org/pep-0537/#schedule)|[2020年6月27日](https://peps.python.org/pep-0537/#schedule-last-bugfix-release)|[2023年6月6日](https://peps.python.org/pep-0537/#schedule-last-security-only-release)|
|Python 2.7|2.7.18|[2010年7月7日](https://peps.python.org/pep-0373/#release-schedule)|[2020年1月1日](https://peps.python.org/pep-0373/#maintenance-releases)|[2020年1月1日](https://peps.python.org/pep-0373/#maintenance-releases)|

# Java のサポート状況

Oracle がサポートしている Java のバージョンは Version 8, 11, 17, 21 です。
その中で[商用利用が無料のバージョンは **Version 17, 21**](https://www.itmedia.co.jp/news/articles/2109/15/news147.html) です。

|リリース|利用開始（GA）日|Premier Support期限|Extended Support期限|
|---|---|---|---|
|[**21**](https://www.oracle.com/jp/java/technologies/downloads/)|2023年9月|2028年9月|[**2031年9月**](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|
|20|2023年3月|[2023年9月](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|設定なし|
|19|2022年9月|[2023年3月](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|設定なし|
|18|2022年3月|[2022年9月](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|設定なし|
|[**17**](https://www.oracle.com/jp/java/technologies/downloads/)|2021年9月|2026年9月|[**2029年9月**](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|
|12 - 16 (非LTS)|2019年3月- 2021年3月|[2019年9月~2021年9月](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|設定なし|
|**11**|2018年9月|2023年9月|[**2032年1月**](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|
|9 - 10|2017年9月- 2018年3月|[2018年3月- 2018年9月](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|設定なし|
|**8**|2014年3月|2022年3月|[**2030年12月**](https://www.oracle.com/jp/java/technologies/java-se-support-roadmap.html)|

# Go(Golang) のサポート状況

Google App Engine でサポートされている Go(Golang) のバージョンは **1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.18, 1.19, 1.20, 1.21** です。1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.18 は1年以内にサポート終了の予定です。

|バージョン|リリース日|Google App Engine のサポート|
|---|---|---|
|**1.21**|[2023年8月8日](https://go.dev/doc/devel/release#go1.21.0)|[**サポート内**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.20**|[2023年2月1日](https://go.dev/doc/devel/release#go1.20.0)|[**サポート内**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.19**|[2022年8月2日](https://go.dev/doc/devel/release#go1.19.0)|[**2025年8月31日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.18**|[2022年3月15日](https://go.dev/doc/devel/release#go1.18.0)|[**2024年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.17**|[2021年8月16日](https://go.dev/doc/devel/release#go1.17.0)|[**2024年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.16**|[2021年2月16日](https://go.dev/doc/devel/release#go1.16.0)|[**2024年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.15**|[2020年8月11日](https://go.dev/doc/devel/release#go1.15.0)|[**2024年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.14**|[2020年2月25日](https://go.dev/doc/devel/release#go1.14.0)|[**2014年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.13**|[2019年9月03日](https://go.dev/doc/devel/release#go1.13.0)|[**2014年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.12**|[2019年2月25日](https://go.dev/doc/devel/release#go1.12.0)|[**2014年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|
|**1.11**|[2018年8月24日](https://go.dev/doc/devel/release#go1.11.0)|[**2014年1月30日**](https://cloud.google.com/appengine/docs/standard/lifecycle/support-schedule?hl=ja)|

# Node.js のサポート状況

サポートが有効なバージョンは **18.x, 20.x** です。

|リリース番号|リリース日|サポート終了日|
|---|---|---|
|**20.x**|2023年4月18日|[**2026年4月30日**](https://github.com/nodejs/release#release-schedule)|
|19.x|2022年10月18日|[2023年6月1日](https://github.com/nodejs/release#end-of-life-releases)|
|**18.x**|2022年4月19日|[**2025年4月30日**](https://github.com/nodejs/release#release-schedule)|
|17.x|2021年10月19日|[2022年6月1日](https://github.com/nodejs/release#end-of-life-releases)|
|16.x|2021年4月20日|[2023年9月11日](https://github.com/nodejs/release#end-of-life-releases)|
|15.x|2020年10月20日|[2021年6月1日](https://github.com/nodejs/release#end-of-life-releases)|
|14.x|2020年4月21日|[2023年4月30日](https://github.com/nodejs/release#end-of-life-releases)|
|13.x|2019年10月22日|[2020年6月1日](https://github.com/nodejs/release#end-of-life-releases)|
|12.x|2019年4月23日|[2022年4月30日](https://github.com/nodejs/release#end-of-life-releases)|
|11.x|2018年10月23日|[2019年6月1日](https://github.com/nodejs/release#end-of-life-releases)|
|10.x|2018年4月24日|[2021年4月30日](https://github.com/nodejs/release#end-of-life-releases)|

# PHP のサポート状況

サポートが有効なバージョンは **8.0, 8.1, 8.2** です。8.0 は1年以内にサポート終了の予定です。

|リリース番号|リリース日|サポート終了日|
|---|---|---|
|**8.2**|2022年12月8日|[**2025年12月8日**](https://www.php.net/supported-versions.php)|
|**8.1**|2021年11月25日|[**2024年11月25日**](https://www.php.net/supported-versions.php)|
|**8.0**|2020年11月28日|[**2023年11月26日**](https://www.php.net/supported-versions.php)|
|7.4|2019年11月28日|2022年11月28日|
|7.3|2018年12月6日|2021年12月6日|
|7.2|2017年11月30日|2020年11月30日|

# Ruby のサポート状況

サポートが有効なバージョンは **3.0, 3.1, 3.2** です。3.0 は1年以内にサポート終了の予定です。

|リリース番号|リリース日|サポート終了日|
|---|---|---|
|**3.2**|2022年12月25日|[**2026年3月31日**](https://www.ruby-lang.org/en/downloads/branches/)|
|**3.1**|2021年12月25日|[**2025年3月31日**](https://www.ruby-lang.org/en/downloads/branches/)|
|**3.0**|2020年12月25日|[**2024年3月31日**](https://www.ruby-lang.org/en/downloads/branches/)|
|2.7|2019年12月25日|[2023年3月31日](https://www.ruby-lang.org/en/downloads/branches/)|
|2.6|2018年12月25日|[2022年4月12日](https://www.ruby-lang.org/en/downloads/branches/)|
|2.5|2017年12月25日|[2021年4月5日](https://www.ruby-lang.org/en/downloads/branches/)|
|2.4|2016年12月25日|[2020年4月5日](https://www.ruby-lang.org/ja/news/2020/04/05/support-of-ruby-2-4-has-ended/)|
|2.3|2015年12月25日|[2019年3月31日](https://www.ruby-lang.org/ja/news/2019/03/31/support-of-ruby-2-3-has-ended/)|
|2.2|2014年12月25日|[2018年6月20日](https://www.ruby-lang.org/en/news/2018/06/20/support-of-ruby-2-2-has-ended/)|
