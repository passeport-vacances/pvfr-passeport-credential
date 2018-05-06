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
import pvfr.passeport_credential as cred


class SimpleTest(unittest.TestCase):
    def test(self):
        s_key = bytearray.fromhex("c31e739fbd3acf8592b65aaa3aacbf15876c87ebf999af8c33ca1e7892f619e8")
        p_key = bytearray.fromhex("ca1414bc18362e57e914f433c6c11439207c4953ad4b16d9bcf26d9ef5acae03")
        c = cred.Credential(s_key, p_key)
        self.assertEqual(c.bar_code(42), "246595760042")
        self.assertEqual(c.serial_pwd(42), "bvuz-bfnb-ktm6")
