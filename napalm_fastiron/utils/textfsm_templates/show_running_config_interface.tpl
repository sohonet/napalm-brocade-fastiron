Value Interface (\S+)
Value InterfaceNum (\S+)
Value DualMode (\d+)

Start
  ^interface ${Interface} ${InterfaceNum}
  ^\s+dual-mode\s+${DualMode}
  ^! -> Record
