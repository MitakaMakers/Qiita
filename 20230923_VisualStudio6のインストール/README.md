# Windows 11 への Visual Studio 6.0 のインストール手順
Visual Studio VC6 VB6 

Visual Studio 6.0 は Windows 7 以降の OS をサポートしないため、そのまま Windows 11 にインストールしようとすると失敗します。この記事では入社 3 ～ 4 年目の若手エンジニア以上を対象に Visual Studio 6.0 のインストール手順を紹介します。

## Visual Studio 6.0 について

Visual Studio 6.0 はマイクロソフトが 1998 年にリリースした統合開発環境です。Visual C++ 6.0 や Visual Basic 6.0 といった複数のプログラム言語の開発環境が含まれます。2008年に Microsoftのサポートが終了し、更新パッチの配布も終了しています。一般的な開発プロジェクトでは新しいバージョンの Visual Studio に移行することが強く推奨されます。それでも Visual Studio 6.0 が必要となる状況を 2 つ挙げます。

### レガシーアプリケーションのサポート
一部の企業では 20 年以上前に作られた過去の Windows アプリケーションを保守する必要があります。これらのアプリケーションは、Visual C++ 6.0 や Visual Basic 6.0 で開発されたものかもしれません。Visual Studio 6.0 は、こういった昔のプログラムを保守するために必要な開発ツールを提供します。

### VBA マクロのアプリケーション化
Excel VBA で書かれたツールを単体アプリケーション(EXE)として作り直す場合、Visual Basic 6.0 は安価なソリューションです。

## Visual Studio 6.0 のシステム要件

Visual Studio 6.0 は以下の環境で動作します。

- プロセッサ: Pentium 90MHz 以上
- メモリ(RAM): 16MB 以上 (32MB 以上が推奨)
- ハードディスクの空き容量: 120MB 以上
- オペレーティングシステム: Windows NT 4.0 (Service Pack 3 以上) または Windows 95/98
- グラフィックス: Super VGA 解像度 (800x600) 以上のディスプレイ
- CD-ROM ドライブ: インストールメディアを読み込むために必要

この記事では MSDN 版 Visual Studio 6.0 Enterprise Edition を例にして Windows 11 Pro にインストールする手順を説明します。

## インストール手順
### a. Visual Studio 6.0 のインストール
Visual Studio 6.0, Enterprise Edition, Disk 1 の CD をパソコンに挿入します。

![](012.jpg)

CD-ROM 内の SETUP.EXE を右クリックし、「管理者として実行」で起動します。

![](103_VISUALSTUDIO6.png)

「プログラム互換アシスタント」が表示されたら、「閉じる」をクリックします。

![](105_VISUALSTUDIO6.png)

「セットアップウィザード」が表示されたら、「次へ」をクリックします。

![](107_VISUALSTUDIO6.png)

使用許諾契約の内容を確認して「同意します」を選択し、「次へ」をクリックします。

![](109_VISUALSTUDIO6.png)

「名前」を入力し、「次へ」をクリックします。

![](111_VISUALSTUDIO6.png)

「Microsoft Virtual Machine for Java」が表示されたら、「次へ」をクリックします。

![](113_VISUALSTUDIO6.png)

プログラム互換アシスタントのメッセージが表示されたら、「閉じる」をクリックします。

![](115_VISUALSTUDIO6.png)

Windows の機能の追加ウィザードが表示されたら、「この機能をインストールする」をクリックします。

![](119_VISUALSTUDIO6.png)

「Direct Play」のインストールに成功したら、「閉じる」をクリックします。

![](121_VISUALSTUDIO6.png)

「システムを再起動します」ダイアログが表示されたら、「OK」をクリックして Windows を再起動します。

![](123_VISUALSTUDIO6.png)

Windowsの再起動後、セットアップウィザードが表示されたら、「カスタム」を選択し、「次へ」をクリックします。

![](201_VISUALSTUDIO6.png)

