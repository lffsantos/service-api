from service.util.import_files import run_importer


def test_run_importer(session):
    save_data1 = run_importer()
    for model in save_data1:
        cls, n_insert = model
        assert len(cls.query.all()) == n_insert

    # run again and no insert more data because already exists
    save_data2 = run_importer()
    for model in save_data2:
        cls, n_insert = model
        assert n_insert == 0