import cx_Freeze

executables = [cx_Freeze.Executable("connectFour.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ['Images/icon.png', 'soundEffects/wav/player.wav', 'soundEffects/wav/computer.wav']}},
    executables=executables

)