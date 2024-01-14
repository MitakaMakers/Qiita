# プログラム開発ツール .NET 6 のインストール
tag: .NET 初心者向け 新人教育 新人応援 Windows11　

.NET 6 は無料で使える C# プログラム開発ツールです。.NET 6 は Windows や Linux, macOS で動くソフトウェアを開発するために利用されます。この記事では 18 歳の新入社員向けに .NET 6 のインストール手順を説明します。

## .NET 6 の目的
.NET 6 は以下のような用途で使われます。

### クロスプラットフォーム開発
.NET 6 はWindows、Linux、macOS をサポートしています。１つのソースコードで複数のプラットフォームに対応するアプリケーションを構築できます。

### クラウドアプリケーションの開発
ASP.NET Core を使うと Azure クラウドで動く Web アプリケーションを開発できます。

### .NET アプリケーションの高速化
.NET 6 は多くの最適化が行われ、.Net Framework 4 よりアプリケーションのパフォーマンスが向上しています。

## .NET 6 のシステム要件
.NET 6 の[システム要件](https://github.com/dotnet/core/blob/main/release-notes/6.0/supported-os.md)は、使用する OS によって異なります。Windows OS のシステム要件を以下に示します。

- オペレーティングシステム:　Windows 7 SP1, 8.1, 10 (1607 以降), 11, Windows Server 2012 以降

ここでは .NET 6.0.26 を Windows 11 にインストールする手順を説明します。

## .NET 6 のインストール手順

.NET 6 の公式ページにアクセスします。

[https://dotnet.microsoft.com/ja-jp/download/dotnet/6.0](https://dotnet.microsoft.com/ja-jp/download/dotnet/6.0)

ページが表示されたら、SDK 6.0.x（x はバージョン番号）の Windows OS のインストーラーの「x64」のリンクをクリックします。

![](03_officialsite.png)

インストーラをダウンロードしたら、ファイルをダブルクリックし、インストーラを起動します。

![](11_download.png)

.NET SDK 6 のインストール画面が表示されたら、「インストール」をクリックします。

![](21_install.png)

ユーザーアカウント制御が表示されたら、「はい」をクリックします。

![](22_install.png)

インストール完了画面が表示されたら、「閉じる」をクリックします。

![](24_install.png)

以上で、インストール作業は終了です。