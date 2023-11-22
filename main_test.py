import pytest

from sdk.config import hello

@pytest.fixture(scope="function", autouse=False)
def exec_build_image():
    hello()
    print("exec image build")



@pytest.mark.smoke
def test_example(exec_build_image):
    print('test example')

@pytest.mark.apple
def test_example_02():
    print('test example 02')

