import pytest


@pytest.fixture(autouse=True)
def serializable_closures(direct_vm):
    direct_vm.check_pickling = True


@pytest.fixture
def model(direct_vm):
    def respond(answer):
        direct_vm.clear_mocks()
        direct_vm.mock_llm("(?s).*", answer)
    return respond


@pytest.fixture
def consensus(direct_vm):
    def check(alternative):
        assert direct_vm.run_validator() is True
        assert direct_vm.run_validator(leader_result=alternative) is False
        assert direct_vm.run_validator(leader_result=True) is False
        assert direct_vm.run_validator(leader_error=Exception("test failure")) is False
    return check


@pytest.fixture
def direct_deploy(direct_deploy):
    def deploy(contract_path, *args, **kwargs):
        return direct_deploy(contract_path, *args, sdk_version="v0.2.16", **kwargs)
    return deploy
