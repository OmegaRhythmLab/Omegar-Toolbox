# 对话框标题
TITLE = 'Omegar Toolbox v0.2.221028'

# 调试模式
DEBUG_MODE = True

# note 属性
NOTE_PROPERTIES = [
    'is_fake'
]
DEFAULT_PROPERTIES = {
    'is_fake': False
}

# 写入的 omgc 版本及支持读取的 omgc 版本
WRITING_OMGC_VERSION = 3
SUPPORTED_OMGC_VERSIONS = {3}

# omgc 数据存储格式
STRUCT_FORMAT = {int: '<I', float: '<f'}

# 指令列表
PLAY_MUSIC = 0x0000
ACTIVATE_NOTE = 0x0100
REMOVE_NOTE = 0x0101
CHANGE_NOTE_POS = 0x0110
CHANGE_NOTE_TRACK_LINEAR = 0x0120
CHANGE_NOTE_TRACK_SINE = 0x0121
CHANGE_LINE_ALPHA_LINEAR = 0x0200
CHANGE_LINE_ALPHA_SINE = 0x0201
CHANGE_LINE_POS_LINEAR = 0x0210
CHANGE_LINE_POS_SINE = 0x0211
CMD_NAME = {
    PLAY_MUSIC: '播放音乐',
    ACTIVATE_NOTE: '激活 note',
    REMOVE_NOTE: '移除 note',
    CHANGE_NOTE_POS: 'note 位置',
    CHANGE_NOTE_TRACK_LINEAR: 'note 轨道-线性',
    CHANGE_NOTE_TRACK_SINE: 'note 轨道-正弦',
    CHANGE_LINE_ALPHA_LINEAR: 'line 透明度-线性',
    CHANGE_LINE_ALPHA_SINE: 'line 透明度-正弦',
    CHANGE_LINE_POS_LINEAR: 'line 位置-线性',
    CHANGE_LINE_POS_SINE: 'line 位置-正弦'
}

# 画面宽高
FRAME_WIDTH = 1600
FRAME_HEIGHT = 900

# 默认判定线初始位置
LINE_INITIAL_POSITION = 800

# 缓冲时间（提前激活与推迟消失）
BUFFER_TIME = 0.5

# 缓动类型
LINEAR_SLOW_MOVING = 'linear'
SINE_SLOW_MOVING = 'sine'
