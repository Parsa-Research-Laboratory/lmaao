from lava.magma.core.model.py.model import PyLoihiProcessModel
from lava.magma.core.decorator import implements, requires, tag
from lava.magma.core.resources import CPU
from lava.magma.core.model.py.type import LavaPyType
from lava.magma.core.model.py.ports import PyInPort, PyOutPort
from lava.magma.core.process.variable import Var
from lava.magma.core.sync.protocols.loihi_protocol import LoihiProtocol

import numpy as np

from lmao.test_functions.base.process import BaseFunctionProcess


class HimmelblauProcess(BaseFunctionProcess):

    def __init__(self, **kwargs):
        super().__init__(num_params=2, **kwargs)


@implements(proc=HimmelblauProcess, protocol=LoihiProtocol)
@requires(CPU)
@tag('floating_pt')
class PyHimmelblauProcessModel(PyLoihiProcessModel):

    input_port: PyInPort = LavaPyType(PyInPort.VEC_DENSE, np.float32)
    output_port: PyOutPort = LavaPyType(PyOutPort.VEC_DENSE, np.float32)

    num_params = LavaPyType(int, int)
    num_outputs = LavaPyType(int, int)

    def run_spk(self):
        if self.input_port.probe():
            input_data = self.input_port.recv()

            output_packet = np.zeros((self.num_outputs + self.num_params), dtype=np.float32)
            output_packet[:self.num_params] = input_data

            x0 = input_data[0]
            x1 = input_data[1]

            y = (((x0**2 + x1 - 11)**2) + (((x0 + x1**2 - 7)**2)))

            output_packet[self.num_params:] = y

            self.output_port.send(output_packet)
        else:
            pass

