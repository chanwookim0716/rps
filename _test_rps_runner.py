import builtins
import importlib.util
import sys

# scripted inputs to drive the game: 메뉴->게임, 사용자 선택 '바위', then '끝내기' and '닫기'
_inputs = iter(['게임', '바위', '끝내기', '닫기'])
builtins.input = lambda prompt='': next(_inputs)

spec = importlib.util.spec_from_file_location('rps', r'c:\coding\python\rps.py')
module = importlib.util.module_from_spec(spec)
sys.modules['rps'] = module
try:
    spec.loader.exec_module(module)
    # call main() explicitly after module is loaded so scripts that use
    # `if __name__ == '__main__'` will run in this test context
    module.main()
except Exception as e:
    import traceback
    traceback.print_exc()
    raise
