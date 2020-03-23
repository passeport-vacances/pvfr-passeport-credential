# Copyright 2020 Jacques Supcik, Passeport vacances Fribourg
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
"""Library for generating verifiable credentials for the Passeport vacances Fribourg

This library is used to generate verifiable serial numbers or verifiable passwords
for the Passeport vacances Fribourg. It is also used to check if a serial number
or a password is valid.

Typical usage example:

.. code:: python

    from pvfr.passeport_credential import Signer, SerialNumber, Password

    s = Signer("f09d837b265d7ff95d724c7f9dcc8b51dc6a357db5630eedff48b6c1659e2181")

    serialGen = SerialNumber(s)
    print(serialGen.serial(0))
    print(serialGen.check("000100994252"))

    pwGen = Password(s)
    print(pwGen.password(0))
    print(pwGen.check(0,"yd2f-ktfb-dyru"))
"""

__version__ = "2.0.0"

import hmac
import string
import typing
from hmac import HMAC


class Signer:
    """The Signer is able to produce a HMAC signature, based on a secret key, for an integer
    """

    def __init__(self, key: str, length: int = 4):
        """Initialize the signer with the given key.

        Args:
            key (str): The signing key.
            len (int): The maximum number of digits of the number to sign.
        """
        self.key = bytearray.fromhex(key)
        self.length = length

    def signature(self, number: int) -> int:
        """Sign the number.

        Args:
            number (int): The number to sign.
        Returns:
            int: The signature.
        """
        # pylint: disable = invalid-name
        f = "{:0" + str(self.length) + "d}"
        msg: str = f.format(number)
        return int(
            hmac.new(self.key, msg=msg.encode(),
                     digestmod="sha256").hexdigest(), 16)

    def __str__(self) -> str:
        return f"Signer({self.key})"


class Credential:
    """The Credential is the base class for `SerialNumber` and `Password`
    """

    def __init__(self, signer: Signer):
        """Initialize the credential with a signer.

        Args:
            signer (Signer): The signer associated with the credential.
        """
        self.signer = signer

    def signature(self, number: int) -> int:
        """Generate a signature.

        Args:
            number (int): The number to sign.
        Returns:
            int: The signature.
        """
        return self.signer.signature(number)

    def __str__(self):
        return "Credential with {self.signer}"


class SerialNumber(Credential):
    """Class to generate and verify Serial Numbers
    """

    def __init__(self, signer: Signer, size: int = 8):
        """Initialize the serial number

        Args:
            signer (Signer): The signer associated with the credential.
            size (int): The size (length) of the serial number.
        """
        super().__init__(signer)
        self.size = size

    def serial(self, number: int) -> str:
        """Generate a serial number for `number`

        Args:
            number (int): The number to generate a serial number for.
        Returns:
            str: The serial number.
        """
        return "{:04d}".format(number) + "{:08d}".format(
            self.signature(number))[-self.size:]

    def check(self, ser: str) -> bool:
        """Check a serial number

        Args:
            ser (str): The serial number to check.
        Returns:
            bool: True if the serial number is valid.
        """
        try:
            number = int(ser[0:4])
            return self.serial(number) == ser
        except Exception:  # pylint: disable = broad-except
            return False


class Password(Credential):
    """Class to generate and verify Passwords

    The passwords are composed of blocks of digits and lettres, excluding the characters
    that can easily be mistaken (such as 0 and O or 1 and l).
    """

    def __init__(self, signer: Signer, blocks: int = 3, size: int = 4):
        """Initialize the password

        Args:
            signer (Signer): The signer associated with the credential.
            blocks (int): The number of blocks composing the password.
            size (int): The size (length) of each blocks.
        """
        super().__init__(signer)
        self.blocks = blocks
        self.size = size

    _alphabet = sorted(
        list(
            set(string.ascii_lowercase + string.digits) -
            set(list("0Ool19g5SB8qQ"))))

    def password(self, number: int) -> str:
        """Generate a password for `number`

        Args:
            number (int): The number to generate a password for.
        Returns:
            str: The password.
        """
        pass_blocks: typing.List[str] = list()
        sig = self.signature(number)
        for _ in range(self.blocks):
            block: str = ""
            for _ in range(self.size):
                block += Password._alphabet[sig % len(Password._alphabet)]
                sig = sig // len(Password._alphabet)
            pass_blocks.append(block)
        return "-".join(pass_blocks)

    def check(self, number: int, passwd: str) -> bool:
        """Check a password

        Args:
            number (int): The number from the username.
            passwd (str): The password to check.
        Returns:
            bool: True if the password is valid for the number.
        """
        return self.password(number) == passwd
