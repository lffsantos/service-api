from service.members.service_filter import filter_tree

__author__ = 'lucas'


def test_filter_tree(session):
    filters = filter_tree()
    assert filters
