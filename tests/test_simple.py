# Copyright 2018 Jacques Supcik, Passeport vacances Fribourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from pvfr.passeport_credential import Signer, SerialNumber, Password


class SimpleTest(unittest.TestCase):
    def test(self):
        s = Signer("f09d837b265d7ff95d724c7f9dcc8b51dc6a357db5630eedff48b6c1659e2181")
        serialGen = SerialNumber(s)
        self.assertEqual(serialGen.serial(0), "000075101802")
        pwGen = Password(s)
        self.assertEqual(pwGen.password(0), "yd2f-ktfb-dyru")
