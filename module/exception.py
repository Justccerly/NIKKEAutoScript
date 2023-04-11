class RequestHumanTakeover(Exception):
    # 请求人工接管
    pass


class EmulatorNotRunningError(Exception):
    # 模拟器未运行
    pass


class ScriptError(Exception):
    # This is likely to be a mistake of developers, but sometimes a random issue
    pass


class GameTooManyClickError(Exception):
    pass


class GameStuckError(Exception):
    pass


class GameNotRunningError(Exception):
    pass


class GamePageUnknownError(Exception):
    pass
