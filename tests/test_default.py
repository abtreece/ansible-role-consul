import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_consul_group(Group):
    group = Group('consul')

    assert group.exists


def test_consul_user(User):
    user = User('consul')

    assert user.exists


@pytest.mark.parametrize("dir", [
    ("/etc/consul"),
    ("/etc/consul.d/bootstrap"),
    ("/etc/consul.d/server"),
    ("/etc/consul.d/client"),
    ("/opt/consul/web-ui"),
    ("/var/consul")
])
def test_etc_consul(File, dir):
    assert File(dir).exists
    assert File(dir).user == 'consul'
    assert File(dir).group == 'consul'


def test_zip_pkg(Package):
    pkg = Package('zip')

    assert pkg.is_installed


def test_consul_bin(File):
    bin = File('/usr/local/bin/consul')

    assert bin.exists


def test_upstart_init(File):
    file = File('/etc/init/consul.conf')

    assert file.exists


def test_consul_service(Service):
    svc = Service('consul')

    assert svc.is_running
    assert svc.is_enabled
