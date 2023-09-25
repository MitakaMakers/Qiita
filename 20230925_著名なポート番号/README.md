
IANAが規定したウェルノウン・ポート

TCP と UDP では　1番から 65535番までのポート番号が使われます。
ポート番号は１つのアプリケーションで複数の番号を使う事ができます。
いくつかのポート番号は，一般的に知られているポート番号（ウェルノウン・ポート、well - known port number）として，決まったアプリケーション・サービスに割り当てられています。

以下に代表的なウェルノウン・ポートの一覧を示します。

[IANA > Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

|キーワード|ポート番号|プロトコル|説明|
|---|---|---|---|
|ftp-data|20|tcp|File Transfer（Default Data）|
|ftp|21|tcp|File Transfer（Control）|
|ssh|22|tcp|TELNET|
|telnet|23|tcp|TELNET|
|smtp|25|tcp|Simple Mail Transfer|
|domain|53|udp|Domain Name Server|
|bootps|67|udp|Bootstrap Protocol Server(DHCP)|
|bootpc|68|udp|Bootstrap Protocol Client(DHCP)|
|tftp|69|udp|Trivial File Transfer|
|www|80|tcp|World Wide Web HTTP|
|pop3|110|tcp|Post Office Protocol-Version 3|
|sunrpc|111|tcp/udp|SUN Remote Procedure Call|
|ntp|123|udp|Network Time Protocol|
|netbios-ns|137|tcp/udp|NetBIOS Name Service|
|netbios-dgm|137|udp|NetBIOS Datagram Service|
|netbios-ssn|139|tcp|NetBIOS Session Service|
|ptp-event|319|udp|PTP Event|
|ptp-general|320|udp|PTP General|
|https|443|tcp|http protocol over TLS/SSL|
|syslog|514|udp|syslog|
|dhcpv6-client|546|udp|DHCPv6 Client|
|dhcpv6-server|547|udp|DHCPv6 Server|
|ftps-data|989|tcp|file data over TLS/SSL|
|ftps|990|tcp|file control over TLS/SSL|
|hislip|4880|tcp|IVI High-Speed LAN Instrument Protocol|

