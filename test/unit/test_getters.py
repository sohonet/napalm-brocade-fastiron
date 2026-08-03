"""Tests for getters."""

from napalm.base import models
from napalm.base.test import helpers
from napalm.base.test.getters import BaseTestGetters, wrap_test_cases


import pytest


@pytest.mark.usefixtures("set_device_parameters")
class TestGetter(BaseTestGetters):
    """Test get_* methods."""

    # Skip test_method_signatures - we have additional getters
    def test_method_signatures(self):
        return True

    # get_interfaces_ip reports is_virtual on a VRRP/VRRP-E virtual address, and
    # napalm's InterfacesIPDictEntry has no room for it. test_model has no
    # extra-keys-allowed mode, so drop that one key and validate the rest against the
    # model exactly as the base test does.
    @wrap_test_cases
    def test_get_interfaces_ip(self, test_case):
        """Test get_interfaces_ip."""
        get_interfaces_ip = self.device.get_interfaces_ip()
        assert len(get_interfaces_ip) > 0

        for interface_details in get_interfaces_ip.values():
            for family in ("ipv4", "ipv6"):
                for details in interface_details.get(family, {}).values():
                    assert helpers.test_model(
                        models.InterfacesIPDictEntry,
                        {key: value for key, value in details.items() if key != "is_virtual"},
                    )

        return get_interfaces_ip

    # Unsupported functions
    def test_get_interfaces_counters(self):
        return True

    def test_get_environment(self):
        return True

    def test_get_arp_table_with_vrf(self):
        return True

    def test_get_ntp_peers(self):
        return True

    def test_get_ntp_servers(self):
        return True

    def test_get_ntp_stats(self):
        return True

    def test_get_users(self):
        return True

    def test_get_config(self):
        return True

    def test_get_config_filtered(self):
        return True

    def test_get_config_sanitized(self):
        return True

    def test_get_lldp_neighbors_detail(self):
        return True

    def test_get_bgp_neighbors_detail(self):
        return True
