from src.vm.malbolge_vm import SimpleMalbolgeVM


def test_vm_out_and_halt():
    # Program: out 65, hlt
    prog = bytes([5, 65, 239])
    vm = SimpleMalbolgeVM()
    vm.load(prog)
    out = vm.run()
    assert out == b'A'
