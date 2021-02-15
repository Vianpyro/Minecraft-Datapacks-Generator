def Raycast(datapack_name, function_name, distance=20, step=0.3, goal=None, output=None, display_particle=None):
    return [
        f'particle {display_particle} ~ ~ ~ 0 0 0 0 1 normal @a' if display_particle is not None else None,
        f'{goal} run {output}' if goal is not None else None,
        f'execute if entity @s[distance=..{distance}] positioned ^ ^ ^{step} run function {datapack_name}:{function_name}'
    ]