「セットアップフォルダの選択」が表示されたら、「次へ」をクリックします。

![](203_VISUALSTUDIO6.png)

「セットアッププログラムへようこそ」が表示されたら、「継続」をクリックします。

![](206_VISUALSTUDIO6.png)

プロダクトIDを確認し、「OK」をクリックします。

![](208_VISUALSTUDIO6.png)

「カスタムオプション」の画面が表示されたら「データアクセス」を選択し、「オプションの変更」をクリックします。

![](210_VISUALSTUDIO6.png)

詳細オプションが表示されたら、「ADO、RDSおよびOLE DBプロバイダ」のチェックを外します。

![](212_VISUALSTUDIO6.png)

ダイアログが表示されたら、「OK」をクリックします。

![](213_VISUALSTUDIO6.png)

「ADO、RDSおよびOLE DBプロバイダ」のチェックが外れたことを確認し、「OK」をクリックします。

![](219_VISUALSTUDIO6.png)

「カスタムオプション」の画面に戻ったら、「継続」をクリックします。

![](222_VISUALSTUDIO6.png)

「環境変数の登録」の画面が表示されたら、「環境変数の登録」のチェックを外し、「OK」をクリックします。

![](223_VISUALSTUDIO6.png)

「新しいデータベース形式」のダイアログが表示されたら、「はい」をクリックします。

![](225_VISUALSTUDIO6.png)

「Windows セキュリティの警告」ダイアログが表示されたら、「プライベートネットワーク」と「パブリックネットワーク」をチェックし、「アクセスを許可する」をクリックします。

![](231_VISUALSTUDIO6.png)

「デバッグシンボル」ダイアログが表示されたら、「OK」をクリックします。

![](233_VISUALSTUDIO6.png)

「JIT」ダイアログが表示されたら、「いいえ」をクリックします。

![](237_VISUALSTUDIO6.png)

セットアップが完了したら、「Windowsの再起動」をクリックします。

![](240_VISUALSTUDIO6.png)

Windowsの再起動後、追加機能のセットアップウィザードが表示されたら、「MSDNのセットアップ」のチェックを外し、「次へ」をクリックします。

![](303_VISUALSTUDIO6.png)

「プログラムの互換性アシスタント」ダイアログが表示されたら、「このプログラムは正しくインストールされました」をクリックします。

![](305_VISUALSTUDIO6.png)

「確認」ダイアログが表示されたら、「はい」をクリックします。

![](307_VISUALSTUDIO6.png)

「その他のクライアントツール」の画面が表示されたら、何も選択せずに「次へ」をクリックします。

![](309_VISUALSTUDIO6.png)

「サーバー セットアップ」の画面が表示されたら、何も選択せずに「次へ」をクリックします。

![](311_VISUALSTUDIO6.png)

「今すぐ登録」のチェックをはずして、「完了」をクリックします。

![](315_VISUALSTUDIO6.png)

### b. Visual Studio 6.0 Service Pack 6 のインストール

Visual Studio 6.0 Service Pack 6 の CD をパソコンに挿入します。

![](014.jpg)

CD-ROM 内の SETUPSP6.EXE を「管理者として実行」で起動します。

![](403_VS6SP6.png)

セットアップウイザードが表示されたら 、「継続」をクリックします。

![](406_VS6SP6.png)

使用許諾契約の内容を確認して、「同意します」をクリックします。

![](407_VS6SP6.png)

MFC 日本語版の置き換えの確認が表示されたら、「いいえ」を選択します。

![](409_VS6SP6.png)

現在のファイルを残すかの確認が表示されたら、「はい」を選択します。

![](411_VS6SP6.png)

ファイルのコピーがはじまるので完了まで待機します。

![](414_VS6SP6.png)

インストール完了メッセージが表示されたら、「OK」をクリックしセットアップを終了します。

![](416_VS6SP6.png)

### c. Visual Basic 6.0 Service Pack 6 累積的な更新プログラムのインストール

