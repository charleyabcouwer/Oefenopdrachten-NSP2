# Pyvisa shell openen: uvx --from pyvisa --with pyvisa-py --with pyserial pyvisa-shell --backend py
# Foutmelding bij openen nieuwe terminal: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# Arduino openen: 
# 1) Bovenste comment in terminal. 2) (visa) list 3) open 4, of een andere channel waar de Arduino is.
# Daarna: 1) help termchar. 2) termchar CRLF LF

# Arduino channel vinden: list opgvragen met kabel en zonder kabel: missende poort = Arduino. 

import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

# Arduino poort: ASRL5::INSTR, verschilt per aansluiting / Arduino. 

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n"
)
identification = device.query("*IDN?")
print(identification)