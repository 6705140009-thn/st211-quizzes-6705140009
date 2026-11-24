# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest


@pytest.fixture(scope="module")
def module_resource():
    return object()


@pytest.fixture
def fresh_list():
    return []


def test_fixture_cached_within_its_scope(module_resource, request):
    assert module_resource is request.getfixturevalue("module_resource")


def test_can_modify_function_fixture(fresh_list):
    fresh_list.append("student")
    assert fresh_list == ["student"]


def test_next_function_gets_empty_list(fresh_list):
    assert fresh_list == []
