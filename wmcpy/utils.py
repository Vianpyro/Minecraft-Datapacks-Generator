def Raycast(
        datapack_name: str, function_name: str, distance: int=20, step: (int, float)=0.3,
        goal:str=None, output:str=None, display_particle:str=None
    ) -> list:
    return [
        f'particle {display_particle} ~ ~ ~ 0 0 0 0 1 normal @a' if display_particle is not None else None,
        f'{goal} run {output}' if goal is not None else None,
        f'execute if entity @s[distance=..{distance}] positioned ^ ^ ^{step} run function {datapack_name}:{function_name}'
    ]
