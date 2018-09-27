import textwrap

from tests.common import exercise_code_verbosely
from tests.int_mod_n import int_mod_n


def integer_group_functions():
    # 2048 bit modulus
    small_prime = int(''.join(textwrap.dedent("""
        2634427397878110232503205795695468045251992992603340168049253044454387
        1080897872360133472596339100961569230393163880927301060812730934043766
        3646941725034559080490451986171041751558689035115943134790395616490035
        9846986660803055891526943083539429058955074960014718229954545667371414
        8029627597753998530121193913181474174423003742206534823264658175666814
        0135440982296559552013264268674093709650866928458407571602481922443634
        2306826340229149641664159565679297958087282612514993965471602016939198
        7906354607787482381087158402527243744342654041944357821920600344804411
        149211019651477131981627171025001255607692340155184929729""").split(
            "\n")))
    # 4096 bit modulus
    large_prime = int(''.join(textwrap.dedent("""
        8466908771297228398108729385413406312941234872779790501232479567685076
        4762372651919166693555570188656362906279057098994287649807661604067499
        3053172889374223358861501556862285892231110003666671700028271837785598
        2711897721600334848186874197010418494909265899320941516493102418008649
        1453168421248338831347183727052419170386543046753155080120058844782449
        2367606252473029574371603403502901208633055707823115620627698680602710
        8443465519855901353485395338769455628849759950055397510380800451786140
        7656499749760023191493764704430968335226478156774628814806959050849093
        5035645687560103462845054697907307302184358040130405297282437884344166
        7188530230135000709764482573583664708281017375197388209508666190855611
        3020636147999796942848529907410787587958203267319164458728792653638371
        7065019972034334447374200594285558460255762459285837794285154075321806
        4811493971019446075650166775528463987738853022894781860563097254152754
        1001763544907553312158598519824602240430350073539728131177239628816329
        0179188493240741373702361870220590386302554494325819514615309801491107
        2710093592877658471507118356670261129465668437063636041245619411937902
        0658733974883998301959084381087966405508661151837877497650143949507846
        1522640311670422105209760172585337397687461""").split("\n")))
    N = small_prime
    N = large_prime
    initial_x = int_mod_n(
        15619920774592561628351138998371642294622340518469892832433140464182509560910157, N)

    element_size_bytes = N.bit_length() // 8

    return initial_x, 1, element_size_bytes, int(N.bit_length())


def test_main():
    exercise_code_verbosely(integer_group_functions)


if __name__ == '__main__':
    test_main()


"""
Copyright 2018 Chia Network Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""