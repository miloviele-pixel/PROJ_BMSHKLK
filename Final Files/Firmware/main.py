import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# Matrix pins (XIAO RP2040)
keyboard.col_pins = (
    board.GP28,  # Column 0
    board.GP29,  # Column 1
    board.GP6,   # Column 2
    board.GP7,   # Column 3
)

keyboard.row_pins = (
    board.GP26,  # Row 0
    board.GP27,  # Row 1
)

keyboard.matrix = MatrixScanner(
    cols=keyboard.col_pins,
    rows=keyboard.row_pins,
    diode_orientation='COL2ROW',
)

# Keymap (row-major order)
keyboard.keymap = [
    [
        # Top row (left → right)
        KC.Macro(Press(KC.LCMD), Press(KC.LCTRL), Tap(KC.Q), Release(KC.LCTRL), Release(KC.LCMD)),  # Lock computer
        KC.Macro(Press(KC.LCMD), Press(KC.LSHIFT), Tap(KC.N4), Release(KC.LSHIFT), Release(KC.LCMD)),  # Screenshot
        KC.Macro(Press(KC.LCMD), Tap(KC.T), Release(KC.LCMD)),  # New tab
        KC.Macro(Press(KC.LCMD), Tap(KC.W), Release(KC.LCMD)),  # Close tab

        # Bottom row (left → right)
        KC.Macro(Press(KC.LCMD), Tap(KC.Z), Release(KC.LCMD)),  # Undo
        KC.Macro(Press(KC.LCMD), Tap(KC.Y), Release(KC.LCMD)),  # Redo
        KC.Macro(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),  # Copy
        KC.Macro(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)),  # Paste
    ]
]

if __name__ == '__main__':
    keyboard.go()