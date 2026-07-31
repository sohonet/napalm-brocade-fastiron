Value Filldown,Required Interface (\S+)
Value Filldown,Required InterfaceNum (\S+)
Value Required VirtualIpv4address (\S+)

Start
  ^interface ${Interface} ${InterfaceNum}
  ^\s+ip vrrp(-extended)? vrid \d+ -> Vrrp
  ^! -> Clearall

Vrrp
  ^\s+ip-address ${VirtualIpv4address} -> Record Start
  ^interface ${Interface} ${InterfaceNum} -> Start
  ^! -> Clearall Start
