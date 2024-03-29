# Hyper-V に Windows 11 仮想マシンをインストールする方法
tag: Hyper-V 初心者向け 新人教育 Windows11

::: note
この記事は [Win 11 への Hyper-V のインストール](https://qiita.com/mmake/items/cd96a0c59226e8460af6) の続きの内容になります。
:::

この記事では 18 歳の新入社員向けに Hyper-V で Windows 11 を実行する方法を説明します。

## 前回のおさらい

[Win 11 への Hyper-V のインストール](https://qiita.com/mmake/items/cd96a0c59226e8460af6) では Hyper-V 機能を有効にする方法を説明しました。

ここでは、Hyper-V 上に Windows 11 90日評価版をインストールする方法を説明します。

## Windows 11 仮想マシンの入手
### Windows 11 評価版のダウンロード
Windows 11 開発環境のダウンロードページにアクセスします。

[https://developer.microsoft.coダウンロードp/windows/downloads/virtual-machines/](https://developer.microsoft.com/ja-jp/windows/downloads/virtual-machines/)、

![](303.png)

### Hyper-V (Gen2) 仮想マシンのダウンロード
ページを下にスクロールし、「**Hyper-V (Gen2)**」をクリックします。仮想マシンのダウンロードが始まります。

![](305.png)

### ファイルの展開
ダウンロードが完了したら、ファイルを右クリックし、「**すべて展開**」をクリックします。

![](313.png)

### 展開先フォルダの指定
ファイルの展開先を指定します。ここでは例として **C:\Users\User\Downloads\WinDev2401Eval.HyperV** というフォルダに展開します。

![](315.png)

### VHDX ファイル
WinDev2401Eval.vhdx ファイルができます。

![](317.png)

## 仮想マシンの作成
### Windows ツールを開く
スタートメニューから 「**すべてのアプリ > Windows ツール**」 をクリックします

![223.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/352dd0e9-833a-d446-1ef4-dac9a00fdac2.png)

### Hyper-V マネージャーの起動
Windows ツールが表示されたら、「**Hyper-V マネージャー**」 をクリックします。

![243.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/a9152c15-2139-dc8d-fff3-a044f3d9ae55.png)

### 新しい仮想マシンの作成
Hyper-V マネージャーが表示されたら、メニューから 「**操作 > クイック作成**」 の順にクリックします

![](351.png)

### インストール元の変更
クイック作成画面が表示されたら、「**ローカルインストール元**」をクリックします。

![](353.png)

### 仮想マシンの選択
「**インストール元の変更**」をクリックします。

![](355.png)

### VHDX ファイルの選択
先ほど展開した vhdx ファイルを選択し、「**開く**」をクリックします。

![](357.png)

### 仮想マシンの作成
ファイル名が表示されたら、「**仮想マシンの作成**」をクリックします。

![](359.png)

### 仮想マシンの作成完了
仮想マシンの作成完了画面が表示されたら、「**接続**」をクリックします。

![](363.png)

### 仮想マシンの起動
接続画面が表示されたら、「**起動**」をクリックします。

![](365.png)

### 仮想マシンへの接続
画面のサイズを選択し、「**接続**」をクリックします。

![](369.png)

### 仮想マシンへのログイン
ログイン画面が表示されたら、「**Sign in**」をクリックします。

![](373.png)

### ログイン完了
デスクトップ画面が表示されたら、接続完了です。

![](401.png)

## 表示言語の変更
### 設定画面を開く
スタートメニューをクリックし、「**Settings**」をクリックします。

![](403.png)

### 設定画面の表示
設定画面が表示されたら、左側の「**Time & language**」をクリックします。

![](405.png)

### 時刻と言語の表示
Time & Language が表示されたら、右側の「**Language & region**」をクリックします。

![](407.png)

### 言語と地域の表示
Language & region が表示されたら、「**Add a language**」をクリックします。

![](409.png)

### 言語の検索
言語の検索画面が表示されたら、「**japanese**」と入力します。
![](413.png)

### 日本語の選択
日本語を選択し、「**Next**」をクリックします。

![](415.png)

### 日本語のインストール
「**Set as my Windows display language**」のチェックをオンにし、「**Install**」をクリックします。

![](419.png)

### 英語の削除
Japanese のインストールが完了したら、**「English (United States)」の ...** をクリックし、「**Remove**」をクリックします。

![](425.png)
### Remove の確認
確認画面が表示されたら、「**Yes**」をクリックします。

![](426.png)

### Sign Out
「**Sign out**」をクリックします。

![](427.png)

### 仮想マシンへのログイン
ログイン画面が表示されたら、「**Sign in**」をクリックします。

![](373.png)

### 日本語への変更完了
デスクトップ画面のライセンス表示が日本語に変われば、設定完了です。

![](428.png)
## 管理用言語の変更
### 設定画面を開く
スタートメニューをクリックし、「**設定**」をクリックします。

![](451.png)
### 設定画面の表示
設定画面が表示されたら、左側の「**時刻と言語**」をクリックします。

![](453.png)
### 時刻と言語の表示
時刻と言語が表示されたら、右側の「**言語と地域**」をクリックします。

![](455.png)
### 管理用の言語の設定
「**管理用の言語の設定**」をクリックします。

![](429.png)
### 設定のコピー
地域の管理画面が表示されたら、「**設定のコピー**」をクリックします。

![](431.png)
### ようこそ画面の設定
ようこそ画面と新しいユーザアカウントの設定画面が表示されたら、「**ようこそ画面とシステムアカウント**」「**新しいユーザーアカウント**」のチェックをオンにし、「**OK**」をクリックします。

![](432.png)
### 再起動の確認
再起動を促す画面が表示されたら、「**後で**」をクリックします。

![](433.png)
### システムロケールの変更
引き続き、「**システムロケールの変更**」をクリックします。

![](431.png)

### 現在のシステムロケールの変更
地域の設定が表示されたら、「**英語（米国）**」クリックします。

![](434.png)

### 日本語を選択
リストが表示されたら、「**日本語**」を選択し、「**OK**」をクリックします。

![](435.png)
### 再起動の確認
再起動を促す画面が表示されたら、「**今すぐ再起動**」をクリックします。

![](439.png)
### 仮想マシンへの再接続
再接続画面が表示されたら、「**再接続**」をクリックします。

![](445.png)
### 再起動の完了
ログイン画面にサインインと表示されたら、管理用言語の変更完了です。「**サインイン**」をクリックします。

![](446.png)
## 地域の変更
### 設定画面を開く
デスクトップ画面が表示されたら、スタートメニューをクリックし、「**設定**」をクリックします。

![](451.png)

### 設定画面の表示
設定画面が表示されたら、左側の「**時刻と言語**」をクリックします。

![](453.png)

### 時刻と言語の表示
時刻と言語が表示されたら、右側の「**言語と地域**」をクリックします。

![](455.png)

### 国または地域の表示
言語と地域が表示されたら、国または地域の「**米国 ｖ**」をクリックします。

![](457.png)

### 国または地域
リストが表示されたら、「**日本**」を選択します。

![](459.png)

## タイムゾーンの変更
### 設定画面を開く
スタートメニューをクリックし、「**設定**」をクリックします。

![](451.png)

### 設定画面の表示
設定画面が表示されたら、左側の「**時刻と言語**」をクリックします。

![](453.png)

### 時刻と言語の表示
時刻と言語が表示されたら、右側の「**タイムゾーン**」をクリックします。

![](471.png)

### タイムゾーンの表示
タイムゾーンの詳細が表示されたら、「**(UTC-08:00) 太平洋標準時（米国およびカナダ）▽**」をクリックします。

![](473.png)

### タイムゾーンの選択
リストが表示されたら、「**(UTC+9:00)大阪、札幌、東京**」を選択します。

![](475.png)

### タイムゾーンの確認
時刻が変われば設定完了です。

![](477.png)

## キーボードレイアウトの変更
### 設定画面を開く
スタートメニューをクリックし、「**設定**」をクリックします。

![](451.png)
### 設定画面の表示
設定画面が表示されたら、左側の「**時刻と言語**」をクリックし、右側の「**言語と地域**」をクリックします。

![](481.png)
### 設定画面の表示
言語と地域が表示されたら、「**日本語**」の「**…**」をクリックし、「**言語のオプション**」をクリックします。

![](483.png)

### キーボードの詳細設定
言語のオプションが表示されたら、キーボードレイアウトの「**レイアウトを変更する**」をクリックします。

![](485.png)

### キーボードレイアウトの変更
ハードウェアキーボードのレイアウトの変更が表示されたら、「**英語キーボード(101/102キー)**」をクリックします。

![](487.png)
### 日本語キーボードの選択
リストが表示されたら、「**日本語キーボード(106/109キー)**」を選択します。

![](489.png)
### レイアウトの変更
「**今すぐ再起動する**」をクリックします。

![](491.png)

## リモートデスクトップの有効化
### 設定画面を開く
スタートメニューをクリックし、「**設定**」をクリックします。

![](451.png)

### 設定画面の表示
設定画面が表示されたら、左側の「**システム**」をクリックします。

![](453.png)
### リモートデスクトップの選択
右側のを下にスクロールし、「**リモートデスクトップ**」をクリックします。

![](513.png)

### リモートデスクトップのON
リモートデスクトップの詳細が表示されたら、リモート デスクトップを「**オン**」にします。

![](514.png)
### 確認
確認画面が表示されたら、「**確認**」をクリックします。

![](515.png)
### リモートデスクトップの確認
リモートデスクトップがONになれば設定完了です。

![](517.png)

### 仮想マシン接続の終了
Hyper-V 接続アプリの「X」をクリックして、仮想マシンから一旦切断します。

![](571.png)

### 仮想マシン接続の終了
Hyper-V マネージャーの メニューから 「**操作 > 接続**」 の順にクリックします

![](573.png)

## 接続時の設定
接続画面が開いたら、「**オプションの表示**」をクリックします。

![](577.png)

## 接続時の設定
オプションの画面が開いたら、「**ローカルリソース > 詳細**」をクリックします。

![](579.png)

## 接続時の設定
ローカルリソースの画面が開いたら、「**ドライブ**」のチェックをオンにし、「**OK**」をクリックします。

![](581.png)
　
## 接続時の設定
「**接続**」をクリックします。

![](583.png)
### ドライブの共有
仮想マシンにホストマシンのドライブが共有されます。

![](585.png)

## 仮想マシンの停止
### 操作の停止
Hyper-V 接続アプリのメニューから 「**操作 > 停止**」 の順にクリックします

![](591.png)
### 停止の確認
確認画面が表示されたら、「**停止する**」をクリックします。

![](593.png)


## 参考文献
- Learn > 仮想化 > Windows 10 の Hyper-V > Hyper-V を使用した仮想マシンの管理 
https://learn.microsoft.com/ja-jp/virtualization/hyper-v-on-windows/user-guide/enhanced-session-mode