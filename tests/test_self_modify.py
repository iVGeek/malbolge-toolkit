from src.vm.full_malbolge_vm import FullMalbolgeVM


def test_memory_self_modify():
    # Program: mov 1 ; hlt
    prog = bytes([40, 1, 239])
    vm = FullMalbolgeVM()
    vm.load(prog)
    original = vm.memory[0]
    vm.step()
    # After executing the instruction at address 0, the memory at 0 should change
    assert vm.memory[0] != original