マイクロソフトの「Visual Basic 6.0 Service Pack 6 累積的な更新プログラム」サイトにアクセスします。<BR>
https://www.microsoft.com/ja-jp/download/details.aspx?id=7030

サイトが表示されたら「ダウンロード」をクリックします。

![](603_VS6SP6UP.png)

ダウンロードした VB60SP6-KB2708437-x86-JPN.msi を実行します。

![](607_VS6SP6UP.png)

使用許諾契約の内容を確認して「同意する」を選択し、「次へ」をクリックします。

![](609_VS6SP6UP.png)

完了メッセージが表示されたら、「完了」をクリックし、セットアップを終了します。

![](611_VS6SP6UP.png)

### d. Visual Basic 6.0 の起動

Windows のスタートメニューから「全てのアプリ」→「Microsoft Visual Studio 6.0」を選択し、「Microsoft Visual Basic」を右クリックし、「管理者として実行」で起動します。

![](703_VB6.png)

### e. Visual Basic のバージョンを確認

Visual Basic のメニューから「ヘルプ」→「バージョン情報」をクリックします。  「Microsoft Visual Basic 6.0(SP6)」と表示されればOKです。

![](705_VB6.png)

## アンインストール手順

### コントロールパネルを開く方法
スタートボタンをクリックします。

![13.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/6bdeedc8-62a2-e4d8-88ff-0a837a7bc6d6.png)

スタートメニューが表示されたら、右上にある「すべてのアプリ」をクリックします。

![21.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/b625ae94-e15c-0399-6160-b30d34119229.png)

アプリ一覧が表示されたら下にスクロールし、「Windows ツール」をクリックします。

![23.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/8f7d684c-46b7-81a4-fd2f-8ac6280b22f8.png)

Windows ツールが表示されたら、「コントロールパネル」をクリックします。

![25.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/cb771013-9c7f-f7b7-0c20-8c83ce2e0944.png)

コントロールパネルが表示されたら、「プログラムのアンインストール」をクリックします。

![47.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/1122cf31-1af4-4d71-b198-b364bd7ba5ed.png)

### Microsoft Visual Basic 6.0 SP6 用の累積的な更新プログラムのアンインストール【問題あり】

プログラムの一覧から「Microsoft Visual Basic 6.0 SP6 用の累積的な更新プログラム」を右クリックし、「変更」をクリックします。

![](831.png)

使用許諾契約が表示されたら、「同意する」を選択し、「次へ」をクリックします。

![](833.png)

アンインストール中に「ネットワーク上の場所 Tools\Controls\Controls_Backupへアクセスできません。」 というメッセージが表示され、アンインストールできません。

![](835.png)

「キャンセル」をクリックすると、「セットアップに失敗しました」というダイアログが表示されて、アンインストールが中断します。

![](837.png)

**「対処方法をご存じの方は、方法を教えていただけると大変ありがたいです。**

### Microsoft Web 発行 ウィザード のアンインストール

プログラムの一覧から「Microsoft Web 発行 ウィザード」を右クリックし、［アンインストールと変更］をクリックします。

![](851.png)

確認メッセージが表示されたら、「はい」をクリックします。

![](855.png)

アンインストールが完了します。

![](857.png)

### Microsoft Visual Studio 6.0 Enterprise Edition のアンインストール

Visual Studio 6.0, Enterprise Edition, Disk 1 の CD をパソコンに挿入します。

![012.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3160433/72be49f6-4d1e-ee48-001c-40d7baf11af3.jpeg)

プログラムの一覧から「Microsoft Visual Studio 6.0 Enterprise Edition」を右クリックし、［アンインストール］をクリックします。

![](861.png)

セットアップが表示されたら、「すべて削除」をクリックします。

![](865.png)

確認メッセージが表示されたら、「はい」をクリックします。

![](867.png)

再起動を促すメッセージが表示されたら、「Windows の再起動」をクリックします。

![](869.png)

Windows を再起動すると、アンインストールの完了です。

![](871.png)
