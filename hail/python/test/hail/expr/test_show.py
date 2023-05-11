import hail as hl

def test_show():
    mt = hl.balding_nichols_model(3, 10, 10)
    t = mt.rows()
    mt.GT.show()
    mt.locus.show()
    mt.af.show()
    mt.pop.show()
    mt.sample_idx.show()
    mt.bn.show()
    mt.bn.fst.show()
    mt.GT.n_alt_alleles().show()
    (mt.GT.n_alt_alleles() * mt.GT.n_alt_alleles()).show()
    (mt.af * mt.GT.n_alt_alleles()).show()
    t.af.show()
    (t.af * 3).show()


def test_show_negative():
    hl.utils.range_table(5).show(-1)


def test_show_mt_duplicate_col_key():
    shown_cols = 2

    mt = hl.utils.range_matrix_table(5, 5)
    mt = mt.key_cols_by(c = 0)
    showobj = mt.show(n_cols=shown_cols, handler=lambda x: x)

    assert len(showobj.table_show.table.row) == len(mt.row) + shown_cols


def test_show_mt_fewer_cols():
    shown_cols = 7

    mt = hl.utils.range_matrix_table(5, 5)
    mt = mt.key_cols_by(c = 0)
    showobj = mt.show(n_cols=shown_cols, handler=lambda x: x)

    assert len(showobj.table_show.table.row) == len(mt.row) + mt.count_cols()


