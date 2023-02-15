VXI-11通信プロトコルの紹介
C#

VXI-11（ぶいえっくすあいいれぶん）はオシロスコープ等の電子計測器の制御に使われるイーサネット通信プロトコルです。VXI-11 を理解するには、電子計測器の通信インタフェースとして使われる GP-IB（じーぴーあいびー）と、ネットワーク通信プロトコルの RPC（あーるぴーしー） の知識を前提とします。そこでまず GP-IB と RPC を説明し、次に VXI-11 の概要を説明します。対象読者としてイーサネットの基本（ツイストペア結線、IPアドレスとTCP ポート番号）を知っている18歳の新人技術者を想定しています。

# GP-IB について

GP-IB はデジタルマルチメータや信号発生器を制御するために1960年代に設計された通信規格です。コネクタや電気信号を規定した [IEEE488.1](https://standards.ieee.org/ieee/488/6465/)(あいとりぷるいーよんはちはちぽいんとわん、通称ぽいんとわん) と、コマンド形式や共通コマンドを規定した [IEEE488.2](https://standards.ieee.org/ieee/488.2/717/)(あいとりぷるいーよんはちはちぽいんとつー、通称ぽいんとつー)  の２つの仕様があります。最新版は [IEEE/IEC 60488-1-2004](https://standards.ieee.org/ieee/60488-1/3686/) と [IEEE/IEC 60488-2-2004](https://standards.ieee.org/ieee/60488-2/3632/) です。

GP-IB は24ピンの頑丈なコネクタでねじ止めするため、断線トラブルや引き抜きトラブルがありません。また制御信号はグランド線とツイストぺアで配線されており電子ノイズに強く、三線式ハンドシェークによりトラブル発生時の原因特定が容易なため、高い信頼性が必要な工場の生産ラインの通信方式として利用されます。

GP-IB の特徴的な用語を説明します。

### リモート、ローカル、ローカルロックアウト
(TODO)
### トリガー
(TODO)
### デバイスクリア
(TODO)
### サービスリクエスト
(TODO)
### ステータスバイト
(TODO)
### *IDN?コマンド
(TODO)
### インタラプトエラー
(TODO)

# RPCについて

RPC はイーサネット経由で遠隔地にあるコンピュータを制御するために1980年代に実用化された通信プロトコルです。[RFC 1831](https://www.rfc-editor.org/rfc/rfc1831) というインターネット規格になっています。

RPC の用語を説明します
### サーバ、クライアント
(TODO)
### CALL、REPLY
(TODO)
### プログラム番号、プログラムバージョン
(TODO)
### 認証機構、perf verif
(TODO)
### ステータス、エラーコード
(TODO)
### ポートマッパ
(TODO)
### 任意長データ
(TODO)

# VXI-11について

VXI-11 は　GP-IB の機能をイーサネット通信で実現するために1990年代に策定された規格です。[VXI-11 REVISION 1.0](https://www.vxibus.org/specifications.html) という業界規格です。物理層にイーサネット、トランスポート層に TCP、セッション層に RPC を用い、プレゼンテーション層に VXI-11 があります。

VXI-11の特徴を以下にあげます。

### コアチャネル、インタラプトチャネル
(TODO)
### プログラム番号、プログラムバージョン
(TODO)
### ロック
(TODO)
### 関数一覧表
(TODO)

# VXI-11.Netについて

VXI-11.NET はクラスルームでの学習を対象とする、VXI-11通信ソフトウェアです。サーバアプリケーションとクライアントアプリケーションの２つがあります
- https://github.com/mitakalab1/VXI-11.Net

# VXI-11 の周辺規格について

VXI-11 を前提にした規格がいくつかあります。主な規格を手短に紹介します

### HiSLIPプロトコル
2010年代に策定された VXI-11 の後継のイーサネット通信プロトコルです。[IVI-6.1: High-Speed LAN Instrument Protocol](https://www.ivifoundation.org/specifications/)という業界規格です。

### VISAライブラリ
GP-IB, VXI-11 等を共通の関数で制御するための通信ライブラリ。[VPP-4.3: The VISA Library](https://www.ivifoundation.org/specifications/)という業界規格です。

### SCPI
オシロスコープ、デジタルマルチメータ、任意信号発生器などの製品カテゴリ別の共通コマンドの規定。[Standard Commands for Programmable Instruments-1999](https://www.ivifoundation.org/specifications/)という業界規格です。

### IVI ドライバ
SCPI対応機器を制御するためのC++/C#のクラスライブラリ。[IVI Specifications](https://www.ivifoundation.org/specifications/)という業界規格です。測定器の仮想化に対応しています。

# 参考文献

仕様をより深く理解したい人向けの日本語解説記事を挙げます。

- [GPIB通信の基礎知識と用語集](https://www.contec.com/jp/support/basic-knowledge/daq-control/gpib-communication/)
