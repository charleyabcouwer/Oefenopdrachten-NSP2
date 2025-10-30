# Pyvisa shell openen: uvx --from pyvisa --with pyvisa-py --with pyserial pyvisa-shell --backend py
# Foutmelding bij openen nieuwe terminal: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

# Arduino poort: ASRL5::INSTR

device = rm.open_resource(
    "ASRL5::INSTR", read_termination="\r\n", write_termination="\n"
)
identification = device.query("*IDN?")
print(identification)