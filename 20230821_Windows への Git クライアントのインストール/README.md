# 3 分でわかるGit for Windows のインストール手順
tag: git for windows tortoisegit 新人エンジニア向け 新人教育

Git はファイルの変更を効率的に管理するための「バージョン管理システム(VCS)」の一種です。Git はソフトウェアのソースファイルや設定ファイルを管理するために役立ちます。

この記事では 18 歳の新人エンジニア向けに「Git for Windows」と「TortoiseGit」をインストールする手順を説明します。

##  Git for Windows と TortoiseGit を使う目的

Git for Windows と TortoiseGit をインストールすると以下のことができるようになります。

### Windows 環境で Git が使える
Git は 元々 Linux システムのために開発されました。Git for Windows をインストールすると、Windows ユーザーも Git の全機能を利用することができます。

![](02_Bash.png)

### グラフィカルなインターフェースが使える
一部のユーザーにとってコマンドラインベースの操作は難しく感じられます。TortoiseGit をインストールすると Git の機能をグラフィカルなインターフェースで直感的に利用できるようになります。

![](03_GUI.png)

### 統合されたシェル拡張が使える
TortoiseGit が Windows Explorer に統合されたシェル拡張を提供します。これにより一目でファイルの状態がわかり、ファイルやディレクトリを右クリックするだけで Git に関する操作を行うことができます。

![](04_Menu.png)

##  Git for Windows と TortoiseGit のシステム要件

Git for windows は以下の環境で動作します。

- オペレーティングシステム: Windows 7 SP1, 8, 8.1, 10, 11
  - アーキテクチャ: 32ビットと64ビットの Windows に対応しています。
- 必要なディスクスペース: インストールには通常 100MB 程度の空き容量が必要です

TortoiseGit は以下の環境で動作します。

- オペレーティングシステム: Windows 7 SP1, 8, 8.1, 10, 11
  - アーキテクチャ: 32ビットと64ビットの Windows に対応しています。

ここでは Windows 11 (64ビット) と Git for windows version 2.41.0.3、TortoiseGit version 2.14.0 を例にして、インストール手順を紹介します。

## Git for Windows のインストール手順

 Git for Windows の公式ページにアクセスしま す。ダウンロードボタンが表示されたら、「Download」をクリックします。

