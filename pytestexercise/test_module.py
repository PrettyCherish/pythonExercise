# test_module.py
import pytest

'''
fixture的自动分组
如果有一个参数化的fixture，那么所有使用它的测试用例会首先使用其一个实例来执行，
直到它完成后才会去调用下一个实例。 这样做使得应用程序的测试中创建和使用全局状态更为简单
'''
'''
命令行运行：pytest -v -s test_module.py
代码具体的执行顺序是：test_0首先执行完成，然后是test_1使用mod1执行，
然后test_2使用mod1执行，然后是test_1使用mod2，最后是test_2使用mod2.

'''
@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg %s" % param)
    yield param
    print("  TEARDOWN modarg %s" % param)


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg %s" % param)
    yield param
    print("  TEARDOWN otherarg %s" % param)


def test_0(otherarg):
    print("  RUN test0 with otherarg %s" % otherarg)


def test_1(modarg):
    print("  RUN test1 with modarg %s" % modarg)


def test_2(otherarg, modarg):
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))
