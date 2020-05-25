from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

r1 = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
r2 = Rotor('my rotor2', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', ring_setting=5, stepping='E')
r3 = Rotor('my rotor3', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=15, stepping='V')

reflector = Rotor('my reflector', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')

pb = Plugboard.from_key_sheet('PO ML IU KJ NH YT GB VF RE DC')

machine = EnigmaMachine([r1, r2, r3], reflector, pb)
