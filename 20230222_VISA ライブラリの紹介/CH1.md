# VISA ライブラリの紹介
タグ：C#

1995年に測定器業界団体が策定した、計測機器の GP-IB, RS-232, USB, イーサネットといった異なる通信規格に対して同一関数で操作するための通信ライブラリです。VMEバスや PCI バスを想定したメモリ読み書き関数群と、GP-IB や VXI-11 を対象とするメッセージ送受信関数群があります。仕様書は [VPP-4.3: The VISA Library](https://www.ivifoundation.org/specifications/) です。
VISAライブラリには、以下のような関数が含まれます。

- viOpenDefaultRM()
- viOpen()
- viClose()
- viSetAttribute()
- viGetAttribute()
- viWrite()
- viRead()
- viPrintf()
- viScanf()
- viFlush()
- viClear()
- viLock()
- viUnlock()
- viStatusDesc()
- viTerminate()
- viFindRsrc()
- viFindNext()
- viIn8()
- viOut8()
- viIn16()
- viOut16()
- viIn32()
- viOut32()

### viOpenDefaultRM()
### viOpen()
### viClose()
### viSetAttribute()
### viWrite()
### viRead()