[https://gitforwindows.org/](https://gitforwindows.org/)

![](09_OffifialSite.png)

インストーラをダウンロードしたら、ファイルを実行します。

![](12_installer.png)

ライセンスの承諾画面が表示されたら、「Next」をクリックします。

![](21_installer.png)

インストール先フォルダの確認画面が表示されたら、「Next」をクリックします。

![](22_installer.png)

インストールする機能の選択画面が表示されたら、「Next」をクリックします。
<details><summary>各機能の詳細は以下の通りです。</summary><div>

|No.|初期値|項目|説明|
|---|---|---|---|
|1|  |Additional icons|アイコンを追加する|
|2|  | On the Desktop|デスクトップにアイコンを追加する|
|3|有効|Windows Explorer integration|Windows エクスプローラーと統合する|
|4|有効| Open Git Bash here|コンテキストメニューに「Open Git Bash here」を追加する|
|5|有効| Open Git GUI here|コンテキストメニューに「Open Git GUI here」を追加する|
|6|有効|Git LFS (Large File Support)|Git LFS（ラージファイルサポート）|
|7|有効|Associate .gi* configuration files with the default text editor|.git 設定ファイルをデフォルトのテキストエディタに関連付ける|
|8|有効|Associate .sh files to be run with Bash|Bash で実行する .sh ファイルを関連付ける|
|9|  |Check daily for Git for Windows updates|Windows for Git の更新を自動的にチェックする|
|10|  |Add a Git Bash Profile to Windows Terminal|Windows ターミナルに Git Bash プロファイルを追加する|
|11|  |Scalar (Git add-on to manage large-scale repositories)|Scalar を有効にする|

</div></details>

![](23_installer.png)

スタートメニューのフォルダ名の確認画面が表示されたら、「Next」をクリックします。

![](24_installer.png)

Git コマンドで使うテキストエディタの選択画面が表示されたら、「Next」をクリックします。

![](25_installer.png)

初期ブランチ名の選択画面が表示されたら、「Next」をクリックします。

![](26_installer.png)

PATH 環境変数の選択画面が表示されたら、「Next」をクリックします。

![](27_installer.png)

SSH クライアントの選択画面が表示されたら、「Next」をクリックします。

![](28_installer.png)

HTTPS 転送に使うライブラリの選択画面が表示されたら、「Next」をクリックします。

![](29_installer.png)

改行コードの取り扱いの選択画面が表示されたら「Checkout as-is, commit as-is」を選択し、「Next」をクリックします。

|No.|初期値|項目|説明|
|---|---|---|---|
|1|有効|Checkout Windows-style, commit Unix-style line endings|Windows スタイルのチェックアウト、Unix スタイルの改行コードのコミット|
|2|↓|Checkout as-is, commit Unix-style line endings|そのままチェックアウト、Unix スタイルの改行をコミット|
|3|これを選択|Checkout as-is, commit as-is|そのままチェックアウト、そのままコミット|

![](30_installer.png)

Git Bash で使うソフトウェアの選択画面が表示されたら、「Next」をクリックします。

![](31_installer.png)

git pull コマンドの動作の選択画面が表示されたら、「Next」をクリックします。

![](32_installer.png)

ログイン認証に使うソフトウェアの選択画面が表示されたら、「Next」をクリックします。

![](33_installer.png)

拡張機能の選択画面が表示されたら、「Next」をクリックします。

![](34_installer.png)

実験的な機能の選択画面が表示されたら、「Next」をクリックします。

![](35_installer.png)

インストールの完了画面が表示されたら、「Finish」をクリックします。

![](37_installer.png)

Git for Windows のインストールが完了したら Windows のコマンドプロンプトを開き、「git --version」 と入力し、Gitのバージョンが表示されることを確認します。

![](41_cmd.png)

## TortoiseGit のインストール

TortoiseGit の公式ページにアクセスします。TortoiseGit と Language Pack のインストーラをダウンロードします。あなたの Windows が 32 ビットか 64 ビットかによって、適切なバージョンを選択します。

[https://tortoisegit.org/download/](https://tortoisegit.org/download/)

![](51_officialsite.png)

２つのインストーラをダウンロードしたら、まず TortoiseGit 本体のインストーラを実行します。

![](61_installer.png)

インストーラのセットアップ画面が表示されたら、「Next」をクリックします。

![](71_installer.png)

ライセンスの承諾画面が表示されたら、「Next」をクリックします。

![](72_installer.png)

インストールする機能の選択画面が表示されたら、「Next」をクリックします。

![](73_installer.png)

インストールの最終確認画面が表示されたら、「Install」をクリックします。

![](74_installer.png)

インストールの完了画面が表示されたら、「Finish」をクリックします。

![](75_installer.png)

TortoiseGit の言語選択画面が表示されたら、このまま Language Pack のインストール作業を行います。

![](76_installer.png)

ダウンロードした Language Pack のインストーラを実行します。

![](81_installer.png)

インストーラのセットアップ画面が表示されたら、「次へ」をクリックします。

![](91_installer.png)

インストールの完了画面が表示されたら、「完了」をクリックします。

![](93_installer.png)

TortoiseGit の言語選択画面に戻ります。

「Refresh」ボタンをクリックします。Language リストのプルダウンメニューから「日本語」を選択し、「次へ」をクリックします。

![](101_installer.png)

「TortoiseGit へようこそ」画面が表示されたら、「次へ」をクリックします。

![](102_installer.png)

「Git.exe を設定」画面が表示されたら、「次へ」をクリックします。

![](103_installer.png)

「ユーザー情報を設定」画面が表示されたら、自分の名前とメールアドレスを入力し、「次へ」をクリックします。ここに入力したメールアドレスと名前が Git のログに記録されます。

![](105_installer.png)

「認証/資格情報ストア」画面が表示されたら、「完了」をクリックします。

![](106_installer.png)

これで、Windows 環境に Git for Windows と TortoiseGit がインストールされ、Git を利用できるようになります。

## TortoiseGit の設定

任意のフォルダを右クリックして、コンテキストメニューの「TortoiseGit」→「設定」をクリックします。

![](111_explorer.png)

設定ウィンドウの「全般」→「Windows 11 コンテキストメニュー」でコンテキストメニューに表示する項目を変更できます。

![](121_explorer.png)

設定ウィンドウの「Git」で名前とメールアドレス、改行コードの扱いを変更できます。

![](122_explorer.png)

設定ウィンドウの「ネットワーク」で Git で使うプロキシを設定できます。

![](123_explorer.png)

