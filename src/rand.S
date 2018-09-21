.global asm_rand

#define RA R16
#define RB R17

asm_rand:
          ; R24 vstup
          push RA
          push RB

          ; 7 xor 5
          bst R24, 7
          bld RA, 0
          bst R24, 5
          bld RB, 0
          eor RA, RB

          ; TMP XOR 4
          bst R24, 4
          bld RB, 0
          eor RA, RB

          ; TMP XOR 3
          bst R24, 3
          bld RB, 0
          eor RA, RB

          ; NOT TMP
          ser RB
          eor RA, RB

          ; shift R24
          lsl R24
          bst RA, 0
          bld R24, 0

          pop RB
          pop RA

          ret
