# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import cast, TYPE_CHECKING

from streamlit.proto.Balloons_pb2 import Balloons as BalloonsProto

if TYPE_CHECKING:
    from streamlit.delta_generator import DeltaGenerator


class BalloonsMixin:
    def balloons(self) -> "DeltaGenerator":
        """Draw celebratory balloons.

        Example
        -------
        >>> st.balloons()

        ...then watch your app and get ready for a celebration!

        """
        balloons_proto = BalloonsProto()
        balloons_proto.show = True
        dg = self.dg._enqueue("balloons", balloons_proto)
        return cast("DeltaGenerator", dg)

    @property
    def dg(self) -> "DeltaGenerator":
        """Get our DeltaGenerator."""
        return cast("DeltaGenerator", self)
