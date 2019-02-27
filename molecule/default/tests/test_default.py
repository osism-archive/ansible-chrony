def test_chrony_conf_file(host):
    f = host.file("/etc/chrony/chrony.conf")
    assert f.exists
    assert f.is_file
