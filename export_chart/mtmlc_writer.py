import struct

from common import *


def write_mtmlc(lines: list, notes: list, commands: list, mtmlc_path: str) -> None:
    """
    将指令列表写入 mtmlc 谱面文件
    """

    if DEBUG_MODE:
        debug_log = open('debug.log', 'w', encoding='utf-8')

    def output_log(*data):
        if DEBUG_MODE:
            debug_log.write('\t'.join(map(lambda x: f'{x:.3f}' if type(x) == float else str(x), data))+'\n')

    output_log('[META]')
    meta = [MTMLC_WRITING_VERSION, len(lines), len(notes), len(commands)]
    output_log(*meta)

    output_log('[LINE]')
    lines_expanded = []
    for line in lines:
        lines_expanded.extend(line)
        output_log(*line)

    output_log('[NOTE]')
    notes_expanded = []
    for note in notes:
        notes_expanded.extend(note)
        output_log(*note)

    output_log('[CMD]')
    commands_expanded = []
    for time, cmd_type, parameters in commands:
        commands_expanded.extend((time, cmd_type, len(parameters), *parameters))  # 将二维列表展开成一维并添加参数数量
        output_log(time, COMMAND_NAME[cmd_type], len(parameters), parameters)

    with open(mtmlc_path, 'wb') as f:
        f.write('MTML'.encode('ascii'))
        for data in meta+lines_expanded+notes_expanded+commands_expanded:
            # 将二进制数据写入文件
            f.write(struct.pack(MTMLC_STRUCT_FORMAT[type(data)], data))

    if DEBUG_MODE:
        debug_log.close()
