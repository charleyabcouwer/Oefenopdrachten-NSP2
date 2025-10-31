import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n"  
)


for spanning in range(0, 1023):
    eind_spanning = device.query(f"OUT:CH0 {spanning}")
    print(eind_spanning)
    

