# ONC RPC の概要

RPC(Remote Procedure Call) とは遠隔にあるコンピュータの関数を実行するためのソフトウェアの技術です。ここでは 1990 年代に広く普及した ONC RPC（いわゆる SunRPC）を解説します。対象読者としてイーサネットの基本（IPアドレスとTCP通信）とプログラムの基本（関数、変数、引数、戻り値）がわかる 18 歳の新人技術者を想定しています。

# RPC の背景と目的

RPC(Remote Procedure Call) は分散コンピューティング分野のソフトウェア技術です。次の目的を達成するために開発されました。
- 遠隔地にあるコンピュータや方式の異なるマシン間で透過的なデータのやり取りを可能にする
- 様々なサービスについて一貫性のある環境を提供する
- 高いレベルの機能を実現しプログラマの負担を減らす

![](021_RemoteProcedureCall.png)

RPC の技術的な特徴は以下の通りです。
- クライアント・サーバモデル
- 関数・引数・戻り値があり、通常の関数呼び出しと同様に実行できる
- 同期式通信を基本とし、非同期式通信もできる

1980年代以降、多くの会社が RPC を実現するためのプロトコルを策定しました。ONC RPC は 1988 年にサンマイクロシステムズが [RFC 1057: RPC: Remote Procedure Call Protocol specification Version 2](https://www.ietf.org/rfc/rfc1057.txt) として策定しました。当時のソースコードは [4.3BSD-Reno/lib/librpc/](https://github.com/dank101/4.3BSD-Reno/tree/master/lib/librpc) で閲覧できます。

RPC プロトコルの歴史を以下に示します。

|年|企業|プロトコル名|概要|
|----|----|----|----|
|1976 年|スタンフォード研究所|RFC 707 High-Level Framework for Network-Based Resource Sharing|RPCのコンセプトの提案|
|1981 年|ゼロックス|Courier|最初の商用実用化の１つ|
|1988 年|サン・マイクロシステムズ|RFC 1057 Remote Procedure Call (ONC RPC)|最初のオープンソースの RPC プロトコル|
|1995 年|マイクロソフト|MS-RPC|Windows 向け RPC プロトコル|
|2003 年|サン・マイクロシステムズ|JAX-RPC|Java 言語向け RPC プロトコル|
|2015 年|グーグル|gRPC|HTTP/2 を使った RPC プロトコル|

# 基本的な RPC のプロトコル

一般的なプログラムでの関数呼び出しは

1. 親プログラムが関数名と引数を指定して、特定の関数を呼び出す
2. その関数の処理が実行される
3. 結果の戻り値が、親プログラムに渡される

という順序で行われます。

![ローカル関数呼び出し](352_RPC_LocalFunctionCall_Sequence.png)

RPC はネットワーク環境のクライアントとサーバ間の通信を、一般的な関数呼び出しのように見せることを目的しています。関数呼び出しをクライアントとサーバ間の通信に変換する動作は以下の通りです。

1. クライアント側の親プログラムは、その処理を実行する関数が自分のプログラム内に存在するかのように、特定の関数を呼び出します。
2. 呼び出した関数名、引数などは「スタブ (Stub)」と呼ばれるプログラムによって、RPC のプロトコルで定められた RPC メッセージ(callメッセージ)に組み立てられます
3. TCP や UDP といったトランスポートプロトコルによって、このメッセージがサーバ側に転送されます。
4. サーバ側のスタブ・プログラムは呼び出された関数、引数を取り出して、該当するプログラムを実際に呼び出します。
5. サーバ側でプログラムで要求された関数が実行されます。
6. 関数の実行結果が、サーバ側のスタブ・プログラムに戻され、結果を返すための RPC メッセージ(repy メッセージ)に組み立てられます
7. そのRPCメッセージがクライアント側に転送されます。
8. クライアント側のスタブ・プログラムが戻り値（結果）を取り出して、処理を依頼した親プログラムに戻します。

![リモート関数呼び出し](353_RPC_RemoteProcedureCall_Sequence.png)

# ONC RPC のデータ表現

ONC RPC は異なるコンピュータ間で相互通信できるようデータの構造を XDR として規定しています。XDR の詳細仕様は [RFC 1014 XDR: External Data Representation Standard](https://www.ietf.org/rfc/rfc1014.txt) で公開されています。

![XDR の OSI 階層モデル](031_RPC_Layer.png)

XDR が対応しているデータ型は以下の通りです。

|データ型|サイズ|
|----|----|
|符号付き整数型|4 バイト。|
|符号なし整数型|4 バイト。|
|列挙型|符号付き整数と同じ。|
|ブール型|列挙型と同じ。|
|ハイパー整数|8 バイト。|
|符号なしハイパー整数型|8 バイト。|
|浮動小数点型|4 バイト。|
|倍精度浮動小数点型|8 バイト。|
|固定長の任意データ型|全体のバイト数が 4 の倍数でない場合、末尾に追加の 0 が付きます。|
|可変長の任意データ型|長さを表現する4バイトのシーケンスが先頭に付きます。全体のバイト数が 4 の倍数でない場合、末尾に追加の 0 が付きます。|
|文字列|長さを表現する4バイトのシーケンスが先頭に付きます。全体のバイト数が 4 の倍数でない場合、末尾に追加の 0 が付きます。|
|固定長の配列型|各要素が 1 番目から n 番目まで並びます。|
|可変長の配列型|長さを表現する4バイトのシーケンスが先頭に付きます。各要素が 1 番目から n 番目まで並びます。|
|構造体型|構造体で宣言される順番でコード化されます。|
|区別された共用体型|共用体の区別値と実際の値の順番でコード化されます。|
|ボイド型|0 バイト|

整数型は以下のようなメモリ配置になります。

![XDR の整数型のメモリ配置](551_RFC1014_3.1_Integer_Format.png)

文字列型は下のようなメモリ配置になります。

![XDR の文字列型のメモリ配置](552_RFC1014_3.10_String_Format.png)

# ONC RPC のデータ構造

RPC でリモートの関数を呼び出す時のフォーマットは以下の通りです。

![関数呼び出しのヘッダフォーマット](362_RFC1057_Call_HeaderFormat.png)

+ LAST_FLAG：トランスポートプロトコルが TCP の場合のみ付きます。呼び出しデータが複数のメッセージに分割されているかを示します。
+ flag_header：トランスポートプロトコルが  TCP の場合のみ付きます。flag_header を除いたメッセージ全体の長さを示します。
+ xid：xid は１つの関数の呼び出しと応答で同一の値をとります。トランザクション識別子とも呼ばれます。
+ msg_type：msg_type は呼び出しメッセージか応答メッセージの区別を示します。

|値|定数名|意味|
|--|--|--|
|0|CALL|関数の呼び出し|
|1|REPLY|関数の応答|

+ rpcvers：rpcvers は RPC プロトコルのバージョンを示します。通常は 2 になります。
+ prog, vers, proc：prog（プログラム番号）, vers（バージョン番号）, proc（プロシージャ番号） の組は実行する関数を示します
+ cred.flavor, cred.body, verf.flavor, verf.body：これらはクライアント認証に関するパラメータです。認証を使わない場合、すべて 0 になります。
+ データ：関数の引数を示します。

応答を返す時のフォーマット

![RPC 応答のヘッダフォーマット](364_RFC1057_Reply_HeaderFormat.png)

+ LAST_FLAG：トランスポートプロトコルが TCP の場合のみつきます。呼び出しデータが複数のメッセージに分割されているかを示します。
+ flag_header：トランスポートプロトコルが TCP の場合のみつきます。flag_header を除いたメッセージ全体の長さを示します。
+ xid：xid は応答に対応する呼び出しメッセージのトランザクション識別子を示します。
+ msg_type：msg_type は呼び出しメッセージか応答メッセージの区別を示します。

|値|定数名|意味|
|--|--|--|
|0|CALL|関数の呼び出し|
|1|REPLY|関数の応答|

+ reply_stat：RPCメッセーを受け付けたかどうかを示します。RPCバージョンが2以外の場合や認証に失敗した場合にエラーが返ります。

|値|定数名|意味|
|--|--|--|
|0|MSG_ACCEPTED|正常に実行された|
|1|MSG_DENIED|エラーが発生した|

+ accept_stat：RPC の関数を実行したかどうかを示します。以下の値をとります。

|値|定数名|意味|
|--|--|--|
|0|SUCCESS|RPCが正常に実行された|
|1|PROG_UNAVAIL|リモートがプログラムをエクスポートしていない|
|2|PROG_MISMATCH|リモートがバージョン番号をサポートしていない|
|3|PROC_UNAVAIL|プログラムがプロシージャをサポートしていない|
|4|GARBAGE_ARGS|プロシージャはパラメータをデコードできません|

+ verf.flavor, verf.body：クライアント認証の結果に関するパラメータです。認証を使わない場合、すべて 0 になります。
+ データ：関数の戻り値を示します。

# RPC の事例：ポートマッパ

ポートマッパは  [RFC 1057: RPC: Remote Procedure Call Protocol specification Version 2](https://www.ietf.org/rfc/rfc1057.txt) 内で定義されているプログラム番号に対応する TCP または UDP のポート番号を返すサービスです。ポートマッパ自身は TCP または UDP の 111 番ポートを使います。

![ポートマッパの動作フロー](402_Portmap.png)

## ポートマッパの関数

ポートマッパはプログラム番号 10000 の RPC として定義されています。ポートマッパは次のような機能をもちます

|関数名|プログラム番号|バージョン番号|プロシージャ番号|引数|戻り値|説明|
|----|----|----|----|----|----|----|
|PMAPPROC_NULL|10000|2|0|void|void|この関数はテスト用です。何も実行しません。|
|PMAPPROC_SET|10000|2|1|mapping 構造体|bool|ポートマッパにポート番号を登録します。|
|PMAPPROC_UNSET|10000|2|2|mapping 構造体|bool|ポートマッパに登録されているポート番号を削除します。|
|PMAPPROC_GETPORT|10000|2|3|mapping 構造体|unsigned int|対象プログラムのポート番号を返します。|
|PMAPPROC_DUMP|10000|2|4|void|pmaplist 構造体の配列|ポートマッパの登録プログラム一覧を返します。|
|PMAPPROC_CALLIT|10000|2|5|call_args 構造体|call_result 構造体|別の関数を呼び出します。|

## PMAPPROC_GETPORT のデータ構造

ポートマッパの PMAPPROC_GETPORT 関数の呼び出しメッセージを以下に示します。

![PMAPPROC_GETPORT 関数の呼び出しメッセージ](451_RFC1057_A1_PMAPPROC_GETPORT_args.png)

各項目の説明は以下の通りです。

+ xid：一意の識別子を指定します。
+ prog, vers：ポート番号を取得したいプログラム番号とバージョン番号を指定します。
+ prot：プロトコル種別を指定します。

|値|定数名|意味|
|----|----|----|
|6|IPPROTO_TCP|TCP プロトコル|
|17|IPPROTO_UDP|UDP プロトコル|

ポートマッパの PMAPPROC_GETPORT 関数の応答メッセージを以下に示します。

![PMAPPROC_GETPORT 関数の応答メッセージ](453_RFC1057_A1_PMAPPROC_GETPORT_result.png)

各項目の説明は以下の通りです。

- xid：関数呼び出し時の識別子を示します。
- port：プログラム番号に対応する TCP または UDP のポート番号を示します。


## ポートマッパの通信フロー

最後に ポートマッパのパケットキャプチャの例を示します。

![wireshark のキャプチャ](610_wireshark.png)

# 参考文献
本ページで引用した参考文献を挙げます。

- [RFC 1057 RPC: Remote Procedure Call Protocol specification ersion 2](https://www.ietf.org/rfc/rfc1057.txt)
- [4.3BSD-Reno/lib/librpc/](https://github.com/dank101/4.3BSD-Reno/tree/master/lib/librpc)
- [RFC 1014 XDR: External Data Representation Standard](https://www.ietf.org/rfc/rfc1014txt)
- [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
