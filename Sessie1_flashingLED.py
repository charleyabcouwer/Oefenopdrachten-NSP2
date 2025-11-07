import time
import pyvisa

print("Hello world, dit is een commit change.")

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n"  
)


# for spanning in range(0, 1023):
#     eind_spanning = device.query(f"OUT:CH0 {spanning}")
#     print(eind_spanning)
#     time.sleep(0.001)

# heartbeat light



hartslag = device.query(f"OUT:CH0 {1023}")
geen_hartslag = device.query(f"OUT:CH0 {0}")



for t in range(0, 1000):

    hartslag = device.query(f"OUT:CH0 {1023}")
    geen_hartslag = device.query(f"OUT:CH0 {0}")

    print(hartslag)
    time.sleep(0.5)
    print(geen_hartslag)
    time.sleep(0.05)
    print(hartslag)
    time.sleep(0.5)
    print(geen_hartslag)
    time.sleep(0.1)




